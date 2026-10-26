"""Shared helpers for validate.py, build-manifest.py and check-links.py. Stdlib only."""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DOCS = os.path.join(REPO, "docs")
REPO_URL = "https://github.com/ndiego/wordpress-documentation"
SOURCE_BASE = f"{REPO_URL}/blob/trunk/docs/"

FRONT = re.compile(r"\A---\n(.*?)\n---\n", re.S)
FENCE = re.compile(r"^(\s*)(`{3,}|~{3,})(.*)$")
INLINE_CODE = re.compile(r"(`+)(.+?)\1")
LINK = re.compile(r"(!?)\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(\s*(<[^>]*>|[^()\s]*(?:\([^()\s]*\)[^()\s]*)*)(?:\s+\"[^\"]*\")?\s*\)")


class FrontMatterError(ValueError):
    pass


def page_files():
    """Every page, as a path relative to docs/, sorted. assets/ holds no pages."""
    out = []
    for dp, dn, fn in os.walk(DOCS):
        dn[:] = sorted(d for d in dn if not (dp == DOCS and d == "assets") and not d.startswith("."))
        for f in fn:
            if f.endswith(".md"):
                out.append(os.path.relpath(os.path.join(dp, f), DOCS))
    return sorted(out)


def unquote(v, where=""):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] == '"':
        return re.sub(r'\\(.)', lambda m: {"n": "\n", "t": "\t"}.get(m.group(1), m.group(1)), v[1:-1])
    if len(v) >= 2 and v[0] == v[-1] == "'":
        return v[1:-1].replace("''", "'")
    if v[:1] in ('"', "'"):
        raise FrontMatterError(f"unterminated quoted string {v[:40]!r}")
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    return v


def parse_yaml(text):
    """The YAML subset front matter uses: `key: scalar`, `key: [a, b]`, `key:` + `  - item` lines, # comments."""
    fm, key = {}, None
    for n, line in enumerate(text.split("\n"), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        li = re.match(r"^\s+-\s*(.*)$", line)
        if li:
            if key is None or not isinstance(fm.get(key), list):
                raise FrontMatterError(f"line {n}: list item outside a list")
            fm[key].append(unquote(li.group(1)))
            continue
        kv = re.match(r"^([A-Za-z_][\w-]*):(?:\s+(.*))?$", line)
        if not kv:
            raise FrontMatterError(f"line {n}: cannot parse {line[:60]!r}")
        key, val = kv.group(1), (kv.group(2) or "").strip()
        if key in fm:
            raise FrontMatterError(f"line {n}: duplicate key {key!r}")
        if val.startswith("[") and val.endswith("]"):
            fm[key] = [unquote(x) for x in val[1:-1].split(",") if x.strip()]
        elif val == "":
            fm[key] = []
        else:
            fm[key] = unquote(val)
    return fm


def split_front_matter(text):
    """(front matter dict or None, raw front matter or None, body, body start line number)."""
    m = FRONT.match(text)
    if not m:
        return None, None, text, 1
    return parse_yaml(m.group(1)), m.group(1), text[m.end():], text[:m.end()].count("\n") + 1


def iter_lines(body, first_line=1):
    """Yield (line_no, line, in_fence, fence_info); fence_info is the info string on an opening fence."""
    fence = None
    for n, line in enumerate(body.split("\n"), first_line):
        m = FENCE.match(line)
        if fence is None and m:
            fence = (m.group(2)[0], len(m.group(2)))
            yield n, line, True, m.group(3).strip()
            continue
        if fence is not None:
            if m and m.group(2)[0] == fence[0] and len(m.group(2)) >= fence[1] and not m.group(3).strip():
                fence = None
            yield n, line, True, None
            continue
        yield n, line, False, None


def strip_inline_code(line):
    return INLINE_CODE.sub(lambda m: " " * len(m.group(0)), line)


def github_slug(text, seen=None):
    """GitHub's heading anchor: lowercase, punctuation removed (except - and _), spaces become hyphens."""
    t = re.sub(r"<[^>]+>", "", text)
    t = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = t.replace("`", "").strip().lower()
    t = re.sub(r"[^\w\- ]", "", t, flags=re.U)
    t = t.replace(" ", "-")
    if seen is not None:
        base, i = t, 1
        while t in seen:
            t = f"{base}-{i}"
            i += 1
        seen.add(t)
    return t


def page_key(rel):
    """docs-relative file to manifest key: write/create-a-post, write/publish (README), index (home)."""
    if rel == "README.md":
        return "index"
    if os.path.basename(rel) == "README.md":
        return os.path.dirname(rel)
    return rel[:-3]


def live_path(rel):
    key = page_key(rel)
    return "" if key == "index" else key + "/"
