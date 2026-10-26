#!/usr/bin/env python3
"""Validate every page under docs/ against conventions/front-matter.md and conventions/markdown.md.

Errors (exit 1):
  file         UTF-8, LF line endings, no byte order mark
  front matter present; parses; no '---' inside; only known fields; title, description and type present and
               non-empty; type one of tutorial, guide, concept, reference; description one line, under 200
               characters, no em-dash; order an integer; status placeholder or draft; updated YYYY-MM-DD;
               redirect_from a list of root-relative paths with a trailing slash
  title        the first body line is '# ' + title; exactly one H1; headings do not skip levels
  tree         slugs unique; redirect_from paths unique and never equal to a live path; every folder that holds
               pages, directly or in a subfolder, has a README.md
  Markdown     no em-dashes (or &mdash; entities) in prose; raw HTML only kbd, details, summary, sub, sup and
               comments; alerts use NOTE, TIP, IMPORTANT, WARNING or CAUTION; fenced code (also inside a
               blockquote) has a language and is closed; no block markup (<!-- wp:) outside code; no footnotes;
               no setext headings (=== or --- under a line)
  links        relative links (inline, wrapped across lines, or reference definitions) point at a file that exists
               (a .md page, or a folder's README.md); no root-relative links; no github.com links into this
               repository; relative images exist
Warnings: images without alt text; an alert directly after another blockquote; description equal to the lede.

Usage: python3 -I scripts/validate.py [--quiet] [files ...]
"""
import argparse
import collections
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import docslib as D  # noqa: E402

TYPES = ("tutorial", "guide", "concept", "reference")
STATUSES = ("placeholder", "draft")
FIELDS = {"title", "description", "type", "order", "slug", "id", "status", "redirect_from", "applies_to", "updated"}
ALERTS = ("NOTE", "TIP", "IMPORTANT", "WARNING", "CAUTION")
ALLOWED_HTML = {"kbd", "details", "summary", "sub", "sup"}
EM = "—"
EM_RE = re.compile(r"—|&mdash;|&#0*8212;|&#x0*2014;", re.I)


class Report:
    def __init__(self):
        self.errors, self.warnings = [], []

    def err(self, where, line, msg):
        self.errors.append((where, line, msg))

    def warn(self, where, line, msg):
        self.warnings.append((where, line, msg))


def prose(line):
    """The line without inline code, link targets and bare URLs (em-dashes there are not prose)."""
    t = D.strip_inline_code(line)
    t = re.sub(r"\]\([^)]*\)", "]()", t)
    t = re.sub(r"<https?://[^>]+>|https?://\S+", "", t)
    return t


def html_tags(bare):
    """Tag names of raw HTML on a line that has had inline code and comments removed. Angle-bracket link
    destinations (`](<a b.png>)`) and autolinks are not HTML."""
    t = re.sub(r"\]\(\s*<[^>]*>", "](", bare)
    t = re.sub(r"<[a-zA-Z][a-zA-Z0-9+.-]*:[^>\s]*>", "", t)
    return sorted({m.group(1).lower() for m in re.finditer(r"</?([a-zA-Z][a-zA-Z0-9-]*)(?=[\s>/]|$)", t)})


def strip_comments(line, in_comment):
    """(line without HTML comments, still inside a comment at the end of the line)."""
    out, i = "", 0
    while i < len(line):
        if in_comment:
            j = line.find("-->", i)
            if j < 0:
                return out, True
            i, in_comment = j + 3, False
        else:
            j = line.find("<!--", i)
            if j < 0:
                return out + line[i:], False
            out += line[i:j]
            i, in_comment = j + 4, True
    return out, in_comment


