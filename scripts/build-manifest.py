#!/usr/bin/env python3
"""Derive manifest.json from the tree under docs/ (format: wordpress-documentation-site/CONTRACT.md).

- Key: the page's path without trailing slash (write/create-a-post); a folder's README.md is the folder
  (write/publish); the home docs/README.md is `index` with path "" and parent null.
- Parent: the README.md of the folder a page sits in; for a README.md, the README.md of the folder above.
  Section landings (docs/<section>/README.md) are top-level posts: parent null.
- Order: `order` from front matter; siblings without one follow, alphabetically by title, numbered on from
  the highest explicit order in steps of 10 (10, 20, 30 when no sibling has one).
- slug: front matter, else the file name (README.md: the folder name). id: front matter, else the key.
  section: the first path segment ("" for the home).
- Entries are written parents first, in sidebar order; keys inside each entry are sorted; one tab indent.

Usage: python3 -I scripts/build-manifest.py [--check]
  --check   do not write; exit 1 when manifest.json differs from what the tree produces
"""
import argparse
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import docslib as D  # noqa: E402

OUT = os.path.join(D.REPO, "manifest.json")


def load_pages():
    pages = {}
    for rel in D.page_files():
        text = open(os.path.join(D.DOCS, rel), encoding="utf-8-sig").read().replace("\r\n", "\n")
        try:
            fm, _, _, _ = D.split_front_matter(text)
        except D.FrontMatterError as exc:
            print(f"docs/{rel}: front matter: {exc}", file=sys.stderr)
            fm = None
        pages[rel] = fm or {}
    return pages


def parent_of(rel, keys_by_rel):
    """The key of the nearest README.md above this page, or None for the home and section landings."""
    if rel == "README.md":
        return None
    d = os.path.dirname(rel)
    if os.path.basename(rel) == "README.md":
        d = os.path.dirname(d)
    while True:
        if d == "":
            return None  # section landings are top-level posts; the home has no parent
        cand = os.path.join(d, "README.md")
        if cand in keys_by_rel:
            return keys_by_rel[cand]
        d = os.path.dirname(d)


def build():
    pages = load_pages()
    keys = {rel: D.page_key(rel) for rel in pages}
    entries = {}
    for rel, fm in pages.items():
        key = keys[rel]
        if os.path.basename(rel) == "README.md":
            default_slug = "docs" if rel == "README.md" else os.path.basename(os.path.dirname(rel))
        else:
            default_slug = os.path.basename(rel)[:-3]
        lst = lambda v: v if isinstance(v, list) else ([] if v in (None, "") else [v])  # noqa: E731
        entries[key] = {
            "title": str(fm.get("title") or ""),
            "slug": str(fm.get("slug") or default_slug),
            "parent": parent_of(rel, keys),
            "order": fm.get("order") if isinstance(fm.get("order"), int) else (0 if key == "index" else None),
            "markdown_source": D.SOURCE_BASE + rel,
            "id": str(fm.get("id") or key),
            "path": D.live_path(rel),
            "section": "" if key == "index" else key.split("/")[0],
            "type": str(fm.get("type") or ""),
            "status": str(fm.get("status") or ""),
            "description": str(fm.get("description") or ""),
            "updated": str(fm.get("updated") or ""),
            "redirect_from": [str(x) for x in lst(fm.get("redirect_from"))],
            "applies_to": [str(x) for x in lst(fm.get("applies_to"))],
        }
    children = collections.defaultdict(list)
    for key, e in entries.items():
        if key != "index":
            children[e["parent"]].append(key)
    for parent, kids in children.items():
        explicit = [entries[k]["order"] for k in kids if entries[k]["order"] is not None]
        nxt = (max(explicit) // 10 + 1) * 10 if explicit else 10
        for k in sorted((k for k in kids if entries[k]["order"] is None), key=lambda k: (entries[k]["title"].lower(), k)):
            entries[k]["order"] = nxt
            nxt += 10
        kids.sort(key=lambda k: (entries[k]["order"], entries[k]["title"].lower(), k))
    ordered = collections.OrderedDict()

    def walk(key):
        ordered[key] = dict(sorted(entries[key].items()))
        for k in children.get(key, []):
            walk(k)

    if "index" in entries:
        walk("index")
    for k in children.get(None, []):
        walk(k)
    return ordered


def render(manifest):
    return json.dumps(manifest, indent="\t", ensure_ascii=False) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    text = render(build())
    current = open(OUT, encoding="utf-8").read() if os.path.isfile(OUT) else None
    if a.check:
        if current != text:
            print("manifest.json is out of date; run python3 -I scripts/build-manifest.py")
            return 1
        print("manifest.json is up to date")
        return 0
    if current != text:
        with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print(f"wrote manifest.json ({text.count(chr(10) + chr(9) + chr(34))} pages)")
    else:
        print("manifest.json unchanged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
