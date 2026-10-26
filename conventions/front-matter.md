# Front matter

Every page starts with YAML front matter, then a blank line, then `# <title>` as the first body line. The folder
tree is the structure; front matter carries what the tree cannot say.

```yaml
---
title: Create a post
description: Write your first post in the editor, add an image, and publish it.
type: tutorial
order: 20
redirect_from:
  - /documentation/article/write-posts-block-editor/
---

# Create a post
```

| Field | Type | Required | Meaning |
|---|---|---|---|
| `title` | string | yes | The page title, sentence case. The first body line is `# ` + this, exactly. Product names keep their capitals (Site Editor, Block Directory). |
| `description` | string, one line | yes | One or two sentences for search results, cards and the lede under the title. No em-dashes. Under 200 characters. |
| `type` | `tutorial`, `guide`, `concept`, `reference` | yes | What kind of page it is (see STRUCTURE.md "Principles"). Shown on the page. |
| `order` | integer | no | Position among its siblings in the folder; lower first. Pages without `order` follow the ordered ones, alphabetically by title. Use steps of 10. A `README.md` does not need one (it is the folder). |
| `slug` | string | no | The post slug on the site. Defaults to the file name (for `README.md`, the folder name). Slugs must be unique across the whole tree; block pages use `<name>-block` to keep their HelpHub slug. The URL does not come from the slug; it comes from the path. |
| `id` | string | no | Stable page id the importer matches posts by. Defaults to the path (`write/create-a-post`). Set it only when a page moves and must keep its post (its comments, its media). |
| `status` | `placeholder`, `draft` | no | `placeholder`: the page describes something that is planned; it renders with a banner and its body is an outline. `draft`: content is being written; also a banner. Absent means published. |
| `redirect_from` | list of strings | no | Old WordPress.org paths (root-relative, with a trailing slash) that should 301 here. Every old path appears on exactly one page. |
| `applies_to` | list of strings | no | Reference ids the page explains, such as block names (`core/image`). Reserved for the unified site; optional here. |
| `updated` | `YYYY-MM-DD` | no | When the content was last checked against WordPress. The site shows the import date otherwise. |

Rules `scripts/validate.py` enforces:

- `title`, `description` and `type` present and non-empty; `type` one of the four.
- The first body line is `# ` + `title`.
- One H1 per page; headings do not skip levels.
- Slugs unique across the tree; `redirect_from` paths unique across the tree and never equal to a live path.
- Every relative link points at a file that exists; every relative image exists.
- No em-dashes in prose; no raw HTML other than `<kbd>`, `<details>`, `<summary>`, `<sub>`, `<sup>` and comments.
- GitHub alerts use only NOTE, TIP, IMPORTANT, WARNING, CAUTION.
- UTF-8, LF, no byte order mark.