def check_page(rel, r, pages, slugs, redirects):
    where = f"docs/{rel}"
    with open(os.path.join(D.DOCS, rel), "rb") as fh:
        raw = fh.read()
    if raw.startswith(b"\xef\xbb\xbf"):
        r.err(where, 1, "byte order mark (the importer would render the front matter)")
        raw = raw[3:]
    if b"\r" in raw:
        r.err(where, 1, "CR line endings; use LF")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        r.err(where, 1, f"not UTF-8 ({exc})")
        return
    try:
        fm, fm_raw, body, start = D.split_front_matter(text)
    except D.FrontMatterError as exc:
        r.err(where, 1, f"front matter: {exc}")
        return
    if fm is None:
        r.err(where, 1, "missing front matter (--- ... --- at the top)")
        return
    if "---" in fm_raw:
        r.err(where, 1, "front matter contains '---' (the importer ends front matter at the first ---)")
    for k in fm:
        if k not in FIELDS:
            r.err(where, 1, f"unknown front matter field {k!r}")
    for k in ("title", "description", "type"):
        if not isinstance(fm.get(k), str) or not fm[k].strip():
            r.err(where, 1, f"front matter {k} is missing or empty")
    title = fm.get("title") if isinstance(fm.get("title"), str) else ""
    if isinstance(fm.get("type"), str) and fm["type"] and fm["type"] not in TYPES:
        r.err(where, 1, f"type {fm['type']!r} is not one of {', '.join(TYPES)}")
    desc = fm.get("description")
    if isinstance(desc, str):
        if "\n" in desc:
            r.err(where, 1, "description must be one line")
        if len(desc) >= 200:
            r.err(where, 1, f"description is {len(desc)} characters (keep it under 200)")
    for k in ("title", "description"):
        if isinstance(fm.get(k), str) and EM_RE.search(fm[k]):
            r.err(where, 1, f"em-dash in {k}")
    if "order" in fm and not isinstance(fm["order"], int):
        r.err(where, 1, "order must be an integer")
    if "status" in fm and fm["status"] not in STATUSES:
        r.err(where, 1, f"status {fm['status']!r} is not one of {', '.join(STATUSES)}")
    if "updated" in fm and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(fm["updated"])):
        r.err(where, 1, "updated must be YYYY-MM-DD")
    for k in ("slug", "id"):
        if k in fm and (not isinstance(fm[k], str) or not fm[k]):
            r.err(where, 1, f"{k} must be a non-empty string")
    for k in ("redirect_from", "applies_to"):
        if k in fm and not isinstance(fm[k], list):
            r.err(where, 1, f"{k} must be a list")
    slug = fm.get("slug") if isinstance(fm.get("slug"), str) else None
    if not slug:
        slug = os.path.basename(os.path.dirname(rel)) if os.path.basename(rel) == "README.md" else rel[:-3].split("/")[-1]
        if rel == "README.md":
            slug = "docs"
    slugs[slug].append(rel)
    for red in fm.get("redirect_from") or [] if isinstance(fm.get("redirect_from"), list) else []:
        if not isinstance(red, str) or not re.fullmatch(r"/\S*/", red):
            r.err(where, 1, f"redirect_from {red!r} must be a root-relative path with a trailing slash")
            continue
        redirects[red].append(rel)

    # Body.
    lines = body.split("\n")
    first_idx = next((i for i, x in enumerate(lines) if x.strip()), None)
    if first_idx is None:
        r.err(where, start, "empty body")
        return
    if lines[first_idx] != f"# {title}":
        r.err(where, start + first_idx, f"first body line must be '# {title}', got {lines[first_idx][:70]!r}")
    if fm.get("description") and isinstance(fm.get("description"), str):
        lede = next((x for x in lines[first_idx + 1:] if x.strip()), "")
        if lede.strip() == fm["description"].strip():
            r.warn(where, start, "description repeats the first paragraph word for word")
    base = os.path.dirname(rel)
    h1s, prev_level, prev_line, last_quote, in_comment = 0, 1, "", -10, False
    state = {}
    for n, line, in_fence, info in D.iter_lines(body, start, state):
        if in_fence:
            if info is not None and not info:
                r.err(where, n, "fenced code block without a language (```text if nothing else fits)")
            prev_line = line
            continue
        bare = D.strip_inline_code(line)
        nocomment, in_comment = strip_comments(bare, in_comment)
        h = re.match(r"^(#{1,6})\s+\S", line)
        if h:
            lvl = len(h.group(1))
            if lvl == 1:
                h1s += 1
                if h1s > 1:
                    r.err(where, n, "second H1; use ## for sections")
            elif lvl > prev_level + 1:
                r.err(where, n, f"heading level skips from H{prev_level} to H{lvl}")
            prev_level = lvl
        if re.match(r"^ {0,3}(=+|-+)[ \t]*$", line) and prev_line.strip() and not D.FENCE.match(prev_line) \
                and not re.match(r"^\s*([-*+](\s|$)|[>|#<]|\d+[.)](\s|$))", prev_line) and not re.match(r"^ {0,3}(=+|-+)[ \t]*$", prev_line):
            r.err(where, n, "setext heading (a line of = or - under text); use # headings, or a blank line before ---")
        if EM_RE.search(prose(line)):
            r.err(where, n, "em-dash in prose; use a comma, a colon, parentheses or two sentences")
        if "<!-- wp:" in bare:
            r.err(where, n, "block markup '<!-- wp:' outside a code fence (disables wpautop on the whole page)")
        for tag in html_tags(nocomment):
            if tag not in ALLOWED_HTML:
                r.err(where, n, f"raw HTML <{tag}> (allowed: {', '.join(sorted(ALLOWED_HTML))} and comments)")
        a = re.match(r"^\s*>\s*\[!([^\]]+)\]", line)
        if a:
            if a.group(1) not in ALERTS:
                r.err(where, n, f"alert type {a.group(1)!r} (allowed: {', '.join(ALERTS)})")
            elif not re.match(r"^\s*>\s*\[![A-Z]+\]\s*$", line):
                r.err(where, n, "the alert type line must be alone on its line")
            if last_quote == n - 2 and not prev_line.strip():
                r.warn(where, n, "alert directly after another blockquote; put a paragraph between them")
        if line.lstrip().startswith(">"):
            last_quote = n
        if re.search(r"\[\^[^\]]+\]", bare):
            r.err(where, n, "footnotes are not supported; put the note in the sentence or a NOTE alert")
        prev_line = line
    if state.get("open_fence"):
        r.err(where, state["open_fence"], "code fence is never closed")
    for n, bang, label, url in D.iter_links(body, start):
        check_link(where, base, n, bang, label, url, r, pages)
    if h1s == 0:
        r.err(where, start, "no H1")


