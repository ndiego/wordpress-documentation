---
title: Columns
description: "The Columns block allows you to insert text, media, and other types of content into columns. When used one after another, the columns can create a grid effect."
type: reference
slug: columns-block
redirect_from:
  - /documentation/article/columns-block/
---

# Columns

The Columns block allows you to insert text, media, and other types of content into columns. When used one after another, the columns can create a grid effect.

You can type `/columns` in the editor and hit enter in a new paragraph block to add one quickly.

![columns block selected in the popover that appears after typing /columns in the editor.](https://wordpress.org/documentation/files/2019/03/add-columns-block.png)

> [!NOTE]
> [Detailed instructions on adding blocks](../../write/blocks/add-a-block.md)

Once you add the Columns block, you can choose a variation to start with. You can change the number or add more columns later in the block settings. If you select **Skip** at the bottom, you will start with 50/50 columns by default.

![Columns block setup options showing preset column layouts, like 100, 50/50, and 33/66](https://wordpress.org/documentation/files/2019/03/columns-block-default-variations.png)

*Column variations you can start with*

## Adding and removing columns

It is possible to add or remove columns in a few different ways:

1.  Hover between two existing columns and select the **Add column** **+** button to add another column in that spot.
2.  Use the Columns slider or number field in the block settings sidebar to change the number of columns.

Remove a column by selecting the individual Column block, then choosing **Delete** from the **More** options menu (three dots) in [List View](../../write/blocks/list-view.md) or the block toolbar.

[Watch the video](https://wordpress.org/documentation/files/2026/05/columns-block-add-and-remove.mp4)

## Adding content to columns

Once you have defined the number of columns, you can add content to each column. The amazing thing about the columns block is that you can add other blocks into each of the columns.

For instance, you can use the Columns block as the structure and add an image, heading, and paragraph block to create a grid of services.

![Columns block selected in the editor display three service items from a design and development agency, each using an image, heading, and short description.](https://wordpress.org/documentation/files/2026/05/columns-block-3cols-services.jpg)

Or you can use the [Cover block](../media/cover.md) inside a Columns block to create a row of visual cards.

![Columns block selected in the editor with Cover block cards in a two column layout describing vacation rentals, each with a background image, heading, description, and button.](https://wordpress.org/documentation/files/2026/05/columns-block-2cols-cover.jpg)

You can also use the Columns block with [Buttons block](buttons.md) to show a small set of related actions side by side. To make the buttons the same width, add one Button block to each column and set each button to 100% width.

![Columns block selected in the editor showing a three-column layout with three equal-width buttons.](https://wordpress.org/documentation/files/2026/05/columns-block-3cols-equal-width-buttons.png)

## Block toolbar

Most blocks have their own block-specific controls that allow you to manipulate the block right in the editor.

The Columns block shows the following buttons:

-   Transform to
-   Move controls
-   Change alignment
-   Change vertical alignment
-   More options

![Columns block toolbar](https://wordpress.org/documentation/files/2023/05/image17.png)

### Transform to

Select the Columns icon at the left side of the block toolbar. This opens the **Transform to** menu, where you can change the Columns block to the [Group](group/README.md), [Details](../text/details.md), or [Grid](group/grid.md) block.

When you transform the Columns block to a Grid block, the content in each column is preserved.

![Transform the Columns block into the Group, Details, or Grid block](https://wordpress.org/documentation/files/2019/03/column-block-transform-to-options.png)

A common reason to place a Columns block inside a Group block is to create a section with its own background color and spacing. To ungroup the blocks, select **Ungroup** in the **Transform to** menu.

![WordPress editor showing a selected Group block with a yellow background containing five columns, each with a book cover image.](https://wordpress.org/documentation/files/2026/05/columns-blocks-group-background.jpg)

### Moving handles

![The block moving tools on the columns block toolbar](https://wordpress.org/documentation/files/2023/05/image11.png)

The dotted icons can be used to drag and drop a block to the place of your choosing. The up and down arrow icons can be used to shift a block up and down in your document.

> [!NOTE]
> [Get more information about moving a block within the editor.](../../write/blocks/move-blocks.md)

### Change alignment

![The alignment tools on the columns block toolbar](https://wordpress.org/documentation/files/2023/05/image6-1.png)

Use the Change alignment button from the toolbar to modify the width of the Columns block.  Select the button and pick one of the following alignment options:

-   **None** –  Leaves the block the current size.
-   **Wide width** – Increase the width of the block beyond the content size.
-   **Full width** – Extend the block to cover the full width of the screen.

### Change vertical alignment

![Dropdown of vertical alignment options in the Columns block toolbar.](https://wordpress.org/documentation/files/2026/05/columns-block-vertical-alignment-controls.png)

Use the Change vertical alignment button to control how content lines up inside the columns. This is most noticeable when columns have different amounts of content. Select the button and pick one of the following options:

-   **Align top** – Make the block vertically aligned top.
-   **Align middle** – Make the block vertically aligned middle.
-   **Align bottom** – Make the block vertically aligned bottom.

Inner Column blocks include vertical alignment options too. **Stretch to fill** is the default behavior and makes the column fill the available height of the Columns block.

![Dropdown of vertical alignment options in the individual Column block toolbar.](https://wordpress.org/documentation/files/2026/05/inner-column-block-stretch-to-fill-alignment.png)

This option is useful when columns have borders or background colors and you want them to appear equal in height.

[Watch the video](https://wordpress.org/documentation/files/2026/05/column-block-stretch-to-fill-cards.mp4)

### More options

The controls give you additional features to customize the block, like the ability to duplicate, copy, rename, hide, and more.

> [!NOTE]
> [Read about these and other settings.](../../write/blocks/more-options.md)

## Block settings

Every block has specific options in the editor sidebar in addition to the options found in the block toolbar. If you do not see the sidebar, click on the **Settings** button next to the **Save/Publish** button.

![Settings button highlighted in the block editor next to the Save button.](https://wordpress.org/documentation/files/2019/03/block-settings-7-0.png)

The Columns block settings panel is divided into two tabs – **Settings** and **Styles**. It contains the following sections:

### Settings tabs

Open the **Settings** tab to change the number of columns from 1 to 6. Use the up and down arrows, drag the slider, or type a number in the input field.

![Column number settings](https://wordpress.org/documentation/files/2019/03/columns-block-settings-column-slider.png)

The **Stack on mobile** setting is enabled by default. When enabled, columns stack vertically on smaller screens instead of remaining side by side. This helps layouts stay readable and responsive across screen sizes.

### Styles tab

Open the **Styles** tab to change color, typography, dimensions, and border options. Your theme may also include style choices you can apply to the Columns block – these options vary by theme.

![Styles settings in the WordPress Twenty Twenty-Five theme.](https://wordpress.org/documentation/files/2019/03/columns-block-styles-tab.png)

*Styles settings in the WordPress Twenty Twenty-Five theme.*

#### Color

With Color settings, you can change the color of the text in your block, the color of links, and the background color of your block. For the Columns block, this means that you can style each column individually or both columns for consistency.

> [!NOTE]
> [Learn more about changing colors](../../write/block-settings/color.md).

#### Typography

The Columns block provides typography settings to change the font family, appearance, line height, letter spacing, decoration, letter case, and font size.

> [!NOTE]
> For details, refer to this support article: [Typography settings overview](../../write/block-settings/typography.md)

#### Dimensions

The Columns block provides dimension settings options to add padding, margin, and block spacing.

> [!NOTE]
> For details, refer to this support article: [Dimension settings overview](../../write/block-settings/dimensions.md)

#### Border & shadow

The Columns block provides border settings options to add border color, style, width, and radius.

> [!NOTE]
> For details, refer to this support article: [Border settings overview](../../write/block-settings/border.md)

#### Advanced

The Columns block provides the following Advanced settings options: HTML Anchor, Additional CSS Class(es), Additional CSS, and Styles.

> [!NOTE]
> [Learn more about advanced settings](../../write/block-settings/advanced.md)

#### Column width

![Column width settings](https://wordpress.org/documentation/files/2023/05/image16.png)

To change the width of one column, select the individual Column block and adjust the width in the block settings. You can use [px, %, em, rem, vw, or vh](../../write/block-settings/typography.md#the-difference-between-px-em-rem--vw-and-vh-units) values. To make it easier to find and select the Column Block, it’s recommended to use [List View](../../write/blocks/list-view.md).

> [!NOTE]
> For details, refer to this support article: [Layout settings overview](../../write/block-settings/layout.md)
