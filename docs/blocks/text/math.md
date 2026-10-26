---
title: Math
description: The Math block lets you display mathematical notation in your content. You can enter formulas using LaTeX or MathML and show them as a standalone block or inline within text.
type: reference
slug: math-block
redirect_from:
  - /documentation/article/math-block/
---

# Math

The Math block lets you display mathematical notation in your content. You can enter formulas using LaTeX or MathML and show them as a standalone block or inline within text. Inline math formatting is also available in rich text fields such as Paragraphs, Headings, Lists, and Table cells.

## Requirements

-   WordPress 6.9 or later.

## Add a Math block

1.  Open a post or page in the editor.
2.  Place your cursor where you want the formula to appear.
3.  Open the Block Inserter (+) in the top toolbar, search for “Math,” and select the Math block.

You can also type `/math` in the block editor and press Enter.

![Math block is highlighted in the modal that appears when typing the command forward slash and "math" in the block editor](https://wordpress.org/documentation/files/2025/12/math-block-inserter-e1778724596347.png)

> [!NOTE]
> [Read detailed instructions on adding blocks.](../../write/blocks/add-a-block.md)

## Enter a formula

![Example LaTeX formula](https://wordpress.org/documentation/files/2025/12/math-block-example-equation-e1778728517841.png)

*Example output of a LaTeX formula using the Math block*

1.  Click inside the Math block to edit.
2.  Type or paste your formula using LaTeX (for example, `\frac{a}{b}, E=mc^2, \int_0^\infty e^{-x} dx`) or valid MathML markup.
3.  Exit the block to preview the rendered result in the editor.

## Add inline math inside text

1.  Add or select a text block (for example, Paragraph, Heading, List item, or Table cell).
2.  Select the portion of text where the formula should appear.
3.  Select the **More** icon (down arrow) in the the block toolbar, and then **Math**.
    -   ![Math selected in the dropdown under the More options in the toolbar](https://wordpress.org/documentation/files/2025/12/math-block-add-inline-math.png)
4.  In the field that appears, paste or type your LaTeX or MathML.
5.  The expression will render inline with your text like this example: $\frac{a}{b}, E=mc^2, \int_0^\infty e^{-x} dx$

## Block toolbar

![Math block toolbar including transform, move, and more option controls.](https://wordpress.org/documentation/files/2025/12/math-block-toolbar-editor.png)

*Math block toolbar*

Each block toolbar comes with different options that let you customize or modify the block in the editor. To view the Math block toolbar, select the block and it will show a list of toolbar options.

The Math block has the following options:

-   Transform to
-   Moving handles
-   More options

### Transform to

![Math block transform dropdown menu showing Columns, Group, and Details blocks.](https://wordpress.org/documentation/files/2025/12/math-block-transform-to-1.png)

The Transform to tool allows you to convert the Math block into the following blocks:

-   Columns
-   Group
-   Details

### Moving handles

![Move controls in the block toolbar.](https://wordpress.org/documentation/files/2025/12/math-block-moving-handles.png)

*Move controls in the block toolbar*

To move a Math block, select the block in the editor. Use the Move up or Move down arrows in the block toolbar to move it one position at a time.

You can also click and hold the Drag icon, which looks like six dots, to drag the block to a new location.

> [!NOTE]
> [Get more information about moving a block within the editor.](../../write/blocks/move-blocks.md)

### More options

These controls give you the option to copy, duplicate, remove, lock, and other standard actions.

> [!NOTE]
> [Read about these and other settings.](../../write/blocks/more-options.md)

## Block settings

![Settings icon highlighted next to the Save/Publish button in the top toolbar in the block editor.](https://wordpress.org/documentation/files/2026/05/block-settings-7-0-1.png)

*Settings icon in the top toolbar of the editor*

In addition to the block toolbar, each block has specific options in the Settings sidebar on the right side of the editor. To view Math block settings, select the Math block. If the sidebar is closed, click the **Settings button** next to the Save/Publish button in the top toolbar.

![Block settings panel open in the Math block.](https://wordpress.org/documentation/files/2025/12/math-block-example-customizations.png)

*Block settings panel open in the Math block*

Here is a list of the Math block settings options:

### Color

With the Color settings, you can customize content in the Math block by applying text and background colors. You can also add gradients as a background color. The color selections vary depending on your active theme.

> [!NOTE]
> For details, refer to this support article: [Color Settings overview](../../write/block-settings/color.md)

### Typography

The Typography settings enable you to customize the font size of content in the Math block. For example, you may want to increase the font size of a complex math equation so it’s more easily readable.

> [!NOTE]
> For details, refer to this support article: [Typography settings overview](../../write/block-settings/typography.md)

### Dimensions

The Math block provides dimension settings options to add padding and margin to control the space around the block, and the space between the block and its edges.

> [!NOTE]
> For details, refer to this support article: [Dimension settings overview](../../write/block-settings/dimensions.md)

### Borders

The Math block provides border settings options to add border color, width, and radius.

> [!NOTE]
> For details, refer to this support article: [Border & Shadow settings overview](../../write/block-settings/border.md)

### Advanced

The Math block provides the following Advanced settings options: HTML Anchor, Additional CSS Class(es), Additional CSS, and Styles.

> [!NOTE]
> [Learn more about advanced settings](../../write/block-settings/advanced.md)

## Demo

[Watch the video](https://wordpress.org/documentation/files/2025/11/6-9-math-i3.mp4)

## Tips

-   Use block display for large equations or multi-line expressions; use inline display for short formulas inside sentences.
-   Keep LaTeX simple and standard. Complex packages or custom macros may not be supported.
-   Prefer MathML output for improved accessibility where possible; include explanatory text nearby for readers using assistive technologies.
-   Save commonly used formulas as Patterns to reuse across posts.

## Frequently asked questions

**Which syntax should I use?**

LaTeX is often easiest to type; MathML is a web standard that supports accessibility. The block supports both.

**Can I number equations or add references?**

WordPress doesn’t include built-in equation numbering. You can add labels in surrounding text or use patterns to keep numbering consistent.

**Can I use inline math everywhere text appears?**

Inline math works in most rich text fields, including Paragraphs, Headings, Lists, and Table cells.

## Troubleshooting

**My formula isn’t rendering:**

-   Check for typos or unmatched braces in LaTeX.
-   If using MathML, ensure tags are valid and properly nested.
-   Switch the input format in settings to match what you typed (LaTeX or MathML).

**Characters are being escaped or removed:**

-   Paste plain text (not rich text) to avoid hidden formatting.
-   In MathML, angle brackets and entity references must be valid HTML; ensure your content isn’t stripped by another plugin.
