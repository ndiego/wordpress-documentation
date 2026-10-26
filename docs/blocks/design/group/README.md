---
title: Group
description: "Put blocks together in a Group block so you can style, move and lay them out as one unit."
type: reference
slug: group-block
redirect_from:
  - /documentation/article/group-block/
---

# Group

The *Group block* allows you to group different blocks together and customize them to your liking, including setting custom background colors, spacing, and more.

![Group block with columns, heading, paragraph, image and button blocks.](https://wordpress.org/documentation/files/2020/09/group_block_layout_with_columns.png)

*Example of a Group block with columns, heading, paragraph, image and button blocks.*

## Adding a Group block

To add a *Group block*, click on the **Block Inserter** icon.

![screenshot of the menu that pops up when adding the group block with the inserter. The options shown are group, buttons, accordion, grid, row, and stack.](https://wordpress.org/documentation/files/2020/09/group-block_block-inserter_7-1.png)

You can also type `/group` and hit enter in a new paragraph block to add one quickly. **Accordion, Buttons, Row, Stack and Grid are also types of Group blocks**, they just have a different layout style by default.

![screenshot of the menu that pops up when typing /group. The options shown are group, accordion, buttons, row, stack and grid.](https://wordpress.org/documentation/files/2020/09/group-block_add_7-1.png)

### Block variations

When the Group block is created, you will find different variations to choose from: Group, Stack, Row, and Grid.

![menu showing the layout variations for the group block. These are group, stack, row or grid](https://wordpress.org/documentation/files/2020/09/group-settings-variations.png)

### Converting multiple blocks to a Group block

You can create a group by selecting multiple blocks in several ways. One way is to drag your mouse to highlight the blocks you want to group. Alternatively, you can hold down the “Shift” key and use the arrow keys or click on each block to select multiple blocks. Once the blocks are selected, group icons will appear. You can click on these icons or use the “More Options” button to combine the blocks into a single group. For a quicker method, use the keyboard shortcut (Ctrl + G on Windows or ⌘ Command + G on Mac) to instantly group the selected blocks. Check the video below for a demonstration.

[Watch the video](https://wordpress.org/documentation/files/2023/03/group-block-convert-to-group-1.mp4)

> [!NOTE]
> [Detailed instructions on adding blocks](../../../write/blocks/add-a-block.md)

## Block toolbar

Most blocks have their own block-specific controls that allow you to manipulate the block right in the editor. The Group block offers standard block options as well as full-width and wide-width options, if the theme supports these alignment styles.

The Group block shows three buttons in addition to the “Group” block icon.

-   Moving handles
-   Change alignment
-   Align items justification
-   More options

### Moving handles

![moving handles](https://wordpress.org/documentation/files/2020/09/group-block-move.png)

The up and down arrow icons can be used to shift a block up and down in your document.

> [!NOTE]
> See [Move blocks](../../../write/blocks/move-blocks.md) for detailed instructions.

### Change alignment

![group block alignment options: none, wide and full width](https://wordpress.org/documentation/files/2020/09/group-block-alignemt.png)

**None –** Is the default width, the same as the main content.

**Wide width** – Increase the width of the post beyond the content size.

**Full width** – Extend the block to cover the full width of the screen, if supported by your site’s theme.

### Items align justification

![Items justification inside the group block: left, center and right.](https://wordpress.org/documentation/files/2020/09/group-block_justify-tems.png)

The three options to justify the items inside the Group block are **left**, **center** and **right**.

### More options

These controls give you the option to copy, duplicate, and edit your block as HTML.

> [!NOTE]
> [Read about these and other settings.](../../../write/blocks/more-options.md)

## Editing the block

The nice thing about the Group block is that you can add any other blocks inside the group block and create a layout of your own. To add blocks to the Group block, click on the inserter icon inside the Group block.

![Adding a new block inside an existing group block](https://wordpress.org/documentation/files/2023/03/group-block-add-block.png)

## Adding content

Inside the Group block, you can add a columns block, cover block or any other available block to create the layout of your choice.

![Adding content to the group block](https://wordpress.org/documentation/files/2020/09/group_block_layout_with_columns.png)

The Group block shown here has columns, heading, paragraph, image and button blocks.

Note that since the Group block has the ability to embed other blocks, if you click specifically on one of the blocks, the settings in the sidebar will change according to the block you added to the Group block. For example, if you added an image inside the Group block, when you click on the image the sidebar will display the options from the Image block settings.

Every block has specific options in the editor sidebar in addition to the options found in the block toolbar. If you do not see the sidebar, simply click the ‘**Settings**‘ icon next to the Publish/Update button.

## Group block settings

### Alignment

There are four alignment options for the Group block:

-   Default
-   Row (Horizontal)
-   Stack (Vertical)
-   Grid

![Group block](https://wordpress.org/documentation/files/2020/09/group-block_group-alignment.png)

![Row block](https://wordpress.org/documentation/files/2020/09/group-block_row-alignment.png)

![Stack brock](https://wordpress.org/documentation/files/2020/09/group-block_stack-alignment.png)

![Grid block](https://wordpress.org/documentation/files/2020/09/group-block_grid_alignment.png)

Once you choose one of the other group blocks, like Row, Stack or Grid, the settings change to those of each block.

### Styles

You can modify the block styles by choosing the **Default** or **Style 1** to **Style 5** buttons in the Styles settings panel. Hover over the **Default** or **Style** buttons to get a preview of the styles.

The style options may vary based on your theme.

### Typography

This option allows you to set the font, color, size, line height and other typography-related settings for the block.

> [!NOTE]
> [Learn more about typography settings.](../../../write/block-settings/typography.md)

### Background

The Background settings allow you to customize the appearance of supported blocks using background images, colors, and gradients.

> [!NOTE]
> For details, refer to the [Background Settings Overview](../../../write/block-settings/background.md).

### Layout

This is an advanced option that allows you to add custom content widths to the overall Group block for all blocks assigned to the center or wide columns. In many cases, you won’t need to use this option. When you toggle this option on, it allows the Group block to inherit the options set by your theme. When it’s toggled off, you can customize to your liking.

> [!NOTE]
> [This article provides details about layout settings.](../../../write/block-settings/layout.md)

### Dimensions

The option to control block spacing and padding is enabled for the block.

> [!NOTE]
> [Learn more about dimension controls.](../../../write/block-settings/dimensions.md)

### Border & shadow

This option allows you to set a border around the block, including the color, the width, radius, and the style of the border.

> [!NOTE]
> [Learn more about Border & Shadow settings.](../../../write/block-settings/border.md)

### Elements

The Elements settings allow you to customize the appearance of links, buttons, headings, and heading levels H1 through H6.

### Position

![Position: Sticky](https://wordpress.org/documentation/files/2023/03/group-block-settings-sticky.png)

The “Position” group setting allows you make a group block stick to the top of the viewport instead of scrolling, as seen in the demo below:

[Watch the video](https://wordpress.org/documentation/files/2023/03/group-block-settings-sticky-demo-1.mp4)

*video showing the sticky Group block*

Please note that **only “top level” Group blocks can be set as sticky**. If a Group block is embedded inside any other block, the “Position” setting will not be available in the settings.

### Advanced

The block provides the following Advanced settings options: HTML Anchor, Additional CSS Class(es), Additional CSS, HTML Element, Styles, and Allowed blocks.

> [!NOTE]
> [Learn more about advanced settings](../../../write/block-settings/advanced.md)
