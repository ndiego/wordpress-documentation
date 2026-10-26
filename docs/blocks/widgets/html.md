---
title: Custom HTML
description: "Starting in WordPress 7.0, the Custom HTML block introduces separate editing panels for HTML, CSS, and JavaScript."
type: reference
slug: html-block
redirect_from:
  - /documentation/article/custom-html/
---

# Custom HTML

**Hypertext Markup Language (HTML)**, is language used to describe the semantic content of web pages. This can be added using the custom HTML block. This block allows you to insert your code so you can fine-tune your content.

Starting in WordPress 7.0, the Custom HTML block introduces separate editing panels for HTML, CSS, and JavaScript. The CSS and JavaScript panels are only available to users with the unfiltered_html capability. If a user lacks this capability (for example, a Contributor), WordPress will sanitize the block’s content using the function [wp_kses()](https://developer.wordpress.org/reference/functions/wp_kses/), stripping disallowed tags such as `<script>` and `<iframe>`. In this case, the CSS and JavaScript panels are not shown, and any disallowed markup is removed when the post is saved or updated.

> [!NOTE]
> [Learn more about WordPress user roles and capabilities](../../manage/users/roles-and-capabilities.md)

[Watch the video](https://wordpress.org/documentation/files/2019/03/html-block-7-0.mp4)

## Add a Custom HTML block

In order to add a custom HTML block, click on the **Block Inserter** icon.

You can also type `/html` and hit enter in a new paragraph block to add one quickly.

![Adding a block with a slash html command](https://wordpress.org/documentation/files/2019/03/Screenshot-2026-05-20-at-10.56.23-AM.png)

> [!NOTE]
> [Detailed instructions on adding blocks](../../write/blocks/add-a-block.md)

## Editing the block

Once you add the block, click on the Edit HTML button to open the editing modal.

![Custom HTML block empty state showing an Edit HTML button](https://wordpress.org/documentation/files/2019/03/html-editing-block.png)

Enter HTML code and see the preview of your output to the right of the code editor. You can expand the modal to fullscreen the Enable/disable fullscreen button on the top right of the modal. When you are done entering code, press the Update button.

![Custom HTML block edit state showing the HTML code pane on the left and HTML output preview on the right](https://wordpress.org/documentation/files/2019/03/html-edit-modal.png)

## Block toolbar

The Custom HTML block has the following options on the block toolbar:

![Custom HTML block toolbar](https://wordpress.org/documentation/files/2019/03/html-block-toolbar.png)

### Block moving tools

The block-moving tools allow you to move the block in the editor. Use the six dots icon to drag and drop the block and place it anywhere on the page. Alternatively, click on the up and down arrows to move the block up or down.

![Custom HTML block toolbar with block moving tools highlighted](https://wordpress.org/documentation/files/2019/03/html-move-tools.png)

> [!NOTE]
> [Get more information about moving a block within the editor](../../write/blocks/move-blocks.md)

### Edit Code button

Press this button to make changes to your Custom HTML block code.

### More options

These controls give you the option to copy, duplicate, or rename your block.

> [!NOTE]
> [Read about these and other settings](../../write/blocks/more-options.md)

## Block settings

While most blocks have specific options in the editor sidebar in addition to the options found in the block toolbar, the HTML block does not have extra options.