def check_link(where, base, n, bang, label, url, r, pages):
    if not url or url.startswith("#") or url.startswith("mailto:"):
        if bang and not label.strip():
            r.warn(where, n, "image without alt text")
        return
    if bang and not label.strip():
        r.warn(where, n, f"image without alt text ({url[:70]})")
    if re.match(r"^https?://", url):
        u = urllib.parse.urlsplit(url)
        if u.netloc in ("github.com", "raw.githubusercontent.com") and \
                u.path.lower().startswith("/ndiego/wordpress-documentation/"):
            r.err(where, n, f"link into this repository must be a relative path, not {url}")
        return
    if re.match(r"^[a-z][a-z0-9+.-]*:", url):
        return
    if url.startswith("/"):
        r.err(where, n, f"root-relative link {url}; link to the Markdown file with a relative path")
        return
    target = urllib.parse.unquote(url.split("#", 1)[0].split("?", 1)[0])
    resolved = os.path.normpath(os.path.join(base, target))
    full = os.path.join(D.DOCS, resolved)
    if bang:
        if not os.path.isfile(full):
            r.err(where, n, f"image {url} does not exist")
        return
    if resolved.startswith(".."):
        if not os.path.exists(os.path.join(D.DOCS, resolved)):
            r.err(where, n, f"link target {url} does not exist")
        return
    if os.path.isdir(full):
        if os.path.isfile(os.path.join(full, "README.md")):
            r.err(where, n, f"link to a folder {url}; link to its README.md")
        else:
            r.err(where, n, f"link target {url} is a folder without a README.md")
        return
    if resolved.endswith(".md"):
        if resolved not in pages:
            r.err(where, n, f"link target {url} does not exist")
    elif not os.path.isfile(full):
        r.err(where, n, f"link target {url} does not exist")


def check_folders(pages, r):
    """Every folder on the path to a page has a README.md (the folder's own page and the parent of its pages)."""
    page_set, missing = set(pages), set()
    for rel in pages:
        d = os.path.dirname(rel)
        while d:
            if os.path.join(d, "README.md") not in page_set:
                missing.add(d)
            d = os.path.dirname(d)
    for d in sorted(missing):
        r.err(f"docs/{d}/", 1, "folder has pages (directly or in a subfolder) but no README.md")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--quiet", action="store_true", help="print errors and the summary only")
    ap.add_argument("files", nargs="*", help="limit the per-page report to these files (tree checks still run)")
    a = ap.parse_args()
    r = Report()
    pages = D.page_files()
    page_set = set(pages)
    slugs, redirects = collections.defaultdict(list), collections.defaultdict(list)
    for rel in pages:
        check_page(rel, r, page_set, slugs, redirects)
    for slug, rels in sorted(slugs.items()):
        if len(rels) > 1:
            for rel in rels:
                r.err(f"docs/{rel}", 1, f"slug {slug!r} is also used by {', '.join(x for x in rels if x != rel)}")
    live = {"/docs/" + D.live_path(rel) for rel in pages}
    for red, rels in sorted(redirects.items()):
        if len(rels) > 1:
            r.err(f"docs/{rels[1]}", 1, f"redirect_from {red} also on {', '.join(rels[:1] + rels[2:])}")
        if red in live or red.rstrip("/") + "/" in live:
            r.err(f"docs/{rels[0]}", 1, f"redirect_from {red} is the path of a live page")
    check_folders(pages, r)
    only = {os.path.relpath(os.path.abspath(f), D.REPO) for f in a.files}
    errors = [e for e in r.errors if not only or e[0] in only or e[0].endswith("/")]
    warnings = [w for w in r.warnings if not only or w[0] in only]
    for where, line, msg in errors:
        print(f"{where}:{line}: error: {msg}")
    if not a.quiet:
        for where, line, msg in warnings:
            print(f"{where}:{line}: warning: {msg}")
    print(f"{len(pages)} pages; {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
