---
title: How WordPress processes post content
description: WordPress processes text entered in the Write Post Screen multiple times before the text is finally displayed on a web page within your WordPress blog.
type: reference
order: 40
redirect_from:
  - /documentation/article/how-wordpress-processes-post-content/
---

# How WordPress processes post content

WordPress processes text entered in the [Write Post Screen](../../manage/dashboard/README.md#add-new-post) multiple times before the text is finally displayed on a web page within your WordPress blog. The processing of the text filters out the unwanted code and conforms the text to a form that the browser can interpret. Without attention to detail and familiarity with WordPress’s post content filtering, this can cause unwanted changes.

The majority of the conversion and filters are found in the [`wp-includes/formatting.php`](https://core.trac.wordpress.org/browser/tags/5.1.0/src/wp-includes/formatting.php#L0) file.

Some typical problems some users have with these filtering and processing functions are:

1.  Empty paragraphs, closing span tags, and line break (BR) elements are removed upon saving.
2.  Classes are removed from elements.
3.  DIV elements are converted to P elements.
4.  Javascripts and code are converted to displayable code rather than actionable code. See [Using Javascript](https://codex.wordpress.org/Using_Javascript) for information on how to incorporate Javascript into a blog post.

The following is step-by-step list of how WordPress processes post content text before the final version is displayed.

## Visual editor

Not all WordPress bloggers use Visual Editor, but if you do, it will change various codes upon saving an entry to prepare it for publishing.

## wpautop() WordPress function

[`wpautop()`](https://codex.wordpress.org/Function_Reference/wpautop) is a core WordPress [function](https://developer.wordpress.org/reference/) that automatically processes, fixes, and modifies the text of a post.

It puts in line breaks, paragraph tags, opens and closes tags that aren’t opened and closed, and cleans up duplicate HTML tags.

## Texturize

Texturize ([wptexturize()](https://codex.wordpress.org/Function_Reference/wptexturize)) is a text filter enabled by default that modifies posted text or comments to present a more readable and visually attractive output.

While it creates aesthetically pleasant text, it might create difficulties when posting code examples in a programming language. In such situations modification of the text is not desirable because it might create syntactically incorrect code.

A few examples include:

```text
"quoted text" becomes “quoted text”
'quoted text' becomes ‘quoted text’
          --- becomes —
           -- becomes –
          ... becomes …
          (c) becomes ©
          (r) becomes ®
         (tm) becomes ™
           '' becomes ”
           `` becomes “
  president's becomes president’s
  presidents' becomes presidents’
          12' becomes 12′
          12" becomes 12″
          2x4 becomes 2×4
```

## Convert smilies

The `convert_smilies()` function converts combinations of characters into [smilies or emoticons](smilies.md) within the post, page, and comment text. For example, if smilies are enabled, WordPress will recognize “:” and “D” (:D) and turn it into a smiling face ( 😀 ).

The key to making smilies work is to put a space before and after the keystroke combination. If placed up against the text, it will not convert.

If conversion of smilies is not desired, turn it off through the **Settings > Writing** panel.

## Convert characters

The `formatting.php` code file contains numerous functions which help publish character entities, accents, and non-English characters to a form recognizable by the web browser.

Generally, these work excellently, however, your browser may not recognize various language characters unless that language is activated in your web browser. See your browser’s documentation for more information on adding language character recognition to your browser.

## Methods to prevent processing

There are a variety of Plugins to change the filtering process WordPress uses by default. It is highly recommended that you do not change the core programming but use WordPress Plugins to change all or some of the content processing. See the [WordPress Plugins Directory](https://wordpress.org/plugins/) for various Plugins that change the post content filtering process.
