---
title: Content
description: Show the content of a post or page in a template or a Query Loop with the Content block.
type: reference
slug: post-content-block
redirect_from:
  - /documentation/article/post-content-block/
---

# Content

Use the *Content* block to display the contents of a post or page. This block is a child block of the [*Query Loop*](query.md) block and helps to customize the appearance of the query loop. **The option to add this block is only available in [Site Editor](../../design/site-editor/README.md).**

To add a *Content* block, first ensure that you are editing the page or post template.

![A screenshot of the document overview sidebar in the WordPress edit Template screen. The list view tab is active and a content block is highlighted.](https://wordpress.org/documentation/files/2022/03/content-list-view.jpg)

*The list view tab of the document overview*

After block you want to precede Content block, hover to activate the **inline block Inserter** and click to add the *Content* block in the desired location. You may need to type *Content* in the block search dialog to find it.

![A screenshot of the inline block inserter. The search bar of the block inserter contains the text "content". The Content block is available as an option to insert into the page.](https://wordpress.org/documentation/files/2022/03/content-inserter.jpg)

*Adding Content block via the inline block inserter*

You can also type <kbd>/content</kbd> and hit enter in a new paragraph block to add the *Content* block quickly.

![How to add Content block quickly](https://wordpress.org/documentation/files/2022/03/content-slash-inserter.jpg)

*Adding Content via “/” quick-add*

The inner blocks contain an empty paragraph as a template when the Content block doesn’t already have content in it.

![A screenshot of the empty paragraph in inner block when the block doesn't have any other content in it.](https://wordpress.org/documentation/files/2024/03/268028952-efb999ca-1819-4e93-b942-b60993608e31.png)

> [!NOTE]
> [Detailed instructions on adding blocks](../../write/blocks/add-a-block.md)

## Block toolbar

To view the block toolbar, click on the block and the toolbar will be displayed.

Every block comes with unique toolbar icons. These block-specific controls allow you to manipulate the block right in the editor.

The *Content* block shows four buttons in the block toolbar:

-   Transform to
-   Drag icon
-   Move arrows
-   More options

![Content block toolbar](https://wordpress.org/documentation/files/2022/03/Screen-Shot-2022-03-23-at-3.08.55-PM.png)

*Content block toolbar*

**Transform to**

Click on the **Transform** button to convert into Columns, Details, Group, or Excerpt blocks.

-   **Excerpt**: Display only a trimmed version of the post content, commonly used in blog listings or archive templates.
-   **Columns**: Organize your content into multiple columns for a more structured layout.
-   **Details**: Collapse content inside a toggle panel to display it on demand.
-   **Group**: Wrap the block in a container, allowing you to apply background, spacing, and layout styles.

![The transform dropdown on the Content block](https://wordpress.org/documentation/files/2022/03/content-transforms.png)

*Content block transform options*

**Drag icon**

![Drag icon in the Content block](https://wordpress.org/documentation/files/2022/03/02-post-content.png)

*Content block drag icon*

To drag and drop the block to a new location on the page template, click and hold the **drag** icon, then drag the block to the new location. The blue separator line indicates where the block will be placed. Release the left mouse button when you find the new location to place the block.

**Move arrows**

![Move arrows in the Content block](https://wordpress.org/documentation/files/2022/03/01-post-content-1.png)

*Move arrows in the Content block*

The **up and down** arrow icons can be used to move the block up and down on the page.

> [!NOTE]
> [Get more information about moving a block within the editor.](../../write/blocks/move-blocks.md)

### Options

The **Options** button on a block toolbar gives you more features to customize the block. These controls allow you to duplicate, and edit your block as HTML.

> [!NOTE]
> [Read about these and other settings.](../../write/blocks/more-options.md)

## Block settings

In addition to the block toolbar, every block has specific options in the editor sidebar.

*If you do not see the sidebar, click the **settings** icon next to the **Save** button.*

![The block settings icon](https://wordpress.org/documentation/files/2023/04/settings-1.png)

### Typography

This option allows you to set the font, color, size, line height and other typography-related settings for the block.

> [!NOTE]
> [Learn more about typography settings.](../../write/block-settings/typography.md)

### Background

The Background settings allow you to customize the appearance of supported blocks using background images, colors, and gradients.

> [!NOTE]
> For details, refer to the [Background Settings Overview](../../write/block-settings/background.md).

### Layout

The Layout menu under the Settings tab lets you add custom content width to the *Content* block.

When you toggle this option off, the *Content* block inherits the layout width options set by the theme.

![Content width options](https://wordpress.org/documentation/files/2023/04/content-width.png)

*Content width inherited from the layout*

Otherwise, you can customize the content width and justification when it’s toggled on.

![Setting content width for Content block](https://wordpress.org/documentation/files/2023/04/settings-content-width.png)

*Setting the custom Content width*

![Setting Justification for Content block](https://wordpress.org/documentation/files/2023/04/justification-1.png)

*Setting constrained layout justification*

> [!NOTE]
> [This article provides details about layout settings.](../../write/block-settings/layout.md)

### Dimensions

The option to control block spacing and padding is enabled for the block.

> [!NOTE]
> [Learn more about dimension controls.](../../write/block-settings/dimensions.md)

### Border

This option allows you to set a border around the block, including the color, the width, radius, and the style of the border.

> [!NOTE]
> [Learn more about Border & Shadow settings.](../../write/block-settings/border.md)

### Elements

The Elements settings allow you to customize the appearance of links, buttons, headings, and heading levels H1 through H6. You can define a default color for headings (e.g., H1–H6) directly within the block settingsWhen applied, block-level heading color styles will take precedence over global settings.

### Advanced settings

The following Advanced settings options are available: HTML Anchor, Additional CSS Class(es), Additional CSS, HTML Element, and Styles.

> [!NOTE]
> [Learn more about advanced settings.](../../write/block-settings/advanced.md)
