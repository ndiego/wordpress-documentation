# Style

Short rules for the words. The Markdown rules are in [markdown.md](markdown.md).

- **WordPress.org**, capitalized, in prose. URLs, subdomains and code stay lowercase:
  "Report it on WordPress.org" but `https://wordpress.org/documentation/`.
- **WordPress**, with a capital P, always.
- **Sentence case** for titles and headings: "Set up a development environment".
  Product and feature names keep their capitals: "Site Editor", "Block Editor Handbook", "Font Library".
- **One H1 per page**, the page title, on the first line after the front matter.
- **No em-dashes** in prose (validate fails on them). Use a comma, a colon, parentheses or two sentences.
- **Second person, present tense, active voice**: "Select **Publish**", not "The Publish button should be clicked".
- UI labels in **bold**, exactly as the screen shows them. Menu paths with `>`: **Settings > Reading**.
- Code, file names, functions, hooks and keys in `backticks`: `functions.php`, `register_block_type()`, `settings.color`.
- Write out "for example" and "that is"; avoid "e.g." and "i.e.".
- Say which WordPress version a behavior needs when it is recent: "WordPress 6.5 and later".

## Links

- Link text describes the destination: "[Theme structure](../themes/theme-structure/README.md)", not "click here".
- Link to other docs pages with relative paths to their Markdown files ([markdown.md](markdown.md#links)).
- Link a function, hook or class to the Code Reference on its first mention:
  [`wp_enqueue_script()`](https://developer.wordpress.org/reference/functions/wp_enqueue_script/).
- Do not link to the Codex for anything the docs or the Code Reference cover.

## Alt text and media

- Alt text says what an image shows, in a sentence: "The Styles panel with the Typography section open."
- Screenshots show the current WordPress release, with a default theme, at a normal browser width.

## Accuracy

- Check a claim against the code or the running software (a named WordPress or Gutenberg version), not against
  other documentation. Mark anything you could not verify as unverified in the pull request.
