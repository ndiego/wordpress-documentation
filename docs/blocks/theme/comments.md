---
title: Comments
description: The Comments block is an advanced block that displays post comments with various visual configurations.
type: reference
slug: comments-block
redirect_from:
  - /documentation/article/comment-author-name-block/
  - /documentation/article/comment-content-block/
  - /documentation/article/comment-date-block/
  - /documentation/article/comment-edit-link-block/
  - /documentation/article/comment-link-block/
  - /documentation/article/comment-pagination-block/
  - /documentation/article/comment-reply-link-block/
  - /documentation/article/comment-template-block/
  - /documentation/article/comments-block/
  - /documentation/article/comments-count-block/
  - /documentation/article/comments-title-block/
---

# Comments

The *Comments* block is an advanced block that displays post comments with various visual configurations. It contains multiple blocks to show comments, such as [Comments Title](comments.md), [Comment Template](comments.md), [Comment Pagination](comments.md), and [Post Comments Form](post-comments-form.md). With the Comments block, adding a comment section to your posts becomes effortless.

To add the *Comments* block, open the block inserter by clicking the (**+**) icon on the upper left corner of the editor. After that, look for Comments using the search bar and click it to insert the block into the editor.

![A demonstration on how to add and use Comments block](https://wordpress.org/documentation/files/2023/05/comments.gif)

Alternatively, you can type <kbd>/comments</kbd>on the editor to insert the *Comments* block manually.

> [!NOTE]
> Detailed instructions on adding blocks can be found [here](../../write/blocks/add-a-block.md).

## Block toolbar

Most blocks have their own block-specific controls that allow you to manipulate the block right in the editor.

The *Comments Block* shows the following buttons:

-   Transform to
-   Moving handles
-   Change alignment
-   More options

### Transform to

![The transform button on the Comments block toolbar](https://wordpress.org/documentation/files/2023/05/image-6.png)

The Transform to button lets you change the *Comments* block into a Columns or a Group block.

### Moving handles

![The block moving tools on the Comments block toolbar](https://wordpress.org/documentation/files/2023/05/image6.png)

The dotted icons can be used to drag and drop a block to the place of your choosing. The up and down arrow icons can be used to shift a block up and down in your document.

> [!NOTE]
> [Get more information about moving a block within the editor.](../../write/blocks/move-blocks.md)

### Change alignment

You can modify the alignment of the *Comments* block using this tool. Click on the icon and select one of the following alignment options:

-   **None**
-   **Wide width** – Increase the width of the block beyond the content size.
-   **Full width** – Extend the block to cover the full width of the screen.

![The change alignment options on the Comments block toolbar](https://wordpress.org/documentation/files/2023/02/comments-block-change-alignment.png)

When you transform the *Comments* block into a Columns block, the toolbar will show an additional tool called Change vertical alignment with three options:

-   **Align top** – makes the block top-aligned.
-   **Align middle** – lets you align the block to the center.
-   **Align bottom** – makes the block right-aligned.

![The vertical alignment options on the Comments block toolbar](https://wordpress.org/documentation/files/2023/05/image3.png)

## Options

The **Options** button on a block toolbar gives you more features to customize the block.

> [!NOTE]
> [Read about these and other settings.](../../write/blocks/more-options.md)

## Block settings

The block settings panel contains customization options specific to the block. To open it, select the block and click the *Settings* button next to the *Publish* button.

![The block settings icon](https://wordpress.org/documentation/files/2023/05/image7.png)

It’s possible to change the *Color*, *Typography,* and *Dimensions* settings. To access them, open the *Styles* section:

![The styles tab](https://wordpress.org/documentation/files/2023/05/image4.png)

### Color

The *Comments* block provides color settings options to change the text and background colors.

> [!NOTE]
> For details, refer to this support article: [Color settings overview](../../write/block-settings/color.md)

### Typography

The *Comments* block provides typography settings to change the font family, appearance, line height, letter spacing, decoration, letter case, and font size.

> [!NOTE]
> For details, refer to this support article: [Typography settings overview](../../write/block-settings/typography.md)

### Dimensions

The *Comments* block provides dimension settings options to add padding and margin.

> [!NOTE]
> For details, refer to this support article: [Dimension settings overview](../../write/block-settings/dimensions.md)

### Border

The *paragraph* block provides border settings options to add border color, width, and radius.

> [!NOTE]
> For details refer to this support article: [Border settings overview](../../write/block-settings/border.md)

### Advanced

The following Advanced settings options are available: HTML Anchor, Additional CSS Class(es), Additional CSS, HTML Element, and Styles.

> [!NOTE]
> [Learn more about advanced settings.](../../write/block-settings/advanced.md)

## Comment Template block

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/comment-template-block/; edit it into the page. -->

The *Comment Template* block is a part of the *Comments* block. It contains block elements to display comments, such as the comment author, avatar, and comment content.

### How to use the Comment Template block

When you add a Comments block, the *Comment Template* block is included by default. Also, you can only insert a *Comment Template* block inside a Comments block. Since the *Comment Template* is a part of the Comments block, the content will change on the front-end depending on the query.

![Comment Template block](https://wordpress.org/documentation/files/2022/08/Comment-Template-block.png)

To add a *Comment Template* block, click the block inserter icon (**+**) inside the Comments block to open the block inserter pop-up window and search for the *Comment Template* block.

You can also use the keyboard shortcut<kbd>/comment-template</kbd> to insert a *Comment Template* block quickly.

> [!NOTE]
> Check the detailed instructions on how to add a block [here](../../write/blocks/add-a-block.md).

When the *Comments* block is added in the post editor, the *Comment Template* block will display the actual comments on the post and use a “No results found” placeholder when there’s no comment on the post yet.

![No results found placeholder](https://wordpress.org/documentation/files/2023/04/image-4.png)

### Block toolbar

To view the block toolbar, click on the block, and the toolbar will be displayed.

Every block has unique toolbar icons and blocks specific user controls that allow you to manipulate the block right in the editor.

The *Comment Template* block shows the following buttons:

![Comment Template block toolbar](https://wordpress.org/documentation/files/2023/04/image-2.png)

-   Select Comments block
-   Transform to
-   Drag icon
-   Move arrows
-   Align
-   More options

#### Select Comments block

![Select Comments Query loop block in the Comment Template block](https://wordpress.org/documentation/files/2022/08/Select-Comments-Query-loop-block-in-the-Comment-Template-block.png)

This button will select the Comments block, as it’s the parent block of the *Comment Template* block.

#### Transform to

![Transform tool in the Comment Template block](https://wordpress.org/documentation/files/2022/08/Transform-tool-in-the-Comment-Template-block.png)

When you click the Transform button, you can convert the *Comment Template* block into another block type using the existing content.

#### Block-moving tools

![Block moving tools in the Comment Template block](https://wordpress.org/documentation/files/2022/08/Block-moving-tools-in-the-Comment-Template-block.png)

Use the block-moving tools to move the block up and down inside the editor. Use the six dots icon to drag and drop the *Comment Template* block and reposition it anywhere on the Comments block. Alternatively, click on the up and down arrows to move the block up or down the editor.

> [!NOTE]
> [Get more information about moving a block within the editor.](../../write/blocks/move-blocks.md)

#### Change alignment

![Change alignment in the Comment Template block](https://wordpress.org/documentation/files/2022/08/Change-alignment-in-the-Comment-Template-block.png)

The *change alignment* tool is used for the *Comment Template* block’s position inside the Comments Query Loop block. Choose one of the following block alignment options:

-   None
-   Align left
-   Align center
-   Align right

#### Options

The **Options** button on a block toolbar gives you more features to customize the block.

> [!NOTE]
> [Read about these and other settings.](../../write/blocks/more-options.md)

### Block settings

The block settings panel contains customization options specific to the block. To open it, select the block and click the **Settings** button next to the **Publish** button.

![](https://wordpress.org/documentation/files/2023/04/image-3.png)

#### Typography

Typography settings allow you to change a block’s font size, appearance, line height, letter casing, and spacing.

> [!NOTE]
> [Get more details about changing typography settings.](../../write/block-settings/typography.md)

#### Dimensions

The *Comment Template* block provides dimension settings options to change padding and margin size.

> [!NOTE]
> [For details, refer to this support article: Dimensions Settings Overview.](../../write/block-settings/dimensions.md)

#### Advanced

The following Advanced settings options are available: HTML Anchor, Additional CSS Class(es), Additional CSS, and Styles.

> [!NOTE]
> [Learn more about advanced settings.](../../write/block-settings/advanced.md)

## Comment Author Name block

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/comment-author-name-block/; edit it into the page. -->

The *Comment Author Name* *block* displays the username of the comment’s author. This block is nested inside a Comment Query Loop block and lets you customize the appearance of the comment author’s name.

![The search pop-up window displays the Comment Block with the Comment Author Name Block result.](https://wordpress.org/documentation/files/2022/07/add-comment-author-block.png)

> [!NOTE]
> You can only insert the *Comment Author Name block* inside a Comment Template block within the Comment Query Loop block.

Click the (+) icon inside the Comment Template block to open the block inserter pop-up window and search for the Comment Author Name block.

You can also use the keyboard shortcut `/comment-name` to quickly insert a Comment Author Name block inside a Comment Template block.

> [!NOTE]
> [Detailed instructions on adding blocks](../../write/blocks/add-a-block.md)

### Block toolbar

![The Comment Author name block is selected, with the block toolbar highlighted above it.](https://wordpress.org/documentation/files/2022/07/comment-author-name-block-toolbar.png)

The block toolbar contains the tools to customize each block. The Comment Author Name block’s toolbar is relatively simple with the following tools:

**Transform to**

You can transform a *Comment Author Name block* into a Columns, or a Group block.

![The Comment Author name block is selected, with the ‘Transform To’ tool highlighted.](https://wordpress.org/documentation/files/2022/07/comment-author-name-block-transform-tool.png)

**Block-moving tools**

![The Comment Author name block is selected, with the ‘Move’ tool highlighted.](https://wordpress.org/documentation/files/2022/07/comment-author-name-block-move-too.png)

Use the block-moving tools to move the block up and down the editor. Use the six dots icon to drag and drop the Comment Author Name block and reposition it anywhere on the editor. Alternatively, click on the up and down arrows to move the block up or down the editor.

> [!NOTE]
> [Get more information about moving a block within the editor.](../../write/blocks/move-blocks.md)

**Change text alignment**

![The Comment Author name block is selected, with the ‘Change Text Alignment’ tool highlighted.](https://wordpress.org/documentation/files/2022/07/comment-author-name-block-change-text-alignment.png)

Text alignment options lets you choose to align the author’s name left, center, or right.

#### More options

![The Comment Author name block is selected, with ‘More Options’ in the toolbar highlighted.](https://wordpress.org/documentation/files/2022/07/comment-author-name-block-more-options.png)

> [!NOTE]
> [Read about these and other settings.](../../write/blocks/more-options.md)

### Block settings

The block settings panel contains customization options specific to the block. To open it, select the block and click the cog icon next to the Publish button.

Here are the options for the Comment Author Name block:

#### Link

![The Comment Author name block’s settings, with ‘Link to authors URL’ highlighted.](https://wordpress.org/documentation/files/2022/07/comment-author-name-block-settings-link.png)

In the Link Settings section, you can enable the *`Link to authors URL`* option to link the author’s name to their profile page. When you enable it, the `Open in new tab` option will appear. Enable it if you want the author’s profile page opened in a new tab.

#### Color

Text and background colors can be set on a per-block basis, allowing you to call attention to important content. Pick a color from the suggestions, or add a custom color using the color picker or by adding a color code.

![The Comment Author name block’s settings, with ‘Color' highlighted.](https://wordpress.org/documentation/files/2022/07/comment-author-name-block-settings-colors.png)

> [!NOTE]
> [See this guide for more information about changing colors.](../../write/block-settings/color.md)

#### Typography

Typography settings allow you to change a block’s font size, appearance, line height, letter casing, and spacing.

![The Comment Author name block’s settings, with ‘Typography’ highlighted.](https://wordpress.org/documentation/files/2022/07/comment-author-name-block-settings-typography.png)

> [!NOTE]
> [Get more details about changing typography settings.](../../write/block-settings/typography.md)

#### Dimension

Dimension controls are used to control how groups of blocks are placed alongside one another, by changing the values for padding, margin, and other dimensions

![The Comment Author name block’s settings, with ‘Dimension’ highlighted.](https://wordpress.org/documentation/files/2022/07/comment-author-name-block-settings-dimensions.png)

> [!NOTE]
> [Learn more about dimension controls.](../../write/block-settings/dimensions.md)

**Advanced**

The following Advanced settings options are available: HTML Anchor, Additional CSS Class(es), Additional CSS, and Styles.

> [!NOTE]
> [Learn more about advanced settings.](../../write/block-settings/advanced.md)

## Comment Content block

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/comment-content-block/; edit it into the page. -->

The *Comment Content* block displays the content of a comment. This block is located inside a Comment Query Loop block and lets you customize the appearance of the comment’s content.

![Comment Content block](https://wordpress.org/documentation/files/2022/08/Comment-Content-block-1024x547-1.png)

> [!NOTE]
> You can only insert the *Comment Content* block inside a Comment Template block within the Comment Query Loop block.

Click the (+) icon inside the comment template block to open the block inserter pop-up window and search for the *Comment Content* block.

You can also use the keyboard shortcut <kbd>/comment-content</kbd> to quickly insert a *Comment Content* block inside a Comment Template block.

![How to quickly add a comment content block](https://wordpress.org/documentation/files/2022/08/How-to-quickly-add-a-comment-content-block.png)

> [!NOTE]
> [Detailed instructions on adding blocks](../../write/blocks/add-a-block.md)

### Block toolbar

The block toolbar contains the tools to customize each block. The *Comment Content* block’s toolbar consists of the following tools:

![Block toolbar in the Comment Content block](https://wordpress.org/documentation/files/2022/08/Block-toolbar-in-the-Comment-Content-block.png)

**Transform to**

You can transform a *Comment Content block* into a Columns, or a Group block.

![Transform option in the Comment Content block](https://wordpress.org/documentation/files/2022/08/Transform-option-in-the-Comment-Content-block.png)

**Block-moving tools**

![Block moving tools in the Comment Content block](https://wordpress.org/documentation/files/2022/08/Block-moving-tools-in-the-Comment-Content-block.png)

Use the block-moving tools to move the block up and down inside the editor. Use the six dots icon to drag and drop the *Comment Content* block and reposition it anywhere on the editor. Alternatively, click on the up and down arrows to move the block up or down the editor.

> [!NOTE]
> [Get more information about moving a block within the editor.](../../write/blocks/move-blocks.md)

**Change text alignment**

![Change text alignment in the Comment Content block](https://wordpress.org/documentation/files/2022/08/Change-text-alignment-in-the-Comment-Content-block.png)

Text alignment options let you align the content of a comment towards the left, center, or right.

#### More options

![](https://wordpress.org/documentation/files/2022/08/Comment-Content-Block-more-options.png)

The [More Options menu](../../write/blocks/more-options.md) represented by **three vertical dots on the far right of the toolbar** gives you more features such as the ability to duplicate, remove, or edit your block as HTML.

> [!NOTE]
> [Read about these and other settings.](../../write/blocks/more-options.md)

### Block settings

Every block has specific options in the editor sidebar in addition to the options found in the block toolbar. *If you do not see the sidebar, click the ‘sidebar’ icon.*

![Sidebar icon to display the Block sidebar](https://wordpress.org/documentation/files/2022/08/sidebar-icon-to-display-the-Block-sidebar.png)

Here are the options for the *Comment Content* block:

#### Color

The *comment content block* lets you customize the text, and background colors.

Click on any of the options to change the color. Choose from the default color or click the upper rectangle area to pick a custom color using the color picker.

![Color settings in the Comment Content block](https://wordpress.org/documentation/files/2022/08/Color-settings-in-the-Comment-Content-block.png)

> [!NOTE]
> [See this guide for more information about changing colors.](../../write/block-settings/color.md)

#### Typography

Typography settings allow you to change a block’s font size, appearance, line height, letter casing, and spacing.

![Typography settings in the Comment Content block](https://wordpress.org/documentation/files/2022/08/Typography-settings-in-the-Comment-Content-block.png)

> [!NOTE]
> [Get more details about changing typography settings.](../../write/block-settings/typography.md)

#### Dimensions

Dimension controls are used to control how groups of blocks are placed alongside one another, by changing the values for padding, margin, and other dimensions.

![Dimension settings in the Comment Content block](https://wordpress.org/documentation/files/2022/08/Dimensions.png)

> [!NOTE]
> [Learn more about dimension controls.](../../write/block-settings/dimensions.md)

**Advanced**

The following Advanced settings options are available: HTML Anchor, Additional CSS Class(es), Additional CSS, and Styles.

> [!NOTE]
> [Learn more about advanced settings.](../../write/block-settings/advanced.md)

## Comment Date block

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/comment-date-block/; edit it into the page. -->

The *Comment Date* *block* displays the date on which a comment was posted. This block is located inside a Comment Query Loop block and allows users to edit the appearance of the comment date.

![Comment Date inside the Comment Template block within the Comment](https://wordpress.org/documentation/files/2022/07/comment-date-block.png)

> [!NOTE]
> You can only insert the *Comment Date block* inside a Comment Template block within the Comment Query Loop block.

Click the (+) icon inside the Comment Template block to open the block inserter pop-up window and search for the Comment Date Block.

You can also use the keyboard shortcut `/comment-date` to quickly insert a Comment Date block inside a Comment Template block.

![How to add a Comment Date block](https://wordpress.org/documentation/files/2022/07/Block.gif)

> [!NOTE]
> [Detailed instructions on adding blocks](../../write/blocks/add-a-block.md)

### Block toolbar

![Block toolbar in the Comment Date block](https://wordpress.org/documentation/files/2022/07/Block-toolbar-in-the-Comment-Date-block.png)

The block toolbar contains the tools to customize each block. The Comment Date block’s toolbar consists of the following tools:

**Transform to**

You can transform a *Comment Date block* into a Columns, or a Group block.

![Transform option in the Comment Date block](https://wordpress.org/documentation/files/2022/08/Screen-Shot-2022-08-02-at-10.50.22-AM-1.png)

**Block-moving tools**

![Move tools in the Comment Date block](https://wordpress.org/documentation/files/2022/07/Move-tools-in-the-Comment-Date-block.png)

Use the block-moving tools to move the block up and down inside the editor. Use the six dots icon to drag and drop the *Comment Date Block* and reposition it anywhere on the editor. Alternatively, click on the up and down arrows to move the block up or down the editor.

> [!NOTE]
> [Get more information about moving a block within the editor.](../../write/blocks/move-blocks.md)

**More options**

The [More Options menu](../../write/blocks/more-options.md) represented by **three vertical dots on the far right of the toolbar** gives you more features such as the ability to duplicate, remove, or edit your block as HTML.

![](https://wordpress.org/documentation/files/2022/07/More-Options-menu-.png)

> [!NOTE]
> [Read about these and other settings.](../../write/blocks/more-options.md)

### Block settings

The block settings panel contains customization options specific to the block. To open it, select the block and click the cog icon next to the Publish button.

Here are the options for the *Comment Date Block*:

#### Settings

![Block settings in the Comment Date block](https://wordpress.org/documentation/files/2022/07/Block-settings-in-the-Comment-Date-block.png)

In the Settings tab, you can select the Date format. By turning on the *Default format* option, you can choose to use the default date format. When this setting is turned off, you can select the preferred date format from the drop-down list or enter a custom date or time [format](../../manage/settings/date-and-time-format.md).

![Changing the Default date format in the Comment Date block](https://wordpress.org/documentation/files/2022/07/Screen-Shot-2022-07-25-at-9.47.41-AM-2.png)

You can also turn on/off the ‘*Link to comment’* switch. Turning on this button will link the date field to the specific comment.

#### Color

The *Comment Date Block* lets you customize the text, background, and link color. Click on any of the options to change the color. Choose from the default color or click the upper rectangle area to pick a custom color using the color picker.

![Color settings in the Comment Date block](https://wordpress.org/documentation/files/2022/07/Screen-Shot-2022-07-25-at-9.55.47-AM-1.png)

> [!NOTE]
> [See this guide for more information about changing colors.](../../write/block-settings/color.md)

#### Typography

To access all the typography options click on the 3-dot button in the right corner of the Typography tab. You also have the option to Reset all the typography changes you made by clicking on the Reset all option in the dropdown.

![Reset all typography settings](https://wordpress.org/documentation/files/2022/07/Screen-Shot-2022-07-25-at-10.04.20-AM.png)

> [!NOTE]
> [Get more details about changing typography settings.](../../write/block-settings/typography.md)

**Advanced**

The following Advanced settings options are available: HTML Anchor, Additional CSS Class(es), Additional CSS, and Styles.

> [!NOTE]
> [Learn more about advanced settings.](../../write/block-settings/advanced.md)

## Comment Edit Link block

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/comment-edit-link-block/; edit it into the page. -->

The *Comment Edit Link* block displays a link to edit the comment in the WordPress Dashboard. This block is located inside a Comment Query Loop block and lets you customize the appearance of the *Edit* link. The Edit link is only visible to users who have permission to edit the comments.

![Comment Edit Link Block](https://wordpress.org/documentation/files/2022/08/Comment-Edit-Link-Block.png)

> [!NOTE]
> You can only insert the *Comment Edit Link* block inside a Comment Template block within the Comment Query Loop block.

Click the (+) icon inside the comment template block to open the block inserter pop-up window and search for the *Comment Edit Link* block.

You can also use the keyboard shortcut <kbd>/comment-edit-link</kbd>to quickly insert a *Comment Edit Link* block inside a Comment Template block.

![How to quickly add Comment Edit Link Block](https://wordpress.org/documentation/files/2022/08/How-to-quickly-add-Comment-Edit-Link-Block.gif)

> [!NOTE]
> [Detailed instructions on adding blocks](../../write/blocks/add-a-block.md)

### Block toolbar

![Block toolbar in the Comment Edit Link Block](https://wordpress.org/documentation/files/2022/08/Block-toolbar-in-the-Comment-Edit-Link-Block.png)

The block toolbar contains the tools to customize each block. The *Comment Edit Link* block’s toolbar consists of the following tools:

**Transform to**

You can transform a *Comment Edit Link* block into a Columns block, or a Group block.

![Transform tool in the Comment Edit Link Block](https://wordpress.org/documentation/files/2022/08/Transform-tool-in-the-Comment-Edit-Link-Block.png)

**Block-moving tools**

![Block moving tool in the Comment Edit Link Block](https://wordpress.org/documentation/files/2022/08/Block-moving-tool-in-the-Comment-Edit-Link-Block.png)

> [!NOTE]
> [Get more information about moving a block within the editor.](../../write/blocks/move-blocks.md)

Use the block-moving tools to move the block up and down inside the editor. Use the six dots icon to drag and drop the *Comment Edit Link* block and reposition it anywhere on the editor. Alternatively, click on the up and down arrows to move the block up or down the editor.

**Change text alignment**

![Change text alignment in the Comment Edit Link Block](https://wordpress.org/documentation/files/2022/08/Change-test-alignment-in-the-Comment-Edit-Link-Block.png)

Text alignment options let you align the Edit button towards the left, center, or right.

**More options**

![](https://wordpress.org/documentation/files/2022/08/more-options.png)

The [More Options menu](../../write/blocks/more-options.md) represented by **three vertical dots on the far right of the toolbar** gives you more features such as the ability to duplicate, remove, or edit your block as HTML.

> [!NOTE]
> [Read about these and other settings.](../../write/blocks/more-options.md)

### Block settings

The block settings panel contains customization options specific to the block. To open it, select the block and click the cog icon next to the Publish button.

![The cog icon in the Comment Edit Link Block to show the Block settings](https://wordpress.org/documentation/files/2022/08/The-cog-icon-in-the-Comment-Edit-Link-Block-to-show-the-Block-settings.png)

Here are the options for the *Comment Edit Link* block:

#### Link

![Link settings in the Comment Edit Link Block](https://wordpress.org/documentation/files/2022/08/Link-settings-in-the-Comment-Edit-Link-Block.png)

In the Link Settings section, you can enable the *open in new tab* option, and if enabled, will open the link editing page in a new tab.

#### Color

The Comment Edit Link block lets you customize the background and link color.

Click on any of the options to change the color. Choose from the default color or click the upper rectangle area to pick a custom color using the color picker.

![Color settings in the Comment Edit Link Block](https://wordpress.org/documentation/files/2022/08/Color-settings-in-the-Comment-Edit-Link-Block.png)

> [!NOTE]
> [See this guide for more information about changing colors.](../../write/block-settings/color.md)

#### Typography

Typography settings allow you to change a block’s font size, appearance, line height, letter casing, and spacing.

![Typography settings in the Comment Edit Link Block](https://wordpress.org/documentation/files/2022/08/Typography-settings-in-the-Comment-Edit-Link-Block.png)

> [!NOTE]
> [Get more details about changing typography settings.](../../write/block-settings/typography.md)

**Advanced settings**

The following Advanced settings options are available: HTML Anchor, Additional CSS Class(es), Additional CSS, and Styles.

> [!NOTE]
> [Learn more about advanced settings.](../../write/block-settings/advanced.md)

## Comment Reply Link block

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/comment-reply-link-block/; edit it into the page. -->

The *Comment Reply Link* block displays a link to reply to a comment. This block is located inside a Comment Query Loop block and lets you customize the appearance of the *Reply* link.

![Comment Reply Link Block](https://lh4.googleusercontent.com/2qkG0uLJ3t45aQx2_6X3nDsuc0_hawJhKH96SuSz8DuHBT46XOM38iwR2a0qShWjk24fqsBaXYkQoZf6hCQEqhPzLl6cWT79rdQMCx4VWg7sAETiqxGkKutyslXenkCTQ6h7-5VK3b_jiEsetjlvc-k)

> [!NOTE]
> You can only insert the *Comment Reply Link block inside* a Comment Template block within the Comment Query Loop block.

Click the (+) icon inside the comment template block to open the block inserter pop-up window and search for the *Comment Reply Link* block.

You can also use the keyboard shortcut <kbd>/comment-reply-link</kbd> to quickly insert a *Comment Reply Link* block inside a Comment Template block.

![How to quickly add a Comment Reply Link Block](https://lh6.googleusercontent.com/qzz5T7BXN33y4o_aYdisYXEd4dWwuxtglkR7wKQXlcFJ7wWVK_ZZBp6bb5Hn0TjlKBOjpn61hkOO3z_FOtfF3aPwUw6iYZ4D7kCYQJMwGcjDp3FMUY0kpZQJuBKeurt14ZOR_u4Zrh8h3NsK3yQ7Xbs)

> [!NOTE]
> [Detailed instructions on adding blocks](../../write/blocks/add-a-block.md)

### Block toolbar

![Block toolbar in the Comment Reply Link Block](https://lh5.googleusercontent.com/BeMk7rRjEPCTc3NOEAnYbvKdpjvvffn6gTek7ZbpRM635PB5NDUyjLsmZeoie22r1lMtJByLe6xcvi7CYuKnArc7uSDlNRHlWYFIelkrfyg9CAFRShjSpfOMbOBgJkJcOHHjypQXgxjhDQl9X04KqwE)

The block toolbar contains the tools to customize each block. The *Comment Reply Link* block’s toolbar consists of the following tools:

**Transform to**

You can transform a *Comment Reply Link* block into a Columns block or a Group block.

![Transform option in the Comment Reply Link Block](https://lh4.googleusercontent.com/J6mKf2Rrh-lzXBkV8DugIRjlWWeOrphkvOy7-E6teMYfuml_ulzHypOTIIk2clxvuxrhpPNZsJrlOtgHNL8-f2ajSmXgnIqV5uV0OIfiaK2x-BUPLCkOI4548Qd0hJD-y3ldvP-qB7xZp1ZSQHcDvjw)

**Block-moving tools**

![Block moving tools in the Comment Reply Link Block](https://lh6.googleusercontent.com/zerLYnIAfvt1oLwK43IfX77l45_Y0WcXwviqoIpkrdrKz3qDnbnUCJLpKWdW24JVoj4WK7DGtCJRPcZHjnXVKtUbPR67DZX_Sy54a8h7m0x7CXCPFyAA046qBYnftJnDhHjOtHGxMkq6WfZLLEKpNgU)

Use the block-moving tools to move the block up and down inside the editor. Use the six dots icon to drag and drop the *Comment Reply Link* block and reposition it anywhere on the editor. Alternatively, click on the up and down arrows to move the block up or down the editor.

**Change text alignment**

![Change text alignment in the Comment Reply Link Block](https://lh3.googleusercontent.com/h618HMcHPRguRHMmeq6XgU7F2_UyUVOe1W6LtV1ddQBpuMKvB2XkIAZrlzmIx0-n0vdn1Kmmkhe4r0IpGwjAd-_3Ryti4mFdo54SiswmOIfTratt8kHceJuBp8XWwWHGvS3ZHA3hdoMRfyAQl8e3bUU)

Text alignment options let you align the Reply button towards the left, center, or right.

**More options**

![](https://lh3.googleusercontent.com/sL3Gq4hftCL805JJlLvDjLvxZgzvCgI2h9utgz6l9KI3d8QA3LwBFX39cNYqRodnpAnUHnUTZw8v1CtP4oAdoD-I4wQSTpEOnzAff485usY4wV4EWog6XvyZz7kXet8dePFOESCiUW38aYuiqyxwnoI)

The [More Options menu](../../write/blocks/more-options.md) represented by **three vertical dots on the far right of the toolbar** gives you more features such as the ability to duplicate, remove, or edit your block as HTML.

> [!NOTE]
> [Read about these and other settings.](../../write/blocks/more-options.md)

### Block settings

The block settings panel contains customization options specific to the block. To open it, select the block and click the cog icon next to the Publish button.

![The cog icon next to the Publish button to show the Block settings](https://lh4.googleusercontent.com/HtGEIdSPLZrFI2qjZV4mkowTN7imirz2GTj-4qTYPQqJQNGOnxXmvNZVLP82ttInuHgdbWoaexr8q7C6qyksXpl26pNYh34vXwF92YwMp2jOSKVSKMpsAbkggYwgCPEOc-2kkaA0mzXRaK-lad0x2sY)

Here are the options for the *Comment Reply Link* block:

#### Color

The Comment Reply Link block lets you customize the background and link color.

Click on any of the options to change the color. Choose from the default color or click the upper rectangle area to pick a custom color using the color picker.

![Colors settings in the Comment Reply Link Block](https://lh3.googleusercontent.com/IbApTu0gzDVNuFFjCFqijp_NVC1-OOfh8-sQTrxhnDV3RxXMdeWu-zqao0CXJSQj5ZWaRA-1ajwcWP-ipKbx-GKQE7rfTt-F0jsjYojMenFEruc2FXNbcF-Wm_acdFqQ2xca2rWSokleO6B8JKNlyGM)

> [!NOTE]
> [See this guide for more information about changing colors.](../../write/block-settings/color.md)

#### Typography

![Typography settings in the Comment Reply Link Block](https://lh5.googleusercontent.com/MGFlPOoJjFHQGcNOEDZ9MEQniYI_J4dry5fWVy8n-srhzNBZdea-6c_c6FNeX7__g74Wt03EkPrOUiY6qwbXi5uB_xuRYDugclKXg_6D0PM1UbRYiDPUiqKfL2zoKV_Mnx3__RIfF1N4NIWwiuQfrpY)

> [!NOTE]
> [Get more details about changing typography settings.](../../write/block-settings/typography.md)

**Advanced**

The following Advanced settings options are available: HTML Anchor, Additional CSS Class(es), Additional CSS, and Styles.

> [!NOTE]
> [Learn more about advanced settings.](../../write/block-settings/advanced.md)

## Comments Pagination block

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/comment-pagination-block/; edit it into the page. -->

The *Comments Pagination* block is part of the Comments block that displays paginated navigation to the previous or next comment sections.

By default, a *Comments Pagination* block is included when you insert a Comments block. However, you can still add this block manually.

![Comment Pagination block inside Comment Query loop block](https://wordpress.org/documentation/files/2022/08/Comment-Pagination-block-inside-Comment-Query-loop-block.png)

> [!NOTE]
> You can only insert the *Comments Pagination block* inside a Comments block.

To add the block, select the Comments block and hover your mouse over a blank space. Click the (+) icon to open the block inserter pop-up window. Look for the *Comments Pagination* block using the search bar and click on the block icon to add it to the Comments block.

Alternatively, add a Paragraph block within the Comments block and type /comments-pagination to insert the *Comments Pagination* block.

![How to quickly add Comment Pagination block](https://wordpress.org/documentation/files/2022/08/How-to-quickly-add-Comment-Pagination-block.gif)

> [!NOTE]
> [Detailed instructions on adding blocks](../../write/blocks/add-a-block.md)

### Block toolbar

The *block toolbar* contains tools to customize each block on the editor quickly. The *Comments Pagination* block has the following tools:

#### Select comments block

![](https://wordpress.org/documentation/files/2023/10/image-12.png)

The Select Comments tool lets highlight the *Comment Pagination*’s parent block, which is the Comments block.

#### Transform to

You can transform a *Comment Pagination block* into a Columns, or a Group block.

![Transform option in the Comment Pagination block](https://wordpress.org/documentation/files/2022/08/Screen-Shot-2022-08-02-at-10.07.57-AM.png)

#### Block-moving tools

![Block moving tools for Comment Pagination block](https://wordpress.org/documentation/files/2022/08/Block-moving-tools-for-Comment-Pagination-block.png)

The block-moving tools allow you to move the block up and down the editor. Use the six dots icon to drag and drop the *Comments Pagination* block and place it anywhere on the Comments block. Alternatively, click on the up and down arrows to move the block up or down.

> [!NOTE]
> [Get more information about moving a block within the editor.](../../write/blocks/move-blocks.md)

#### Change items justification

![Change items justification for Comment Pagination block](https://wordpress.org/documentation/files/2022/08/Change-items-justification-for-Comment-Pagination-block.png)

The *change items justification* tool lets you change the horizontal placement of the items inside the *Comment Pagination* block. There are four options to choose from:

-   *Justify items left* will move the items towards the left side of the block.
-   *Justify items center* will move the items towards the center of the block.
-   *Justify items right* will move the items towards the right side of the block.
-   *Space between items* will distribute all items across the block and automatically adjust the space between them.

#### Change vertical alignment

![Change vertical alignment for Comment Pagination block](https://wordpress.org/documentation/files/2022/08/Change-vertical-alignment-for-Comment-Pagination-block.png)

The *change vertical alignment* tool lets you choose the vertical position of the items inside the *Comments Pagination* block. You can choose between top, middle, and bottom vertical alignment.

#### Change alignment

![Change alignment for Comment Pagination block](https://wordpress.org/documentation/files/2022/08/Change-alignment-for-Comment-Pagination-block.png)

Unlike the previous alignment tools, the *change alignment* tool is used for the *Comments Pagination* block’s position inside the Comments block. Choose one of the following block alignment options:

-   None
-   Align left
-   Align center
-   Align right

#### More options

These controls give you the option to copy, duplicate, and edit your block as HTML.

![More options in the Comment Pagination block](https://wordpress.org/documentation/files/2022/08/More-options-in-the-Comment-Pagination-block.png)

> [!NOTE]
> [Read about these and other settings.](../../write/blocks/more-options.md)

### Block settings

The block settings panel contains customization options specific to the block. To open it, select the block and click the cog icon next to the Publish button.

Here are the options for the *Comments Pagination* block:

#### Layout

![Layout settings in the Comment Pagination block](https://wordpress.org/documentation/files/2022/08/Layout-settings-in-the-Comment-Pagination-block.png)

In the layout section, you will find the following customization options:

-   *Justification* settings are similar to the tools in the block toolbar.
-   *Orientation* lets you choose to display the pagination items horizontally or vertically.
-   *Allow to wrap to multiple lines* toggle button lets you display the pagination items in multiple lines when needed.

#### Settings

![More settings in the Comment Pagination block](https://wordpress.org/documentation/files/2022/08/More-settings-in-the-Comment-Pagination-block.png)

The settings section shows three options for a decorative arrow to the next and previous comments link. Here are the options:

-   None
-   Arrow
-   Chevron

#### Color

![Color settings in the Comment Pagination block](https://wordpress.org/documentation/files/2022/08/Color-settings-in-the-Comment-Pagination-block.png)

The color section lets you customize the text, background, and link color for the Comments Pagination block. Click on any of the options to change the color, and a pop-up to pick a color will appear. Choose from the default color or click the upper rectangle area to pick a custom color using the color picker.

> [!NOTE]
> [Read about these and other settings.](../../write/blocks/more-options.md)

#### Typography

![Typography tool for the comment pagination block](https://wordpress.org/documentation/files/2023/10/image-11.png)

The Typography settings enable you to customize the font and text appearance of the content within the *Comments Pagination* block. The settings have various options, such as font size, font style, font family, and letter spacing.

> [!NOTE]
> [Learn more about the Typography settings.](../../write/block-settings/typography.md)

#### Advanced

The following Advanced settings options are available: HTML Anchor, Additional CSS Class(es), Additional CSS, and Styles.

> [!NOTE]
> [Learn more about advanced settings.](../../write/block-settings/advanced.md)

### Comments Pagination inner blocks

The *Comments Pagination* block consists of the following three inner blocks (which can’t be inserted on their own):

-   Comments Previous Page block
-   Comments Page Numbers block
-   Comments Next Page block

The Comments Previous Page block displays the previous posts page link.

The Comments Page Numbers block displays a list of page numbers for pagination.

The Comments Next Page block displays the next posts page link.

All these blocks are located inside a Comments block and lets you customize the appearance of the pagination.

#### Block toolbar

![Block toolbar in the pagination inner blocks](https://wordpress.org/documentation/files/2022/08/Block-toolbar-comments-pagination.png)

The block toolbar for all the *Comments Pagination* inner blocks – Comments Previous Page, Comments Page Numbers, and Comments Next Page contains the tools to customize each block.

##### Block-moving tools

![Block moving tool in the pagination inner blocks](https://wordpress.org/documentation/files/2022/08/Block-moving-tool-in-the-pagination-inner-blocks.png)

Use the block-moving tools to move the block up and down inside the editor. Use the six dots icon to drag and drop the block and reposition it anywhere on the editor. Alternatively, click on the up and down arrows to move the block up or down the editor.

##### More options

![](https://wordpress.org/documentation/files/2022/08/More-options-comments-pagination.png)

Page Numbers, Next Page and Previous page blocks share the same functionality for more block options button. Click on the three dots icon to show more options and a drop-down menu will appear.

#### Block settings

The block settings panel contains customization options specific to the block. To open it, select the block and click the **Settings** panel icon next to the **Publish** or **Update** button.

Here are the options for the *Comments Pagination* inner blocks.

##### Color

The *Comments Pagination* inner blocks – Comments Previous Page, Comments Page Numbers, and Comments Next Page provides color settings option to add background color.

For details refer to this support article: [Color settings overview](../../write/block-settings/color.md)

##### Typography

The *Comments Pagination* inner blocks – Comments Previous Page, Comments Page Numbers, and Comments Next Page provides typography settings to change the font family, appearance, line height, letter spacing, decoration, letter case, and font size.

For details refer to this support article: [Typography settings overview](../../write/block-settings/typography.md)

##### Advanced

The **Advanced** tab lets you add CSS class(es) to your block. This will allow you to write custom CSS and styles for the block.

![Advanced tab with additional CSS](https://wordpress.org/documentation/files/2022/11/Screenshot-2022-11-11-at-11.26.17-AM-1.png)

*Advanced option in the selected Block*

## Comments Title block

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/comments-title-block/; edit it into the page. -->

The **Comments Title** block displays a title with the number of comments. The block is nested inside the Comments block and allows you to customize the comment title.

You can only insert the **Comments Title** block inside a Comments block.

By default, the **Comments Title** block is included when you insert the Comments block into the editor. However, you can still insert it manually when needed.

[Watch the video](https://wordpress.org/documentation/files/2022/11/202590642-80e9154d-a034-403b-9d90-1294b5c1cabb.mp4)

To add a **Comments Title** block, click the (+) icon inside the Comments block to open the block inserter window pop-up and look for the **Comments Title** block.

Alternatively, you can manually insert the **Comments Title** block using the keyboard shortcut <kbd>/comments-title.</kbd>

> [!NOTE]
> Detailed instructions on adding blocks can be found [here](../../write/blocks/add-a-block.md).

### Block toolbar

The block toolbar displays several tools used to customize each block. When you select the **Comments Title** block, it will show the block toolbar that contains the following tools:

**Select Comments block**

![Select Comments block in the Comments Title block](https://wordpress.org/documentation/files/2022/11/Select-Comments-block-in-the-Comments-Title-block.png)

The Select Comments block button lets you navigate to the Comments block, the parent’s block of the **Comments Title** block.

**Transform to**

![Transform tool in the Comments Title block](https://wordpress.org/documentation/files/2022/11/Transform-tool-in-the-Comments-Title-block.png)

Use the Transform to button to change the **Comments Title** block into a Columns or a Group block.

**Block-moving tools**

![Block moving tool in the Comments Title block](https://wordpress.org/documentation/files/2022/11/Block-moving-tool-in-the-Comments-Title-block.png)

The block-moving tool lets you adjust the position of the **Comments Title** block within the Comments block. The six dots icon functions as a drag-and-drop, allowing you to move and place the **Comments Title** block anywhere in the Comments block. Meanwhile, you can use the arrow icons to move the block up or down.

**Change alignment**

![Change alignment in the Comments Title block](https://wordpress.org/documentation/files/2022/11/Change-alignment-in-the-Comments-Title-block.png)

You can change the alignment of the **Comments Title** block using this tool. Click on the Change alignment icon and select one of the following alignment options:

-   None
-   Align left
-   Align center
-   Align right

**Change text alignment**

![Change text alignment in the Comments Title block](https://wordpress.org/documentation/files/2022/11/Change-text-alignment-in-the-Comments-Title-block.png)

Click the Change alignment button to display the alignment dropdown that contains the following options:

-   Align text left
-   Align text center
-   Align text right

The alignment options let you adjust the **Comments Title** block text to the left and right or make it centered-aligned.

**Change heading level**

![Change heading level in the Comments Title block](https://wordpress.org/documentation/files/2022/11/Change-heading-level-in-the-Comments-Title-block.png)

You can change the heading level of the **Comments Title** block by selecting this button and choosing a heading from H1 to H6.

**More options**

The [More Options menu](../../write/blocks/more-options.md) represented by **three vertical dots on the far right of the toolbar** gives you more features such as the ability to duplicate, remove, or edit your block as HTML.

![Examples of the location of the "More Options" menu in a Paragraph block.](https://wordpress.org/documentation/files/2023/08/more-options-generic-6-3.png)

*Example of the location of the “More Options” menu in a Paragraph block.*

> [!NOTE]
> [Read about these and other settings.](../../write/blocks/more-options.md)

### Block settings

WordPress blocks have specific configuration options in the block settings panel. To access the **Comments Title** block settings panel, click the **Settings** button at the top-right corner of the WordPress editor. Alternatively, click the **More options** or three dots icon in the **Comments Title** block toolbar and select **Show more settings**.

**Settings**

You can toggle the post title in the **Comments Title** block in the Settings section by enabling the **Show post title** option. You can also choose whether to show the number of comments in the block by toggling on or off the **Show comments count** option.

![Settings in the Comments Title block](https://wordpress.org/documentation/files/2022/11/Screenshot-2026-05-25-at-1.47.55-PM.png)

**Color**

The **Comments Title** block provides Color settings options to change the text and background colors.

For details refer to this support article: [Color settings overview](../../write/block-settings/color.md)

**Typography**

The **Comments Title** block provides typography settings to change the font family, appearance, line height, letter spacing, decoration, letter case, and font size.

For details refer to this support article: [Typography settings overview](../../write/block-settings/typography.md)

**Dimensions**

The **Comments Title** block provides dimension settings options to add padding and margin.

For details refer to this support article: [Dimension settings overview](../../write/block-settings/dimensions.md)

**Border**

The **Comments Title** block provides border settings options to add border color, width, and radius.

For details refer to this support article: [Border settings overview](../../write/block-settings/border.md)

**Advanced**

The following Advanced settings options are available: HTML Anchor, Additional CSS Class(es), Additional CSS, and Styles.

> [!NOTE]
> [Learn more about advanced settings.](../../write/block-settings/advanced.md)

## Comments Count block

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/comments-count-block/; edit it into the page. -->

The Comments Count block displays the total number of comments for the current post or page. It’s most useful in single post/page templates or inside a Post Template within a Query Loop.

### Where you can use this block

-   Single posts and pages (when comments are enabled).
-   Post Template inside a Query Loop (for example, on index or archive templates).
-   Note: The block requires post context. It won’t display on non‑singular pages unless it’s inside a Post Template (such as within a Query Loop).

### Add the Comments Count block

1.  Open a post, page, or template in the editor.
2.  Place your cursor where you want the count to appear (for example, near the byline or meta).
3.  Click the + Block Inserter, search for “Comments Count,” and select it. Tip: You can also type /comments count on a new line to insert it quickly.

### Behavior notes

-   The block respects your Discussion settings. If comments are disabled, the count may show 0 or be hidden depending on your theme and settings.
-   If a post is password‑protected, the count may be hidden until the password is entered (behavior can vary by theme).
-   When used in a Query Loop, each Comments Count displays the correct total for its corresponding post.

### Block toolbar

The block toolbar displays several tools used to customize each block. When you select the **Comments Count** block, it will show the block toolbar that contains the following tools:

#### Transform to

Click on the “Transform” button to convert the *Comments Count* block into a “Group”, “Columns”, “Details”, or “Comments Count” block.

![](https://wordpress.org/documentation/files/2025/11/comments-count-transform.png)

#### Drag icon

To drag and drop the block to a new location, click and hold the rectangle of dots, then drag it to the new location. The blue separator line indicates where the block will be placed. Release the left mouse button when you find the new location to place the block.

![](https://wordpress.org/documentation/files/2025/11/comments-count-drag-1.png)

> [!NOTE]
> Detailed instructions on moving a block within the editor can be found [here](../../write/blocks/move-blocks.md)

#### Move arrows

The up and down arrow icons can be used to move the block up and down on the page.

![](https://wordpress.org/documentation/files/2025/11/comments-count-move-arrow-1.png)

#### Align

Use the change alignment tool to align the *Comments Count* block. Choose one of the following options:

-   **Align text left**
-   **Align text right**
-   **Align text center**

![](https://wordpress.org/documentation/files/2025/11/comments-count-align.png)

### Block settings

WordPress blocks have specific configuration options in the block settings panel. To access the **Comments Count** block settings panel, click the **Settings** button at the top-right corner of the WordPress editor. Alternatively, click the **More options** or three dots icon in the **Comments Count** block toolbar and select **Show more settings**.

**Color**

The **Comments Count** block provides Color settings options to change the text and background colors.

For details refer to this support article: [Color settings overview](../../write/block-settings/color.md)

**Typography**

The **Comments Count** block provides typography settings to change the font family, appearance, line height, letter spacing, decoration, letter case, and font size.

For details refer to this support article: [Typography settings overview](../../write/block-settings/typography.md)

**Dimensions**

The **Comments Count** block provides dimension settings options to add padding and margin.

For details refer to this support article: [Dimension settings overview](../../write/block-settings/dimensions.md)

**Border**

The **Comments Count** block provides border settings options to add border color, width, and radius.

For details refer to this support article: [Border settings overview](../../write/block-settings/border.md)

**Advanced**

The **Advanced** section allows you to add CSS class(es) to the **Comment Count** block. Therefore, you can insert custom CSS styles into the block.

## Comments Link block

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/comment-link-block/; edit it into the page. -->

The Comments Link block displays a link to the comments section for the current post or page. You can customize the link text and optionally include the total number of comments. This block is most useful in single post/page templates or inside a Post Template within a Query Loop.

### Where you can use this block

-   Single posts and pages.
-   Post Template inside a Query Loop (for example, on an index or archive template).
-   The block requires post context. It does not display on non-singular pages without a current post.

### Add the Comments Link block

1.  Open a post, page, or template in the editor.
2.  Place your cursor where you want the link to appear (for example, under the post title or byline).
3.  Click the + Block Inserter and search for “Comments Link,” then select it.
    -   Tip: You can also type /comments-link on a new line to insert it quickly.

### Behavior notes

-   If comments are disabled for the current post or the post is password-protected, the link may be hidden or disabled depending on your discussion settings.
-   When used in a Query Loop, each Comments Link points to the corresponding post’s comments section.

### Block toolbar

The block toolbar displays several tools used to customize each block. When you select the **Comments Link** block, it will show the block toolbar that contains the following tools:

#### Transform to

Click on the “Transform” button to convert the *Comments Link* block into a “Group”, “Columns”, “Details”, or “Comments Count” block.

![The Transform button in the Comment Link Block is selected and shows options to transform to Group, Columns, Details, or Comments count](https://wordpress.org/documentation/files/2025/11/comment-link-transform-1.png)

#### Drag icon

To drag and drop the block to a new location, click and hold the rectangle of dots, then drag it to the new location. The blue separator line indicates where the block will be placed. Release the left mouse button when you find the new location to place the block.

![The Drag and Drop icon is clicked and highlighted.](https://wordpress.org/documentation/files/2025/11/comment-link-drag-1.png)

#### Move arrows

The up and down arrow icons can be used to move the block up and down on the page.

![The Up and Down arrows of the Comments Link block is selected.](https://wordpress.org/documentation/files/2025/11/comment-link-move-arrows.png)

> [!NOTE]
> Detailed instructions on moving a block within the editor can be found [here](../../write/blocks/move-blocks.md)

#### Align

Use the change alignment tool to align the *Comments link* block. Choose one of the following options:

-   **Align text left**
-   **Align text right**
-   **Align text center**

![The Alignment Tool of the Comment Link block is selected and highlighted.](https://wordpress.org/documentation/files/2025/11/comment-link-align.png)

### Block settings

WordPress blocks have specific configuration options in the block settings panel. To access the **Comments Link** block settings panel, click the **Settings** button at the top-right corner of the WordPress editor. Alternatively, click the **More options** or three dots icon in the **Comments Link** block toolbar and select **Show more settings**.

**Color**

The **Comments Link** block provides Color settings options to change the text and background colors.

For details refer to this support article: [Color settings overview](../../write/block-settings/color.md)

**Typography**

The **Comments Link** block provides typography settings to change the font family, appearance, line height, letter spacing, decoration, letter case, and font size.

For details refer to this support article: [Typography settings overview](../../write/block-settings/typography.md)

**Dimensions**

The **Comments Link** block provides dimension settings options to add padding and margin.

For details refer to this support article: [Dimension settings overview](../../write/block-settings/dimensions.md)

**Border**

The **Comments Link** block provides border settings options to add border color, width, and radius.

For details refer to this support article: [Border settings overview](../../write/block-settings/border.md)

**Advanced**

The **Advanced** section allows you to add CSS class(es) to the **Comments Link** block. Therefore, you can insert custom CSS styles into the block.
