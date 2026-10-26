#!/usr/bin/env python3
"""Report links whose #anchor names no heading in the target page (same-page and cross-page).

Anchors follow GitHub's algorithm (lowercase, punctuation removed, spaces to hyphens, -1, -2 for repeats).
Links to files that do not exist are validate.py's job and are skipped here. Report only: exits 0 unless
--strict is given and an anchor is missing.

Usage: python3 -I scripts/check-links.py [--strict]
"""
import argparse
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import docslib as D  # noqa: E402


def anchors_of(rel, cache):
    if rel not in cache:
        seen, out = set(), set()
        path = os.path.join(D.DOCS, rel)
        if os.path.isfile(path):
            try:
                _, _, body, start = D.split_front_matter(open(path, encoding="utf-8").read())
            except D.FrontMatterError:
                body, start = open(path, encoding="utf-8").read(), 1
            for _, line, fence, _ in D.iter_lines(body, start):
                h = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
                if h and not fence:
                    out.add(D.github_slug(h.group(1), seen))
                if not fence:
                    for a in re.findall(r'<a\s+(?:name|id)="([^"]+)"', line):
                        out.add(a)
        cache[rel] = out
    return cache[rel]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()
    cache, checked, missing = {}, 0, 0
    for rel in D.page_files():
        try:
            _, _, body, start = D.split_front_matter(open(os.path.join(D.DOCS, rel), encoding="utf-8").read())
        except D.FrontMatterError:
            continue
        for n, line, fence, _ in D.iter_lines(body, start):
            if fence:
                continue
            for mm in D.LINK.finditer(D.strip_inline_code(line)):
                url = mm.group(3).strip("<>")
                if mm.group(1) or "#" not in url or re.match(r"^[a-z][a-z0-9+.-]*:", url) or url.startswith("/"):
                    continue
                target, frag = url.split("#", 1)
                tgt = rel if not target else os.path.normpath(os.path.join(os.path.dirname(rel), urllib.parse.unquote(target)))
                if os.path.isdir(os.path.join(D.DOCS, tgt)):
                    tgt = os.path.join(tgt, "README.md")
                if not tgt.endswith(".md") or not os.path.isfile(os.path.join(D.DOCS, tgt)):
                    continue
                checked += 1
                frag = urllib.parse.unquote(frag)
                names = anchors_of(tgt, cache)
                if frag not in names and frag.lower() not in names:
                    missing += 1
                    print(f"docs/{rel}:{n}: anchor #{frag} not found in docs/{tgt}")
    print(f"{checked} anchored links checked, {missing} missing")
    return 1 if a.strict and missing else 0


if __name__ == "__main__":
    sys.exit(main())
