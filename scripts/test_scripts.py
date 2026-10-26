#!/usr/bin/env python3
"""Regression tests for docslib.py, validate.py, build-manifest.py and check-links.py, with inline pages.

Usage: python3 -I scripts/test_scripts.py [-v]
"""
import collections
import importlib.util
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import docslib as D  # noqa: E402


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, file))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


V = load("validate", "validate.py")
B = load("build_manifest", "build-manifest.py")

FM = "---\ntitle: T\ndescription: D\ntype: guide\n---\n\n# T\n\n"


class Tree(unittest.TestCase):
    """Each test gets an empty docs/ folder; D.DOCS points at it."""

    def setUp(self):
        self.dir = tempfile.mkdtemp()
        self.saved = D.DOCS
        D.DOCS = self.dir

    def tearDown(self):
        D.DOCS = self.saved
        shutil.rmtree(self.dir)

    def write(self, rel, content):
        path = os.path.join(self.dir, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as fh:
            fh.write(content if isinstance(content, bytes) else content.encode("utf-8"))

    def errors(self, body, rel="x/p.md", extra=()):
        """Validate one page (plus any extra files) and return its error messages."""
        self.write(rel, body)
        for k, v in extra:
            self.write(k, v)
        r = V.Report()
        pages = set(D.page_files())
        V.check_page(rel, r, pages, collections.defaultdict(list), collections.defaultdict(list))
        return [m for _, _, m in r.errors]

    def assertFlags(self, body, fragment, **kw):
        errs = self.errors(body, **kw)
        self.assertTrue(any(fragment in e for e in errs), f"expected {fragment!r} in {errs}")

    def assertClean(self, body, **kw):
        self.assertEqual(self.errors(body, **kw), [])


class Setext(Tree):
    def test_dash_underline_is_a_heading(self):
        self.assertFlags(FM + "Para\n---\n", "setext")

    def test_equals_underline_is_a_heading(self):
        self.assertFlags(FM + "Para\n===\n", "setext")

    def test_thematic_break_after_blank_line_is_fine(self):
        self.assertClean(FM + "Para\n\n---\n")

    def test_dashes_after_a_list_item_or_fence_are_fine(self):
        self.assertClean(FM + "- item\n---\n")
        self.assertClean(FM + "Para\n\n```text\nx\n```\n---\n")

    def test_dashes_after_emphasis_paragraph_are_a_heading(self):
        self.assertFlags(FM + "*Caption*\n---\n", "setext")


class Links(Tree):
    def test_wrapped_link_text_is_checked(self):
        self.assertFlags(FM + "See [Create a\npost](../nope.md).\n", "does not exist")

    def test_wrapped_link_reports_its_first_line(self):
        self.write("x/p.md", FM + "Intro.\n\nSee [Create a\npost](../nope.md).\n")
        r = V.Report()
        V.check_page("x/p.md", r, set(D.page_files()), collections.defaultdict(list), collections.defaultdict(list))
        self.assertEqual([n for _, n, m in r.errors if "nope" in m], [11])

    def test_wrapped_link_to_existing_page_is_fine(self):
        self.assertClean(FM + "See [the other\npage](q.md).\n", extra=[("x/q.md", FM)])

    def test_reference_definitions_are_checked(self):
        self.assertFlags(FM + "See [x][a].\n\n[a]: ../nope.md\n", "does not exist")
        self.assertFlags(FM + "See [x][b].\n\n[b]: /docs/foo/\n", "root-relative")

    def test_reference_definition_to_existing_page_is_fine(self):
        self.assertClean(FM + "See [x][a].\n\n[a]: q.md\n", extra=[("x/q.md", FM)])

    def test_links_inside_fences_are_ignored(self):
        self.assertClean(FM + "```markdown\n[x](../nope.md)\n[a]: ../nope.md\n```\n")

    def test_nested_readme_resolves_relative_to_its_folder(self):
        extra = [("design/README.md", FM), ("design/site-editor/images/a.png", b"png")]
        self.assertClean(FM + "[Up](../README.md) ![A](images/a.png)\n", rel="design/site-editor/README.md", extra=extra)


class EmDash(Tree):
    def test_literal_and_entities(self):
        for dash in ("—", "&mdash;", "&#8212;", "&#x2014;"):
            self.assertFlags(FM + f"One {dash} two.\n", "em-dash")

    def test_entity_in_front_matter(self):
        self.assertFlags("---\ntitle: T\ndescription: A &mdash; b\ntype: guide\n---\n\n# T\n", "em-dash")

    def test_entity_in_code_is_fine(self):
        self.assertClean(FM + "Write `&mdash;` in HTML.\n")


class Fences(Tree):
    def test_fence_inside_blockquote_is_code(self):
        self.assertClean(FM + "> ```html\n> <div>\n> <!-- wp:paragraph -->\n> [!FOO]\n> ```\n")

    def test_fence_inside_blockquote_needs_a_language(self):
        self.assertFlags(FM + "> ```\n> x\n> ```\n", "without a language")

    def test_fence_ends_with_its_blockquote(self):
        self.assertFlags(FM + "> ```text\n> x\n\n<div>\n", "raw HTML <div>")

    def test_hash_dashes_and_alerts_inside_fences(self):
        self.assertClean(FM + "```bash\n# comment\n---\n> [!FOO]\n<div>\n```\n\n## Ok\n")

    def test_unclosed_fence(self):
        self.assertFlags(FM + "```text\nfoo\n\n## H\n", "never closed")


class RawHtml(Tree):
    def test_html_inside_comments_is_fine(self):
        self.assertClean(FM + "<!-- use <div> here -->\n")
        self.assertClean(FM + "<!-- a\n<div>\n-->\n")

    def test_html_after_a_comment_is_flagged(self):
        self.assertFlags(FM + "<!-- c --> <span>x</span>\n", "raw HTML <span>")

    def test_angle_bracket_destination_is_not_html(self):
        self.assertClean(FM + "![A](<images/a b.png>)\n", extra=[("x/images/a b.png", b"png")])

    def test_autolink_is_not_html(self):
        self.assertClean(FM + "See <https://example.com/>.\n")

    def test_tag_at_end_of_line(self):
        self.assertFlags(FM + "<div\n  class='x'>\n", "raw HTML <div>")

    def test_allowed_tags(self):
        self.assertClean(FM + "Press <kbd>Ctrl</kbd> and H<sub>2</sub>O.\n")


class FrontMatter(Tree):
    def test_trailing_comment_is_stripped(self):
        self.assertEqual(D.parse_yaml("title: T # comment"), {"title": "T"})
        self.assertEqual(D.parse_yaml('title: "A # b" # c'), {"title": "A # b"})
        self.assertEqual(D.parse_yaml("title: C# tips"), {"title": "C# tips"})
        self.assertClean("---\ntitle: T # comment\ndescription: D\ntype: guide\n---\n\n# T\n")

    def test_unquoted_colon_space_is_rejected(self):
        with self.assertRaises(D.FrontMatterError):
            D.parse_yaml("title: A: b")
        self.assertFlags("---\ntitle: A: b\ndescription: D\ntype: guide\n---\n\n# A: b\n", "quote it")

    def test_quoted_colon_is_fine(self):
        self.assertEqual(D.parse_yaml('title: "A: b"'), {"title": "A: b"})
        self.assertEqual(D.parse_yaml("url: https://example.com/"), {"url": "https://example.com/"})

    def test_flow_list_with_quoted_comma(self):
        self.assertEqual(D.parse_yaml('redirect_from: ["/a,b/", /c/]'), {"redirect_from": ["/a,b/", "/c/"]})

    def test_closed_at_end_of_file(self):
        fm, raw, body, start = D.split_front_matter("---\ntitle: T\n---")
        self.assertEqual(fm, {"title": "T"})
        self.assertEqual(body, "")

    def test_empty_front_matter(self):
        fm, raw, body, start = D.split_front_matter("---\n---\n\n# T\n")
        self.assertEqual(fm, {})
        self.assertEqual(start, 3)

    def test_dashes_inside_a_value_do_not_close(self):
        fm, raw, _, _ = D.split_front_matter("---\ntitle: a---b\n---\n")
        self.assertEqual(fm, {"title": "a---b"})

    def test_edge_files_do_not_crash(self):
        self.assertFlags("", "missing front matter")
        self.assertFlags("# T\n", "missing front matter")
        self.assertFlags(b"\xff\xfe\x00", "not UTF-8")


class Folders(Tree):
    def test_folder_on_the_path_without_readme(self):
        for rel in ("a/README.md", "a/b/c/README.md", "a/b/c/p.md"):
            self.write(rel, FM)
        r = V.Report()
        V.check_folders(D.page_files(), r)
        self.assertEqual([w for w, _, _ in r.errors], ["docs/a/b/"])


class Manifest(Tree):
    def page(self, title, extra=""):
        return f"---\ntitle: {title}\ndescription: D\ntype: guide\n{extra}---\n\n# {title}\n"

    def test_contract_shape(self):
        self.write("README.md", self.page("Home"))
        self.write("a/README.md", self.page("A", "order: 20\n"))
        self.write("a/y.md", self.page("Y", "order: 15\n"))
        self.write("a/x.md", self.page("X"))
        self.write("a/w.md", self.page("W"))
        self.write("b/README.md", self.page("B", "order: 10\n"))
        m, errors = B.build()
        self.assertEqual(errors, [])
        self.assertEqual(list(m), ["index", "b", "a", "a/y", "a/w", "a/x"])
        self.assertEqual(m["index"]["path"], "")
        self.assertIsNone(m["index"]["parent"])
        self.assertEqual(m["index"]["order"], 0)
        self.assertIsNone(m["a"]["parent"])
        self.assertEqual(m["a/x"]["parent"], "a")
        self.assertEqual([m[k]["order"] for k in ("a/y", "a/w", "a/x")], [15, 20, 30])
        self.assertEqual(m["a/x"]["path"], "a/x/")
        self.assertEqual(list(m["a/x"]), sorted(m["a/x"]))
        self.assertEqual(B.render(m), B.render(B.build()[0]))

    def test_parent_is_nearest_ancestor_with_readme(self):
        self.write("a/README.md", self.page("A"))
        self.write("a/b/c/README.md", self.page("C"))
        self.write("a/b/c/p.md", self.page("P"))
        m, _ = B.build()
        self.assertEqual(m["a/b/c"]["parent"], "a")
        self.assertEqual(m["a/b/c/p"]["parent"], "a/b/c")

    def test_front_matter_errors_fail(self):
        self.write("a/README.md", self.page("A"))
        self.write("a/bad.md", "---\ntitle: A: b\n---\n")
        self.write("a/none.md", "# None\n")
        self.write("a/latin.md", b"\xff\xfe")
        _, errors = B.build()
        self.assertEqual(len(errors), 3, errors)

    def test_duplicate_slug_fails(self):
        self.write("a/README.md", self.page("A"))
        self.write("a/x.md", self.page("X"))
        self.write("a/z.md", self.page("Z", "slug: x\n"))
        _, errors = B.build()
        self.assertTrue(any("slug 'x'" in e for e in errors), errors)


class IterLinks(unittest.TestCase):
    def test_line_numbers_and_kinds(self):
        body = "a [one](1.md)\n\nb [two\nlines](2.md)\n\n[r]: 3.md\n"
        self.assertEqual([(n, url) for n, _, _, url in D.iter_links(body, 10)], [(10, "1.md"), (12, "2.md"), (15, "3.md")])

    def test_footnote_definition_is_not_a_reference(self):
        self.assertEqual(list(D.iter_links("[^1]: note\n")), [])


if __name__ == "__main__":
    unittest.main()
