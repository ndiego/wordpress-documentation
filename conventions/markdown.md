# Markdown flavor

Every page in this repository is written in this flavor. It is
GitHub-flavored Markdown as GitHub renders it, plus YAML front matter. A page should look the same on
GitHub and on WordPress.org, so nothing here needs a custom renderer: if GitHub cannot render it, it is not
allowed. `scripts/validate.py` enforces the rules marked **(checked)**.

The importer is the WordPress.org `wporg-markdown` plugin (Jetpack's Markdown Extra parser, then kses).
Where its behavior is the reason for a rule, the rule says so.

## File layout

- One file per page, under `docs/<section>/`, named from the page slug: `docs/write/create-a-post.md`.
- A page with child pages is a folder with a `README.md` (GitHub shows it when you open the folder):
  `docs/write/blocks/README.md`, and the children sit next to it. The README is the folder's landing page.
- Each section has a landing page at `docs/<section>/README.md`.
- Every `.md` file under `docs/` is a page. There is no separate list of pages: the tree is the structure
  (STRUCTURE.md) and `scripts/build-manifest.py` derives `manifest.json` from it.
- Images live next to the pages in an `images/` folder, or under `docs/assets/screenshots/<page>/` when the
  screenshot engine renders them (see `screenshots/README.md`).
- UTF-8, LF line endings, no byte order mark **(checked)**. A BOM makes the importer render the front matter.

## Front matter and title

```markdown
---
title: Embeds
description: Add content from YouTube, X, Spotify and other sites with the Embed block.
type: reference
order: 90
redirect_from:
  - /documentation/article/embeds/
---

# Embeds

The first paragraph.
```

- The fields and their types are in [front-matter.md](front-matter.md).
- Never put `---` inside a front matter value **(checked)**. The importer ends the front matter at the first `---`
  it finds, wherever it is.
- The first line after the front matter is `# ` followed by the title, exactly as in `title` **(checked)**. The
  importer takes the post title from this line. Keep it plain text: no links, code or HTML.
- One H1 per page **(checked)**. Sections start at `##`.
- The first paragraph after the H1 is the lede. The site shows `description` under the title, so do not repeat it
  word for word; open with what the reader will be able to do.

## Headings

- Sentence case: "Add a block", not "Add A Block". See [style.md](style.md).
- Do not skip levels (`##` then `####`).
- Anchors follow GitHub's algorithm: lowercase, punctuation removed, spaces become hyphens.
  `## Fonts in a theme` is `#fonts-in-a-theme`. Link to headings with that form. `scripts/check-links.py` reports
  anchors that do not exist.

## Paragraphs and line breaks

- Separate paragraphs with a blank line. Hard-wrapped lines are fine.
- No `<br>` **(checked: raw HTML)**. Start a new paragraph instead. Inside a list item, indent the new paragraph
  to the item's text:

  ```markdown
  -   **Logo**: the site logo.

      Select Logo opens the Media Library.
  ```

## Callouts

Use GitHub alerts, and only these five types **(checked)**:

```markdown
> [!NOTE]
> Useful information that users should know, even when skimming.

> [!TIP]
> Optional advice that helps people do something better.

> [!IMPORTANT]
> Information people need to succeed.

> [!WARNING]
> Something that needs immediate attention to avoid a problem.

> [!CAUTION]
> The risk of losing data or breaking a site.
```

They render like this on GitHub:

> [!NOTE]
> Useful information that users should know, even when skimming.

Ordinary text between them.

> [!WARNING]
> Something that needs immediate attention to avoid a problem.

Rules:

- The type line `> [!TYPE]` is alone on its line, in capitals.
- Put a paragraph between two alerts or between an alert and a quote. The importer merges blockquotes that are
  separated only by a blank line (validate warns).
- The old notations become alerts: HelpHub notice paragraphs, `[info]` (NOTE), `[tip]` (TIP), `[alert]` (WARNING),
  `[warning]` (CAUTION), and any `<div class="callout">`.

## Code

- Fence code with three backticks and a language **(checked)**: `php`, `js`, `jsx`, `css`, `html`, `json`,
  `bash`, `text`, ...

  ````markdown
  ```php
  add_action( 'init', 'myplugin_register_blocks' );
  ```
  ````

- Never write a literal `<code>` tag inside a fence. The importer's parser un-escapes it and injects real HTML
  into the page.
- Inline code uses backticks: `` `wp_enqueue_script()` ``.
- Block markup examples (`<!-- wp:paragraph -->`) go inside a fence only. Outside a fence it is an error
  **(checked)**: one block comment makes WordPress skip `wpautop` and every paragraph on the page loses its `<p>`.

## Lists and tables

- `-` for bullets, `1.` for numbered steps. Indent nested lists and continuation paragraphs to the text of the
  parent item.
- Tables are GFM pipe tables with a header row:

  ```markdown
  | Format | Example |
  |---|---|
  | `d` | 01 to 31 |
  ```

- No HTML tables. Definition lists (`term` then `:   definition`) are Markdown Extra, which GitHub does not
  render; write `- **term**: definition`.

## Links

| To | Write | Example |
|---|---|---|
| Another page here | A relative path to its Markdown file **(checked: the file exists and is a page)** | `[Embeds](../blocks/embeds.md)` |
| A heading on another page | The relative path plus a GitHub anchor | `[Fonts in a theme](../design/fonts.md#fonts-in-a-theme)` |
| A heading on this page | The anchor alone | `[Providers](#providers)` |
| Anything else | The full https URL | `[Code Reference](https://developer.wordpress.org/reference/)` |

- The importer rewrites relative `.md` links to the page's URL on the site, so the same link works on GitHub and
  on the site. A link to a folder's `README.md` becomes the folder's URL.
- Never link with a root-relative path such as `/docs/blocks/` **(checked)**. It works on neither GitHub nor a
  local site at another path.
- Never link to this repository with a github.com URL; use the relative path **(checked)**.
- Link text says where the link goes. Not "click here".

## Images

New images live in the repository, next to the page that uses them, in an `images/` folder:

```text
docs/design/site-editor/
  fonts.md
  images/
    fonts-library-modal.png
```

```markdown
![The Font Library modal with the Install Fonts tab open.](images/fonts-library-modal.png)
```

- Name the file `<page id>-<what it shows>.<ext>`, lowercase with hyphens. PNG for screenshots, JPEG for photos,
  SVG for diagrams. Keep each file under 500 KB.
- Always write alt text that says what the image shows (validate warns when it is empty). The alt text is not a
  caption; if a caption is needed, write it as an ordinary paragraph after the image.
- A relative image path must point at a file that exists **(checked)**. The importer sideloads repository images
  into the media library on import.
- Ported pages still use the remote URLs of the images WordPress.org hosts today
  (`https://wordpress.org/documentation/files/...`). They move into the repository (ideally as a screenshot
  spec the engine can re-render) when a page is next edited; do not add new remote images.
- No raw `<img>` **(checked: raw HTML)**. Width attributes are not supported; crop the image instead.

## Video

No iframes and no `<video>` **(checked)**. Link to the video:

```markdown
[Watch the video: adding a Cover block](https://videopress.com/v/abc123)
```

A bare video URL alone on its own line also becomes an embedded player on WordPress.org (oEmbed), but shows as a
plain link on GitHub; prefer the link form.

## Raw HTML

Not allowed, except these, which GitHub and the importer both handle **(checked)**:

| Element | Use for |
|---|---|
| `<kbd>` | Keys: <kbd>Ctrl</kbd> + <kbd>S</kbd> |
| `<details>` and `<summary>` | A collapsed section; leave a blank line after `<summary>` so Markdown inside renders |
| `<sub>`, `<sup>` | Subscript and superscript |
| `<!-- ... -->` | Comments for editors, such as `<!-- TODO: draft -->`. They ship in the page source, so keep them short |

No `<div>`, `<span>`, `<br>`, `<img>`, `<video>`, `<table>`, inline `style`, `<script>`, `<style>` or `<iframe>`.
The importer's kses strips `<script>` and `<style>` tags but leaves their text on the page.

## Not supported

| Feature | Why | Instead |
|---|---|---|
| Footnotes `[^1]` **(checked)** | kses breaks the `#fn:` links | Put the note in the sentence or a NOTE alert |
| Block markup `<!-- wp: -->` outside code **(checked)** | Disables `wpautop` for the whole page | A fenced `html` example |
| Shortcodes like `[gallery]` outside code | They run on WordPress.org | Put them in a fence |
| `~~strikethrough~~` | Untested in the importer | Rewrite the sentence |
| Heading ids `{#id}` | GitHub shows them literally | Link with the GitHub anchor |
| Setext headings (`Title` + `===`) | The importer only takes `# Title` as the title | ATX headings |
