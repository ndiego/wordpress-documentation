---
title: Use this documentation with an AI assistant
description: Give an AI assistant accurate WordPress answers by pointing it at this documentation as Markdown, through page URLs, llms.txt or the JSON index.
type: guide
order: 10
---

# Use this documentation with an AI assistant

After reading this page you can give an AI assistant, such as ChatGPT or Claude, or an agent you run yourself, the exact pages of this documentation it needs, in a format it reads well.

Assistants answer better from the current page than from memory. Every page here is available as plain Markdown, and the site publishes indexes that list every page, so an assistant can find and read what it needs.

> [!NOTE]
> The examples on this page use `https://docs.example.org` as a placeholder for the address of this documentation site. Replace it with the address in your browser.

## From a page: copy it or open it in an assistant

At the top right of every page is a **Copy page** button.

- **Copy page** copies the whole page as Markdown. Paste it into any assistant, together with your question.
- The arrow next to it opens a menu:
  - **View as Markdown** opens the page's Markdown in the browser.
  - **Open in ChatGPT** and **Open in Claude** start a new conversation in that assistant, with a prompt that asks it to read this page and help you with it.

## Point an assistant at a page

Every page has a Markdown version at the same address with `.md` at the end. For example, the page [Create a post](../write/create-a-post.md):

```text
https://docs.example.org/docs/write/create-a-post/
```

is also available as:

```text
https://docs.example.org/docs/write/create-a-post.md
```

Assistants that can browse the web can read it directly. Name the pages in your request:

```text
Read https://docs.example.org/docs/write/create-a-post.md and
https://docs.example.org/docs/write/publish/post-status.md, then walk me through
scheduling my first post for Monday at 9 am.
```

The Markdown version has a short block at the top with the page's title, description, type and address, and every link in it is a full URL, so the assistant can follow links to related pages.

Two other ways to ask for the same Markdown, for tools that cannot change the URL:

- Add `?output_format=md` to the page address: `https://docs.example.org/docs/write/create-a-post/?output_format=md`.
- Request the page address with the header `Accept: text/markdown`.

Each page also announces its Markdown version in its HTML head, with a `link` element whose `rel` is `alternate` and whose `type` is `text/markdown`, for tools that look for it.

## Give an assistant the whole documentation

Three files describe all of the documentation at once:

- **`/llms.txt`** is a short index in the [llms.txt](https://llmstxt.org/) format: a summary, then one line per page with its title, its Markdown URL and its description, grouped by section. Give it to an assistant that needs to find the right page.
- **`/llms-full.txt`** is every page's Markdown in one file, in the order of the sidebar. It is large; use it with tools that can take a lot of text, or to build your own search index.
- **`/docs/index.json`** lists every page as JSON, with its title, path, URL, Markdown URL, section, type, status, description, parent, order, source file, and the date it was last updated. Use it in scripts and agents.

Pages marked as placeholders have `"status": "placeholder"` in the index, and their first paragraph says so. They describe planned work, so an agent should not treat them as instructions.

## Fetch pages from the command line

The same URLs work with any HTTP client. For example, with `curl`:

```bash
# One page as Markdown
curl https://docs.example.org/docs/write/create-a-post.md

# The same page, asking for Markdown with a header
curl -H "Accept: text/markdown" https://docs.example.org/docs/write/create-a-post/

# The index, and the title and Markdown URL of every page
curl -s https://docs.example.org/llms.txt
curl -s https://docs.example.org/docs/index.json | jq -r '.pages[] | "\(.title)\t\(.md_url)"'
```

## Tips for better answers

- **Give the page, not the topic.** "Read this page and..." works better than "How do I...", because the assistant answers from the text you gave it.
- **Say which WordPress you use.** Mention the version (shown in **Dashboard > Updates**) and whether you use a block theme or a classic theme.
- **Ask for the source.** Ask the assistant to name the page each step comes from, so you can check it.
- **Report problems with the page, not the assistant.** If the documentation is wrong, use **Report a problem** at the bottom of the page.

## The source on GitHub

Every page is a Markdown file in a public GitHub repository, and every page links to its file with **Edit on GitHub**. You or your agent can read the files there too, and propose corrections with a pull request.
