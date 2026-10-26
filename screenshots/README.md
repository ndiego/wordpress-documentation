# Documentation screenshots

The screenshots in `docs/assets/screenshots/` are rendered, not taken by hand. A YAML file per article says what
to show; the [`@wp-docs-toolkit/screenshots`](https://www.npmjs.com/package/@wp-docs-toolkit/screenshots) engine
boots WordPress in [Playground](https://wordpress.github.io/wordpress-playground/) (pinned WordPress and PHP, a
demo site), drives the interface with Playwright and writes WebP images plus a `manifest.json`. When a WordPress
release changes the interface, re-render and review the differences instead of retaking every image.

This directory is the project: `shots.config.js`, the specs in `shots/`, and `package.json`, which pins the
engine at an exact npm version. The engine's own documentation covers everything that is not specific to this
repository: the [README](https://www.npmjs.com/package/@wp-docs-toolkit/screenshots) (commands, spec format,
scenes, steps, capture targets, annotations) and `node_modules/@wp-docs-toolkit/screenshots/ARCHITECTURE.md`.
House style for framing and annotation: [style/SCREENSHOTS.md](https://github.com/ndiego/wp-docs-toolkit/blob/trunk/style/SCREENSHOTS.md)
in the toolkit.

## Setup

Node 22.19 to 25 (24 recommended), about 1 GB of disk. No Docker, database or local WordPress is needed for a
preview render.

```sh
cd screenshots
npm install
npx playwright install chromium   # once per machine
npx wp-screenshots doctor         # checks Node, the blueprint, Chromium, the port and the specs
```

## Render, lint, check

Run these from `screenshots/`.

```sh
npx wp-screenshots lint                          # validate specs, cross-check image references in docs/ (no browser)
npx wp-screenshots run                           # render every shot
npx wp-screenshots run --article create-a-post   # one article's shots
npx wp-screenshots preview --width 1400          # PNG copies in .wp-screenshots/preview/ to look at
npx wp-screenshots check                         # render to a staging dir, diff against committed images, HTML report
npx wp-screenshots update                        # accept what the last check staged
npx wp-screenshots snippet --article create-a-post   # Markdown image lines with the spec's alt text
```

`run` writes an image only when its pixels changed, so a repeat run against the same WordPress leaves git clean.
A failed shot saves its page state (screenshot, HTML, console log) under `.wp-screenshots/failures/`.

### Local renders are previews

Fonts rasterise differently on macOS and Linux, so an image rendered on a laptop is a preview. The canonical
render runs inside the pinned Playwright Docker image (`dockerImage` in `shots.config.js`):

```sh
npx wp-screenshots check --docker   # needs Docker Desktop
npx wp-screenshots update
```

The manifest marks each image `canonical: true` or `false`. **The images committed now are local macOS previews**
(`canonical: false`), which is fine for this proof of concept. Before they are relied on, re-render them with
`check --docker` (or a CI job using the same image) and `update`. Never follow `update` with a plain `run`: that
would overwrite canonical images with previews.

## The demo site

There is no blueprint in this repository. `shots.config.js` points at the toolkit's bundled demo site,
[`@wp-docs-toolkit/demo-site`](https://www.npmjs.com/package/@wp-docs-toolkit/demo-site), installed with the engine:
WordPress 7.1.3 on PHP 8.3, the Ipsum theme, and a placeholder site called "Saltmarsh" (a slow-travel journal) with
posts, pages, photos, three users, a menu and one showcase post per block (`block-image`, `block-gallery`,
`block-table`). A small mu-plugin hides admin notices and the Dashboard Welcome panel, blocks outbound HTTP and
fixes dates, so screens look the same on every run. You log in as `admin` / `password`.

Specs refer to its content by slug: `{{media.landscape-1}}`, `{{post.post-long}}`, `{{page.about}}`. The slugs
that are guaranteed to exist are listed in `node_modules/@wp-docs-toolkit/demo-site/README.md`. If this project
ever needs content the demo site does not have, create it per shot with `setup` (see the engine README), or copy
the demo site into `blueprint/` here and point `blueprint` in `shots.config.js` at the copy.

## Add a shot

1. Open (or create) `shots/<article>.yaml`. `article` is the output folder; images land at
   `docs/assets/screenshots/<article>/<id>.webp`. One file per article.
2. Start from a preset where one fits (`npx wp-screenshots presets` lists them): `admin-screen` with `screen`,
   `post-editor` (omit `post` for a new post), `site-editor` with `view`, `front-end`, `block-canvas`,
   `block-toolbar`, `block-settings`. Otherwise write a `scene` and `steps` by hand
   (`npx wp-screenshots vocab` lists scenes, verbs and capture targets).
3. Write `alt` as a sentence that says what the image shows. The spec is the source of truth for alt text;
   `npx wp-screenshots lint --fix` copies it into the Markdown.
4. Frame it: `wide` for full screens (the presets do this), a tight `target` with `pad` or a `card` for a panel
   or a control. At most one annotation per image, and only when the text refers to it.
5. `npx wp-screenshots lint`, then `run --article <slug>`, then `preview --article <slug> --width 1400` and look
   at the image: nothing cut off, no stray popover or block toolbar, the right thing on screen, text legible.
6. Reference it from the page with `snippet`, and run `lint` again so the reference and alt text are checked.

To find the accessible name of a button or field for a step, `npx wp-screenshots dev --article <slug> --shot <id>`
opens a visible browser paused in the Playwright Inspector; its "Pick locator" tool shows the role and name.

## Updating at a WordPress release

1. Bump `@wp-docs-toolkit/screenshots` in `package.json` to a version whose demo site pins the new WordPress, and
   `wordpress.version` in `shots.config.js`. Keep `dockerImage` at the engine's Playwright version.
2. `npx wp-screenshots check --docker` and open `.wp-screenshots/report/index.html`.
3. Review each before/after pair. A changed image is a prompt to re-read the page around it, not only to accept
   the pixels.
4. `npx wp-screenshots update`, commit, pull request.

## Layout

```
screenshots/
  package.json        pins @wp-docs-toolkit/screenshots
  shots.config.js     paths, demo-site blueprint, pinned versions, output format, Docker image
  shots/              one YAML spec per article
  .wp-screenshots/    logs, previews, failures, check staging, reports (git-ignored)
../docs/assets/screenshots/
  <article>/<id>.webp the rendered images
  manifest.json       per image: alt text, versions, hashes, canonical flag
```
