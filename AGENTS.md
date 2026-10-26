# Working in this repository

This repository holds the WordPress user documentation as Markdown. A WordPress site imports it (see
[wordpress-documentation-site](https://github.com/ndiego/wordpress-documentation-site)); nothing is edited on the
site. Every change is a pull request here. This file is for people and agents alike.

Read first: [STRUCTURE.md](STRUCTURE.md) (what goes where and why), [conventions/markdown.md](conventions/markdown.md)
(the Markdown flavor), [conventions/front-matter.md](conventions/front-matter.md) (the fields),
[conventions/style.md](conventions/style.md) (the words).

## The one rule

**The folder tree is the structure.** A folder is a group, its `README.md` is the group's page, every other `.md`
file is a page, and `order` in front matter sorts siblings. There is no list to keep in sync: `manifest.json` is
generated from the tree and committed by CI. Never edit `manifest.json` by hand.

## Fix a page

1. Edit the file under `docs/`. Keep the front matter rules; keep the first line `# <title>`.
2. Check the claim against WordPress itself (a named version, in Playground, Studio or a local site), not against
   other documentation. Say which version in the pull request.
3. Run the checks:

   ```sh
   python3 -I scripts/validate.py          # front matter, links, images, Markdown rules
   python3 -I scripts/build-manifest.py    # rewrites manifest.json (CI fails if it is stale)
   ```

4. Open the pull request. Say what you checked and against which WordPress version. If an agent drafted the change,
   say so in the body, and name the person responsible. No AI co-author trailers (WordPress AI guidelines).

## Add a page

1. Decide the type (`tutorial`, `guide`, `concept`, `reference`) and the folder from STRUCTURE.md. If the page does
   not fit anywhere, that is a structure question: open an issue first.
2. Create the file with the front matter from `conventions/front-matter.md`. Give it an `order`. A new group is a
   folder with a `README.md`.
3. Link to it from the pages that should lead there (the group README at least).
4. Validate, build the manifest, open the pull request.

## Move or rename a page

1. Move the file (`git mv`). Add the old site path to `redirect_from` on the page (root-relative, trailing slash,
   for example `/docs/write/old-name/`). If the page must keep its post on the site, set `id` to its old path first.
2. Fix relative links from other pages (`validate.py` lists the broken ones).
3. Validate, build, pull request.

## Screenshots

Screenshots are rendered by the [wp-docs-toolkit](https://github.com/ndiego/wp-docs-toolkit) engine from YAML
specs in `screenshots/`, against a pinned WordPress in Playground, so a release re-renders them instead of
someone retaking them. See `screenshots/README.md`. Add a screenshot only where the words cannot carry the step;
one annotated image beats three plain ones.

## Placeholders

A page whose feature does not exist yet carries `status: placeholder`, a body that is an outline (headings and
one line each), and no claims written as fact. The site shows a banner. Turn a placeholder into a page by removing
the field and writing the content.

## What the site does with a merge

On push to `trunk`, CI validates, rebuilds `manifest.json`, and notifies the site, which pulls the manifest and
every changed file within a minute. Each page on the site links back to its file here (Edit on GitHub, Report a
problem) and serves its Markdown at the page URL plus `.md`.
