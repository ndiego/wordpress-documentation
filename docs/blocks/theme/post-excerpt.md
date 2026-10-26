---
title: Excerpt
description: "Show a post's excerpt in a template or a Query Loop with the Excerpt block."
type: reference
slug: post-excerpt-block
redirect_from:
  - /documentation/article/post-excerpt-block/
---

# Excerpt

Use the Excerpt block to display the excerpt of a post. This block is primarily nested inside a [query loop](query.md) block and helps to customize the appearance of the query loop.

If the post does not have an [excerpt](../../write/publish/excerpts.md#classic-editor), the Excerpt block displays the first 55 words in the post as the excerpt, followed by the characters ‘[…]’.

The block has an optional **Read More** link which will direct the website visitor to the URL of the full post. You can customize this link text to anything you like. The **Read More** link can be styled independently.

![Post excerpt block is added from template using the block inserter.](https://wordpress.org/documentation/files/2023/08/excerpt-block.png)

*Excerpt block*

To add an Excerpt block, click the **Block Inserter** icon when editing the page template. Search for the **Excerpt** block. Click on it to add the block to your page template.

![Post excerpt blocks are added inside query loop from template.](https://wordpress.org/documentation/files/2023/08/adding-post-excerpt-block.gif)

*How to add Excerpt block*

You can also type `/excerpt` and hit enter in a new paragraph block to add the Excerpt block quickly.

![The excerpt block can be added quickly by typing /excerpt.](https://wordpress.org/documentation/files/2023/08/adding-excerpt-block.png)

*Adding Excerpt block quickly*

> [!NOTE]
> [Detailed instructions on adding blocks](../../write/blocks/add-a-block.md)

## Block toolbar

To view the block toolbar, click on the block and the toolbar will be displayed.

Every block comes with unique toolbar icons. These block-specific controls allow you to manipulate the block right in the editor.

The Excerpt block shows these buttons in the block toolbar:

-   Transform to
-   Drag icon
-   Move arrows
-   Change text alignment
-   Bold
-   Italic
-   Link
-   More
-   More options

![Excerpt block toolbar shows multiple options as icon.](https://wordpress.org/documentation/files/2022/11/image12.png)

*Excerpt block toolbar*

### Transform to

![Transform to is the first option from left in Excerpt block toolbar.](https://wordpress.org/documentation/files/2022/11/image8-1.png)

*Transform options in Excerpt block*

Click on the **Transform** button to convert the Excerpt block into a **Group** block or **Columns** block.

[Watch the video](https://wordpress.org/documentation/files/2023/08/trasform-to-for-excerpt.mp4)

*Transform button from Excerpt block toolbar*

### Drag icon

![Beside transform to option, the Drag icon shows with two columns of three dots.](https://wordpress.org/documentation/files/2022/11/image3.png)

*Drag icon in the Post Excerpt block*

To drag and drop the block to a new location on the page template, click and hold the rectangle of dots, then drag it to the new location. The blue separator line indicates where the block will be placed. Release the left mouse button when you find the new location to place the block.

### Move arrows

![Next to drag icon, move arrows option shows in up and down arrow angle icon.](https://wordpress.org/documentation/files/2022/11/image1.png)

*Move arrows in the Excerpt block*

The up and down arrow icons can be used to move the block up and down on the page.

> [!NOTE]
> [Get more information about moving a block within the editor.](../../write/blocks/move-blocks.md)

### Change text alignment

![Change text alignment option shows an alignment icon beside the move arrows icon.](https://wordpress.org/documentation/files/2022/11/image4.png)

*Change text alignment in Excerpt block*

Click the **Change alignment** button in the Block toolbar to display the alignment drop-down. You can align the block text to the left, make it center-aligned or align it to the right.

### Bold

![Next to alignment, Bold option shows as B.](https://wordpress.org/documentation/files/2022/03/Next-to-alignment-Bold-option-shows-as-B.png)

The bold option will make the selected text bolded.

### Italic

![Similar to bold, an I icon represents Italic option in excerpt block toolbar.](https://wordpress.org/documentation/files/2022/03/Similar-to-bold-an-I-icon-represents-Italic-option-in-excerpt-block-toolbar.png)

The italic option will make the selected text italic.

### Link

![](https://wordpress.org/documentation/files/2022/03/add-read-more-text.png)

A field to customize the ‘Read more’ link text, the link URL is automatically set to the post.

### More

Click the down arrow button to display more styling tools for the **Read More** link.

> [!NOTE]
> [Get more information about rich text editing options](../../write/blocks/rich-text-options.md).

### Options

These controls give you the option to copy, duplicate, and edit your block as HTML.

![The three dots beside the angle arrow down icon shows list of more options.](https://wordpress.org/documentation/files/2023/08/more-options-excerpt-block-toolbar.png)

> [!NOTE]
> [Read about these and other settings.](../../write/blocks/more-options.md)

## Block settings

The block settings panel contains customization options specific to the block. To open it, select the block and click the settings icon next to the **Save** button.

![Block settings sidebar shows sidebar icon next to save or publish button.](https://wordpress.org/documentation/files/2023/07/block-settings-sidebar-2.png)

*Block settings to enable sidebar*

*If you do not see the sidebar, click the ‘sidebar’ icon next to the Publish button.* *The device icon between **Save draft** and Publish button shows the preview of the block.*

![After enabling the sidebar, the block section shows the settings and style for excerpt block.](https://wordpress.org/documentation/files/2023/08/post-excerpt-block-settings.png)

*Excerpt block settings*

### Show link on new line

Turn on **Show link on new line** button in the Block Settings to show the Excerpt Read More link on a new line instead of inline next to the excerpt text.

![Show link on new line setting appears as a toggle button to show the excerpt link on new line.](https://lh5.googleusercontent.com/QcdK0a2urmazcyYYnUOthL973dmdGlyac2TzOhcr572sUj2ZukcCyvhUZfcmh577shPDG2OzbcsSh_GP9sWixHfHRk4QDFlLpTnTLvACRKDE58luG_8_K9eAKa0RcJ1inZLCopp9)

*Show Excerpt settings on new line*

#### Max number of words

Adds the ability to control the excerpt length in a design. The default value is 55 words, to match the WordPress default length for excerpts.

![Max number of words for excerpt settings appears as a range slider.](https://wordpress.org/documentation/files/2023/08/max-number-of-words.png)

*Max number of words for excerpt*

#### Advanced

The following Advanced settings options are available: HTML Anchor, Additional CSS Class(es), Additional CSS, and Styles.

> [!NOTE]
> [Learn more about advanced settings.](../../write/block-settings/advanced.md)

### Color

The **Excerpt block** provides Color settings options to change the text, background, and link colors. Pick a color from the suggestions, or add a custom color using the color picker or by adding a color code.

> [!NOTE]
> [See this guide for more information about changing colors.](../../write/block-settings/color.md)

### Typography

The **Excerpt block** provides typography settings to change the font family, appearance, line height, letter spacing, decoration, letter case, and font size.

> [!NOTE]
> [Get more details about changing typography settings.](../../write/block-settings/typography.md)

### Dimensions

Dimension controls are used to control how groups of blocks are placed alongside one another, by changing the values for padding, margin, and other dimensions

> [!NOTE]
> [Learn more about dimension controls.](../../write/block-settings/dimensions.md)
