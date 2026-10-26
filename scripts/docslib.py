"""Shared helpers for validate.py, build-manifest.py and check-links.py. Stdlib only."""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DOCS = os.path.join(REPO, "docs")
REPO_URL = "https://github.com/ndiego/wordpress-documentation"
SOURCE_BASE = f"{REPO_URL}/blob/trunk/docs/"

FRONT = re.compile(r"\A---\n(?:(.*?)\n)?---[ \t]*(?:\n|\Z)", re.S)
FENCE = re.compile(r"^(\s*)(`{3,}|~{3,})(.*)$")
QUOTE = re.compile(r"^(?:[ ]{0,3}>[ ]?)+")
REF_DEF = re.compile(r"^[ ]{0,3}\[(?!\^)([^\]]+)\]:[ \t]*(<[^>]*>|\S+)")
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


def strip_comment(v):
    """Remove a trailing ` # comment` that is outside quotes (YAML ignores it)."""
    v = v.strip()
    if v[:1] in ('"', "'"):
        q, i = v[0], 1
        while i < len(v):
            if q == '"' and v[i] == "\\":
                i += 2
                continue
            if v[i] == q:
                if q == "'" and v[i + 1:i + 2] == "'":
                    i += 2
                    continue
                rest = v[i + 1:]
                if not rest.strip() or re.match(r"\s+#", rest):
                    return v[:i + 1]
                return v
            i += 1
        return v
    if v.startswith("#"):
        return ""
    return re.sub(r"\s+#.*$", "", v)


def split_flow(inner):
    """Split the inside of a flow list on commas that are outside quotes."""
    out, cur, q = [], "", None
    for ch in inner:
        if q:
            cur += ch
            if ch == q:
                q = None
        elif ch in ('"', "'") and not cur.strip():
            q = ch
            cur += ch
        elif ch == ",":
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return [x for x in out if x.strip()]


def scalar(v):
    v = strip_comment(v)
    if v[:1] not in ('"', "'") and (": " in v or v.endswith(":")):
        raise FrontMatterError(f"unquoted value {v[:40]!r} contains ': '; quote it")
    return unquote(v)


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
            fm[key].append(scalar(li.group(1)))
            continue
        kv = re.match(r"^([A-Za-z_][\w-]*):(?:\s+(.*))?$", line)
        if not kv:
            raise FrontMatterError(f"line {n}: cannot parse {line[:60]!r}")
        key, val = kv.group(1), strip_comment(kv.group(2) or "")
        if key in fm:
            raise FrontMatterError(f"line {n}: duplicate key {key!r}")
        try:
            if val.startswith("[") and val.endswith("]"):
                fm[key] = [scalar(x) for x in split_flow(val[1:-1])]
            elif val == "":
                fm[key] = []
            else:
                fm[key] = scalar(val)
        except FrontMatterError as exc:
            raise FrontMatterError(f"line {n}: {exc}") from None
    return fm


def split_front_matter(text):
    """(front matter dict or None, raw front matter or None, body, body start line number)."""
    m = FRONT.match(text)
    if not m:
        return None, None, text, 1
    raw = m.group(1) or ""
    return parse_yaml(raw), raw, text[m.end():], text[:m.end()].count("\n") + 1


def quote_depth(line):
    q = QUOTE.match(line)
    return (q.group(0).count(">"), line[q.end():]) if q else (0, line)


def iter_lines(body, first_line=1, state=None):
    """Yield (line_no, line, in_fence, fence_info); fence_info is the info string on an opening fence.

    Fences inside blockquotes (`> ```php`) count. When `state` is a dict, state["open_fence"] is set to the line
    number of a fence that is still open at the end of the body (or None).
    """
    fence = None
    for n, line in enumerate(body.split("\n"), first_line):
        depth, inner = quote_depth(line)
        if fence is not None and depth < fence[2]:
            fence = None  # the blockquote that held the fence ended, and the fence with it
        m = FENCE.match(inner)
        if fence is None and m:
            fence = (m.group(2)[0], len(m.group(2)), depth, n)
            yield n, line, True, m.group(3).strip()
            continue
        if fence is not None:
            if m and m.group(2)[0] == fence[0] and len(m.group(2)) >= fence[1] and not m.group(3).strip():
                fence = None
            yield n, line, True, None
            continue
        yield n, line, False, None
    if state is not None:
        state["open_fence"] = fence[3] if fence is not None else None


def iter_links(body, first_line=1):
    """Yield (line_no, bang, label, url) for every inline link and image outside code, including links whose
    text wraps across lines, and for every reference definition (`[label]: url`; bang is "")."""
    para = []

    def flush():
        if not para:
            return
        text = "\n".join(x for _, x in para)
        starts = [n for n, _ in para]
        for mm in LINK.finditer(text):
            n = starts[text.count("\n", 0, mm.start())]
            yield n, mm.group(1), mm.group(2), mm.group(3).strip("<>")
        para.clear()

    for n, line, in_fence, _ in iter_lines(body, first_line):
        if in_fence or not line.strip() or not quote_depth(line)[1].strip():
            yield from flush()
            continue
        bare = strip_inline_code(line)
        d = REF_DEF.match(quote_depth(bare)[1])
        if d:
            yield from flush()
            yield n, "", d.group(1), d.group(2).strip("<>")
            continue
        para.append((n, bare))
    yield from flush()


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
