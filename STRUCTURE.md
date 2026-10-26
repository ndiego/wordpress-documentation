# Structure: the WordPress user documentation, reimagined

Status: design, 2026-10-26. This file is the information architecture of the documentation and the map from the
pages WordPress.org has today to the pages here. The folder tree under `docs/` **is** the structure: a folder is a
group, its `README.md` is the group's landing page, and every other `.md` file is a page. Order inside a folder
comes from the `order` field in front matter. `scripts/build-manifest.py` turns the tree into `manifest.json`,
which the WordPress.org Markdown importer reads.

## Who it is for

Three readers, in this order of priority:

1. **Someone new to WordPress** who has a site (or is about to) and wants to do one thing: publish a post, change
   the look, add a user. They should never have to understand the whole system to finish one task.
2. **Someone who runs a WordPress site** and comes back when something changes: an update, a new feature, a
   problem.
3. **An AI assistant or agent** acting on behalf of either, which needs clean Markdown, stable URLs, an index and
   an honest statement of what WordPress can and cannot do through an agent today.

## Principles

- **Tasks first, screens second.** The old documentation was organized by wp-admin screen ("Settings General
  Screen"). This one is organized by what the reader is trying to do. Screen reference pages still exist, under
  Manage your site, because people search for them.
- **One reading path for beginners.** Get started is a short, ordered path: what WordPress is, where to run it,
  install it, a guided first session, the mental model. Everything else is reachable but not required.
- **Block-first, classic kept.** The main tree describes a current WordPress install: the block editor, a block
  theme, the Site Editor. Pages that apply only to the Classic Editor plugin or classic themes live in Classic
  WordPress, so a new user never meets them by accident and a long-time user can still find them.
- **One page per topic.** Where HelpHub had three pages for one thing (a "screen" page, a "how to" page and a block
  page) the merged page keeps the fullest content and the other URLs redirect to it.
- **Every page has a type.** `tutorial` (follow along, ordered steps, one outcome), `guide` (how to do a task),
  `concept` (how something works), `reference` (look something up). The type is shown on the page and sets the
  template of the writing.
- **AI is a section, honestly labeled.** The WordPress and AI section exists from day one. Pages that describe
  capabilities that are not shipped yet carry `status: placeholder` and render with a banner that says so.

## The tree

Paths are under `docs/`; URLs are the same path under `/docs/` on the site (a `README.md` is its folder's URL).
`[new]` is written fresh for this project, `[rewrite]` starts from an existing page and is rewritten, `[port]` is
the existing page converted and cleaned up (links, front matter, callouts, removed boilerplate), `[placeholder]` is an
outlined page with a banner.

### Home (`docs/README.md`) [new]

The front page content: a one-paragraph welcome and the four doors (Get started, Write and edit, Design your site,
Manage your site), with a strip for WordPress and AI. The site renders the doors as cards from the tree; the README
holds only the prose.

### 1. Get started (`get-started/`)

An ordered path. Read top to bottom.

| Page | File | Type | Source |
|---|---|---|---|
| Get started (landing: the path, 4 lines) | `README.md` | guide | [new] |
| What is WordPress? | `what-is-wordpress.md` | concept | [new], short; uses `what-wordpress-is` for facts |
| WordPress.org and WordPress.com | `wordpress-org-and-wordpress-com.md` | concept | [port] |
| Choose where to run WordPress | `choose-where-to-run-wordpress.md` | guide | [new]: hosting, local (Studio, Local), try in the browser (Playground); uses `hosting-wordpress` |
| Install WordPress | `install-wordpress.md` | guide | [rewrite] from `install-wordpress/README` + `hosting-wordpress`: one-click, manual, local |
| Your first site: a guided tour | `your-first-site.md` | tutorial | [rewrite] of `your-first-site/README` (5,300 words to about 1,500: log in, dashboard, write a post, publish, change the look, next steps) |
| How a WordPress site is put together | `how-wordpress-works.md` | concept | [new]: posts, pages, blocks, themes, templates, plugins, users, media; the mental model with a diagram |
| The WordPress project | `the-wordpress-project.md` | concept | [port] of `what-wordpress-is/README` (history, releases, community), trimmed |
| Where to find help | `where-to-find-help.md` | guide | [port] |
| Glossary | `glossary.md` | reference | [port] of `glossary/README` (`wordpress-semantics` retires into it) |

### 2. Write and edit (`write/`)

Everything that happens in the editor.

| Page | File | Type | Source |
|---|---|---|---|
| Write and edit (landing) | `README.md` | guide | [new] |
| Create a post | `create-a-post.md` | tutorial | [new] |
| Create a page | `create-a-page.md` | guide | [port] of `posts-and-pages/create-pages` |
| **The editor** (group) | `editor/README.md` | concept | [port] of `the-editor/README`; a new 2-paragraph intro |
| Page and post settings sidebar | `editor/settings-sidebar.md` | reference | [port] |
| Preview | `editor/preview.md` | guide | [port] `editor-preview` |
| Notes | `editor/notes.md` | guide | [port] `editor-notes` |
| Preferences | `editor/preferences.md` | reference | [port] `editor-preferences` |
| Distraction free mode | `editor/distraction-free-mode.md` | guide | [port] |
| Keyboard shortcuts | `editor/keyboard-shortcuts.md` | reference | [port] |
| **Working with blocks** (group) | `blocks/README.md` | guide | [port] of `working-with-blocks/work-with-blocks` (the real overview) |
| Add a block | `blocks/add-a-block.md` | guide | [port] `adding-a-block` |
| Move blocks | `blocks/move-blocks.md` | guide | [port] `moving-blocks` |
| List view | `blocks/list-view.md` | guide | [port] |
| More options | `blocks/more-options.md` | reference | [port] |
| Rich text options | `blocks/rich-text-options.md` | reference | [port] |
| Links | `blocks/link-control.md` | guide | [port] |
| Page jumps | `blocks/page-jumps.md` | guide | [port] |
| Block Directory | `blocks/block-directory.md` | guide | [port] |
| Block errors | `blocks/block-error.md` | guide | [port] |
| **Block settings and design tools** (group) | `block-settings/README.md` | reference | [port] + short intro |
| Color, Typography, Dimensions, Border and shadow, Background, Layout, Position, Filters and duotone, Responsive styles, Advanced | `block-settings/<name>.md` | reference | [port] of `block-settings-<name>` |
| **Media** (group) | `media/README.md` | guide | [port] `media-library/README` |
| Add media | `media/add-media.md` | guide | [port] |
| Edit media | `media/edit-media.md` | guide | [port] |
| Image sizes and quality | `media/image-sizes.md` | concept | [port] |
| **Publish** (group) | `publish/README.md` | guide | [new], short: the publish flow, status, visibility, schedule |
| Post status | `publish/post-status.md` | reference | [port] |
| Content visibility | `publish/content-visibility.md` | guide | [port] |
| Password-protected content | `publish/password-protected.md` | guide | [port] `password-protected-posts` |
| Sticky posts | `publish/sticky-posts.md` | guide | [port] |
| Excerpts | `publish/excerpts.md` | guide | [port] |
| Revisions | `publish/revisions.md` | guide | [port] |
| **Organize your content** (group) | `organize/README.md` | concept | [port] + intro |
| Categories | `organize/categories.md` | guide | [port] `categories-screen` |
| Tags | `organize/tags.md` | guide | [port] `tags-screen` |
| Taxonomies | `organize/taxonomies.md` | concept | [port] |
| Post types | `organize/post-types.md` | concept | [port] |
| Custom fields | `organize/custom-fields.md` | guide | [port] `custom-fields/README` |
| Set a static front page | `organize/static-front-page.md` | guide | [port] |
| Create a search page | `organize/search-page.md` | guide | [port] |
| **Comments** (group) | `comments/README.md` | guide | [port] `comments-in-wordpress` as the landing |
| Comments screen | `comments/comments-screen.md` | reference | [port] |
| Comment moderation | `comments/comment-moderation.md` | guide | [port] |
| Comment spam | `comments/comment-spam.md` | guide | [port] |
| Trackbacks and pingbacks | `comments/trackbacks-and-pingbacks.md` | concept | [port] |
| **Formatting** (group) | `formatting/README.md` | reference | [port] + intro |
| Character entities, Emoji, Smilies, How WordPress processes post content | `formatting/<name>.md` | reference | [port] |
| Search engine optimization | `seo.md` | guide | [port] |

### 3. Blocks (`blocks/`)

The block reference: one page per core block, grouped the way the inserter groups them. Landing page [port] of
`all-blocks/all-blocks-overview` with a new intro. Each block page keeps the HelpHub slug (`image-block`) so the
old URL redirects.

| Group | Folder | Pages |
|---|---|---|
| Text | `text/` | paragraph, heading, list (with list-item), quote, code, details, preformatted, pullquote, table, verse (Poetry), footnotes, math, freeform (Classic) |
| Media | `media/` | image, gallery, audio, cover, file, media-text, video, icon, playlist |
| Design | `design/` | buttons, columns, group (with grid, row, stack), accordion, tabs, home-link, more, navigation-link, navigation-submenu, nextpage (Page Break), separator, spacer |
| Widgets | `widgets/` | archives, calendar, categories (Terms List), html, latest-comments, latest-posts, page-list, rss, search, shortcode, social-links, tag-cloud |
| Theme | `theme/` | avatar, breadcrumbs, comments (and its inner blocks), loginout, navigation, post-author-biography, post-author-name, post-comments-form, post-content, post-date, post-excerpt, post-featured-image, post-navigation-link, post-template, post-terms, post-time-to-read, post-title, query, query-pagination, query-title, query-total, read-more, site-logo, site-tagline, site-title, template-part, term-description, terms-query |
| Embeds | `embeds.md` | one page for the Embed block and every provider [port] |

Each group folder has a one-paragraph `README.md`.

### 4. Design your site (`design/`)

| Page | File | Type | Source |
|---|---|---|---|
| Design your site (landing) | `README.md` | guide | [new] |
| **Themes** (group) | `themes/README.md` | guide | [port] `choose-and-install-a-theme/README` |
| Block themes | `themes/block-themes.md` | concept | [port] |
| Themes screen | `themes/themes-screen.md` | reference | [port] |
| Default themes (group, one page per theme Twenty Ten to Twenty Twenty-Five) | `themes/default-themes/README.md`, `twenty-*.md` | reference | [port] |
| **The Site Editor** (group) | `site-editor/README.md` | guide | [port] with a new intro |
| Templates and template parts | `site-editor/templates.md` | concept | [port] `templates/README` |
| Styles | `site-editor/styles.md` | guide | [port] `styles/README` |
| Fonts | `site-editor/fonts.md` | guide | [port] |
| Navigation | `site-editor/navigation.md` | guide | [port] |
| Site icon | `site-editor/site-icon.md` | guide | [port] |
| Command Palette | `site-editor/command-palette.md` | guide | [port] |
| **Patterns** (group) | `patterns/README.md` | concept | [port] `patterns/README` |
| Pattern Directory | `patterns/pattern-directory.md` | guide | [port] |
| Submit a pattern | `patterns/submit-a-pattern.md` | guide | [port] |

### 5. Manage your site (`manage/`)

| Page | File | Type | Source |
|---|---|---|---|
| Manage your site (landing) | `README.md` | guide | [new] |
| **Dashboard and admin screens** (group) | `dashboard/README.md` | reference | [port] `admin-screens/README` |
| Dashboard screen, Posts screen, Pages screen, Tools screen | `dashboard/<name>.md` | reference | [port] |
| **Settings** (group) | `settings/README.md` | reference | [port] + intro |
| General, Writing, Reading, Discussion, Media, Permalinks, Connectors, Date and time format | `settings/<name>.md` | reference | [port] of `settings-<name>` |
| **Users and roles** (group) | `users/README.md` | guide | [port] + intro |
| Roles and capabilities, Add a user, Users screen, Your profile, Gravatars | `users/<name>.md` | guide/reference | [port] |
| Plugins | `plugins.md` | guide | [port] `manage-plugins` |
| **Updates** (group) | `updates/README.md` | guide | [port] |
| Auto-updates, Site maintenance, Update PHP | `updates/<name>.md` | guide | [port] |
| **Security** (group) | `security/README.md` | guide | [new], short |
| Password best practices, My site was hacked | `security/<name>.md` | guide | [port] |
| Privacy | `privacy.md` | guide | [port] |
| **Troubleshooting** (group) | `troubleshooting/README.md` | guide | [port] `site-health/README` (Site Health and troubleshooting) |
| Troubleshooting FAQ, Recovery mode, Changes not showing | `troubleshooting/<name>.md` | guide | [port] |
| wp-config.php for site owners | `wp-config.md` | reference | [port] |

### 6. WordPress and AI (`ai/`)

New. The first two pages describe what exists today; the rest are placeholders with an outline and a banner.

| Page | File | Type | Source |
|---|---|---|---|
| WordPress and AI (landing) | `README.md` | concept | [new]: what this section is, what is real today, what is coming |
| Use this documentation with an AI assistant | `use-the-docs-with-ai.md` | guide | [new], real: every page as Markdown (`.md` URL), `llms.txt`, Copy page, Open in ChatGPT or Claude, the JSON index |
| Connect an AI agent to your site | `connect-an-agent.md` | guide | [placeholder]: application passwords, the REST API, the WordPress MCP adapter and the Abilities API, what to expect |
| Build a site with an agent | `build-a-site-with-an-agent.md` | tutorial | [placeholder] |
| Write and edit with AI | `write-with-ai.md` | guide | [placeholder] |
| Permissions and safety for agents | `agent-permissions-and-safety.md` | concept | [placeholder] |

### 7. Classic WordPress (`classic/`)

[port] of the ten classic pages, unchanged structure: `README.md`, `classic-editor/` (write posts, write code in
posts, audio and video shortcodes), `widgets-menus-customizer/` (Customizer, Widgets screen, block widgets editor,
Menus screen).

## What is retired

These pages exist on WordPress.org today and have no page here; their old URL redirects to the page named.

| Old page | Redirects to |
|---|---|
| `wordpress-semantics` | `get-started/glossary` |
| `get-started-with-wordpress` (the second "first steps" page) | `get-started/your-first-site` |
| `introduction-to-blogging` | `get-started/what-is-wordpress` |
| `posts-and-pages` (landing with no content) | `write/` |
| the `wordpress-versions` pages | not documentation; they stay on WordPress.org |

`redirect_from` on each page records every old WordPress.org URL (the hub already carried them; the port keeps
them and adds the retired ones).

## The map from the hub

`scripts/port.py` carries the mechanical mapping from `wporg-docs/content/<old path>` to `docs/<new path>`. The
rules, so a reader can check them:

- `get-started/*` as in the table above.
- `content/<x>` becomes `write/<x>` with these renames: `the-editor/` to `editor/`, `posts-and-pages/create-pages`
  to `create-a-page`, the publish-related pages to `publish/`, `organize-your-content/` to `organize/` with
  `-screen` dropped from file names, `custom-fields/README` to `organize/custom-fields`, `media-library/` to `media/`.
- `blocks/working-with-blocks/` becomes `write/blocks/` (`work-with-blocks` is the README), `blocks/block-settings/`
  becomes `write/block-settings/` with the `block-settings-` prefix dropped.
- `blocks/all-blocks/blocks-category-<g>/block-<name>` becomes `blocks/<g>/<name>`, keeping sub-folders.
- `design/choose-and-install-a-theme/` becomes `design/themes/`; `design/default-themes/default-theme-<x>` becomes
  `design/themes/default-themes/<x>`; `styles/README`, `templates/README`, `fonts`, `navigation`, `site-editor/*`
  go under `design/site-editor/`; `patterns/` stays `design/patterns/` flattened.
- `administration/` becomes `manage/`: `admin-screens/` to `dashboard/`, `settings/settings-<x>` to `settings/<x>`,
  `users-roles/` to `users/` (`add-new-user` to `add-a-user`), `site-health/` and `performance/` to
  `troubleshooting/`, `manage-plugins` to `plugins`, `privacy/README` to `privacy`, `server-configuration/wp-config-basics`
  to `wp-config`.
- `classic/` unchanged.
