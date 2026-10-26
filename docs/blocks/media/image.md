---
title: Image
description: Use the Image block to easily add an image to your page.
type: reference
slug: image-block
redirect_from:
  - /documentation/article/image-block/
  - /documentation/article/inserting-images-into-posts-and-pages-block-editor/
  - /documentation/article/inserting-images-into-posts-and-pages-classic/
---

# Image

Use the Image block to easily add an image to your page.

## Add an Image block

To add the Image block, click the **+ Block Inserter** button in the top-left corner of the editor. Search for the Image block and click on the block to add it to the page.

Alternatively, you can quickly add the Image block by typing `/image` and pressing **Enter**.

![Image block selected from the block list modal that appears when typing /image in the editor.](https://wordpress.org/documentation/files/2019/03/image-block-add-image.png)

> [!NOTE]
> [Detailed instructions on adding blocks](../../write/blocks/add-a-block.md)

### Initial options

After adding the Image block, you have a few options to choose to get started.

-   **Upload** an image or video from your device.
-   Choose **Media Library** to select an existing image or video on your site.
-   Select **Insert from URL** to add an image from a specific web address.

![Image block options when first adding to the page to upload, add from media library, or insert an image from a URL.](https://wordpress.org/documentation/files/2019/03/image-block-add-image-options.png)

#### Insert from URL

After choosing **Insert from URL**, follow the steps below:

-   Paste the image URL and press **Enter** to add the image to the page.
-   Select **Upload to Media Library** (up arrow button) in the [block toolbar](#block-toolbar) to save a copy of the image to your site’s Media Library.
-   If you don’t upload the image to your Media Library, the image may stop displaying later if the original file is moved, deleted, or no longer shared.

> [!NOTE]
> This option may not work with every image or website. Some websites block images from being embedded or copied this way. Only use images you have permission to use.

[Watch the video](https://wordpress.org/documentation/files/2019/03/image-block-insert-from-url.mp4)

### Additional ways to add images

There are also additional ways to add images:

#### Drag/drop images

You can drag and drop images from your computer onto a blank page or inside an empty Paragraph block.

#### Media tab

You can select images from the **Media** tab in the WordPress block inserter. If your theme supports [Openverse](https://openverse.org), you can also select free-to-use images from the WordPress Openverse library. If Openverse is not available, the option will not appear in the inserter.

1.  Click the + **Block Inserter** in the top-left corner.
2.  Select the **Media** tab.
3.  Select an image from the Media Library to add to your page, or Openverse if the option is available.
4.  To replace an existing image on the page, drag an image from the **Media tab** onto the existing image.

After adding an Openverse image to your page, WordPress automatically saves it to your Media Library.

[Watch the video](https://wordpress.org/documentation/files/2019/03/image-block-insert-via-media-tab.mp4)

#### Copy images from a document

You can also copy and paste images into the editor from other tools, such as Microsoft Word or Google Docs. WordPress may automatically upload copied images to your site’s Media Library. To confirm, select the image and check whether the block toolbar shows **Upload to Media Library** (up arrow button). If it does, select it to save a copy of the image to prevent it from breaking in the future.

![Upload to Media Library button highlighted in the Image block toolbar](https://wordpress.org/documentation/files/2019/03/image-block-upload-to-media-library.png)

_**Upload to Media Library** button highlighted in the block toolbar_

### Update image details

After uploading or selecting an image, customize the image details in your [Media Library](../../write/media/README.md), such as the Title, Caption, Alt Text, and Description. This data is helpful for SEO, accessibility, and helps you search for files in your media library.

If an image includes a caption, WordPress automatically displays it. You can hide or show image captions in the [block toolbar](#block-toolbar).

### Resizing images

After adding an image to the editor, you can resize and align it to better fit the surrounding content.

To resize an image:

-   Click on the image to reveal the draggable resize handles.
-   Click on the resize handles and drag the image to your desired size.

[Watch the video](https://wordpress.org/documentation/files/2023/12/resize-image.mp4)

*Resize an image by dragging its handles.*

> [!NOTE]
> [Detailed instructions on adding blocks](../../write/blocks/add-a-block.md)

## Block toolbar

![Block toolbar over an image taken from on the moon during the Apollo mission](https://wordpress.org/documentation/files/2019/03/Screenshot-2026-03-02-at-4.15.23-PM-1024x505.png)

Each block has its own block-specific controls that allow you to manipulate the block right in the editor. The Image block contains the following options:

-   Transform to
-   Move controls
-   Change alignment
-   Apply duotone filter
-   Link
-   Crop
-   Add text over image
-   Add/remove caption
-   Replace
-   More options

### Transform to

![Dropdown of Transform to in the Image block toolbar including options to transform to Columns, Group, Gallery and more.](https://wordpress.org/documentation/files/2019/03/image-block-transform-to-selected.png)

*Transform to button highlighted in the block toolbar showing the list of transform options.*

The **Transform to** tool allows you to convert the Image block into Columns, Group, Gallery, Cover, Details, File, or the Media & Text block. You can apply any style options your theme makes available for the block.

### Move controls

![Move control buttons in the image block toolbar side-by-side](https://wordpress.org/documentation/files/2019/03/image-block-move-controls.png)

Click the grab handle (six dots button) to move the block to a new location on the page. A blue separator line shows where WordPress will place the block.

Use the up and down arrow buttons to move the block up and down on the page

> [!NOTE]
> [Get more information about moving a block within the editor.](../../write/blocks/move-blocks.md)

### Change alignment

![Dropdown of alignment options in the image block toolbar](https://wordpress.org/documentation/files/2019/03/image-block-change-alignment.png)

*Alignment button selected showing the list of options.*

Use the **Change alignment** tool to modify the alignment of the Image block. Select the tool and pick one of the following alignment options:

-   **None** – Leaves the block the current size
-   **Wide width** – Increase the width of the post beyond the content size
-   **Full width** – Extend the block to cover the full width of the screen
-   **Align left** – Align the block to the left
-   **Align center** – Center the block
-   **Align right** – Align the block to the right

**Wide width** and **Full width** only display if your theme supports these width options.

#### Wrap text around images

You can wrap text around an image by aligning the image to the left or right.

1.  Add the image directly above the paragraph.
2.  Select the image.
3.  [Resize the image](#resizing-images) to be smaller.
4.  In the block toolbar, select **Align left** or **Align right**.
5.  The paragraph text will wrap around the image.

For best results, use this option with smaller images. Large images can make the text hard to read, especially on mobile devices.

[Watch the video](https://wordpress.org/documentation/files/2019/03/image-block-wrap-text-around-image.mp4)

### Duotone

The block toolbar provides a quick action for applying duotone colors to images, which will recolor your image. Available color options vary by theme.

[Watch the video](https://wordpress.org/documentation/files/2019/03/image-block-duotone-filter-block-toolbar.mp4)

### Link

![Dropdown of image link options in the block toolbar](https://wordpress.org/documentation/files/2019/03/image-block-link-settings.png)

*Link button highlighted in the block toolbar showing list of link of options.*

You can choose link options to apply to an image. Options include the following:

-   **Search field** – Paste a URL or search for a page, post, or other content on your site to link the image.
-   **Link images to image file** – Link image to the image file in a new browser window.
-   **Link images to attachment page** – Link the image to its WordPress media [attachment](#step-4--attachment-details) page.
-   **Enlarge on click** – Lets visitors open the image in a larger view, known as a lightbox, without leaving the page to see more detail.

### Crop

Use the **Crop** button in the block toolbar to open the Media Editor and make detailed edits to an image directly in the editor. The Media Editor has two tabs: **Crop** and **Details**.

#### Crop tab

-   Drag the handles on the image to make a freeform selection, or choose a preset from **Aspect ratio** (Free, Square – 1:1, and more).
-   Use **Zoom** (+/−) to magnify the image for finer adjustments before selecting your crop.
-   Use **Rotate** to turn the image left or right, or drag the ruler beneath the image to straighten it by degree.
-   Use **Flip** to mirror the image horizontally or vertically.
-   Crop handles snap to the source image’s pixels, so selections line up precisely.

#### Details tab

Select **Details** to update the image’s metadata without leaving the editor:

-   **Alt text** – describe the image for accessibility, or leave empty if the image is decorative.
-   **Caption** and **Description**.
-   Read-only file info: date added, author, file name, file type, file size, and dimensions.

Select **Save** to apply your changes, or **Cancel** to discard them and close the Media Editor.

> [!NOTE]
> WordPress saves the edited version as a new image file, so the original image remains available in your Media Library.

[Watch the video on VideoPress](https://videopress.com/v/jymoNgwu)

https://videopress.com/v/jymoNgwu

#### Undo changes

While editing, use **Reset**, **Undo**, and **Redo** at the bottom of the media editor.

![Notification with action to undo changes to the image block](https://wordpress.org/documentation/files/2019/03/image-block-undo-crop-changes.png)

*Undo action notice at the bottom of the block editor after applying image crop changes.*

After applying changes to an image, you can revert them using the Undo option in the action notice or the Undo button in the top-left of the block editor next to the **+ Block Inserter** button.

### Add text over image

Use the **Add text over image** button to change an Image block into a [Cover block](cover.md). This lets you place text on top of the image.

![Icon of the letter A inside of a partial square to indicate adding text over an image feature in the block toolbar](https://wordpress.org/documentation/files/2019/03/image-block-add-text-over-image.png)

_**Add text over image** button highlighted in the block toolbar_

When you select Add text over image, the Image block immediately changes into a Cover block with placeholder text. Replace the placeholder text with your own text.

![Image block converted to a Cover block with the text "Type / to choose a block" over the image.](https://wordpress.org/documentation/files/2019/03/image-block-converted-to-cover.png)

Use this option when the image is decorative or when the text can remain readable over the image. For better readability, adjust the overlay color or opacity in the Cover block settings.

### Captions

Click the **Add caption** button in the block toolbar to show or hide a caption for an individual image.

-   Select the **Add caption** button in the block toolbar.
-   Select the Image block and enter your caption in the space below the image.
-   To hide the caption, select the **Add caption** button again.

![Caption text displays below the image and includes formatting options](https://wordpress.org/documentation/files/2019/03/image-block-add-caption.png)

*Example of the Caption button selected in the block toolbar with an image caption added to the block.*

### Replace

Use the **Replace** button to select a new image from the Media Library, **Upload** a new image, or **Reset** the image block back to it’s initial setup options.

![Dropdown of image block replace options](https://wordpress.org/documentation/files/2019/03/image-block-replace-option.png)

*Replace button selected in the block toolbar showing a list of options.*

### More options

The **More options** menu (three dots) includes common block actions, such as copy, duplicate, lock, and edit as HTML.

The Image block also includes a **Set as featured image** option. Use this option to set the selected image as the featured image for the post or page.

!['Set as featured image' option highlighted in the image block toolbar](https://wordpress.org/documentation/files/2026/08/image-block-set-featured-image.png)

_**Set as featured image** action in the More options dropdown menu._

> [!NOTE]
> [Read about the More options menu and its settings](../../write/blocks/more-options.md).

## Block settings

Every block has specific options in the editor sidebar in addition to the options found in the block toolbar. If you don’t see the sidebar, click on the **Settings** button next to the Save/Publish button.

![Settings icon highlighted next to the Save/Publish button in the top toolbar in the block editor.](https://wordpress.org/documentation/files/2026/05/block-settings-7-0-1.png)

The Image block settings panel is divided into three tabs – **Content**, **Settings**, and **Styles**.

### Content tab

#### Media

Select the image thumbnail or file name under **Media** to upload a new image, choose one from the Media Library, or reset the image. You can also use the **Media options** menu (three dots) next to Media to reset the image or alternative text.

![Media option dropdown when selecting on the dropdown in the Content tab of the block settings.](https://wordpress.org/documentation/files/2019/03/image-block-media-options.png)

#### Alternative text

Add meaningful alternative text to an image or mark it as decorative. The [Describe the purpose of the image](https://www.w3.org/WAI/tutorials/images/decision-tree/) link points to a decision tree that helps users determine what alt text, if any, should be used for images in different accessibility contexts.

![Alternative text added describing a skyscraper](https://wordpress.org/documentation/files/2026/08/image-block-alternative-text-field.png)

If you add alt text in the block settings, that edit only applies to the image on that specific page or post. Adding alternative text for an image in the [Media Library](../../write/media/README.md) sets the default alt text when you insert the image elsewhere.

#### Mark as decorative

Mark an image as decorative only when it does not add meaningful information or functionality, so assistive technologies can ignore it instead of announcing unnecessary or distracting text.

![Mark has decorative checkbox to hide an image from screen readers](https://wordpress.org/documentation/files/2026/08/image-block-mark-as-decorative.png)

### Settings tab

#### Resolution

You can also choose the **Resolution** of your image with options that may include Full Size, Large, Medium and Thumbnail depending on what your theme supports and the size of the originally uploaded image.

![Dropdown selection for image resolution](https://wordpress.org/documentation/files/2026/08/image-block-resolution.png)

> [!NOTE]
> [Learn more about image size and quality](../../write/media/image-sizes.md)

#### Advanced

The Image block provides the following Advanced settings options: HTML Anchor, Additional CSS Class(es), Additional CSS, Title attribute, and Styles.

Use the **Title** attribute to describe the role of this image on the page, however many devices and browsers don’t display this text.

![Title attribute field for images](https://wordpress.org/documentation/files/2026/08/image-block-title-attribute.png)

> [!NOTE]
> [Learn more about advanced settings](../../write/block-settings/advanced.md)

### Styles tab

The **Styles** section appears if your theme includes custom image style options. The available styles may vary, but common options include **Default** and **Rounded**. The Rounded style adds rounded corners to the image.

![Image block style settings including dimensions, duotone, aspect ratio, and more.](https://wordpress.org/documentation/files/2019/03/image-block-style-settings-1.png)

#### Filters

You can create a filter effect on images without actually changing the original image. The **Duotone** filter option allows you to add this filter color to your block content from the block toolbar.

> [!NOTE]
> [Read more about the filter options](../../write/block-settings/filters.md).

#### Dimensions

The Image block provides dimension settings options to change margin size.

> [!NOTE]
> For details refer to this support article: [Dimension settings overview](../../write/block-settings/dimensions.md)

#### Aspect ratio

Use **Aspect ratio** to change the shape of the image on the page, such as square, portrait, or landscape. Some aspect ratios may visually crop the image to fit the selected shape. This only changes how the image appears on the page. It does not edit the original image file.

Choosing an aspect ratio may show additional settings, including **Width** and **Height**, **Scale**, and the **Focal point** picker.

[Watch the video](https://wordpress.org/documentation/files/2019/03/image-block-set-aspect-ratio.mov)

#### Width and height

Use **Width** and **Height** to set the display size of the image.

In most cases, leave these fields set to **Auto**. To resize the image, set the **Width** value and let the height adjust automatically. Use percentages only when you want the image to scale relative to its container.

Avoid setting a fixed height unless the image needs to fit a specific design, because it can make the image harder to control across different screen sizes.

[Watch the video](https://wordpress.org/documentation/files/2019/03/image-block-change-width.mov)

#### Scale

Use **Scale** to control how the image fits inside the selected aspect ratio.

-   **Cover** – Fills the entire image area. Parts of the image may be cropped so there are no empty areas.
-   **Contain** – Shows the full image. This may leave empty space around the image if its shape does not match the selected aspect ratio.

[Watch the video](https://wordpress.org/documentation/files/2019/03/image-block-scale-options.mov)

#### Focal point

Use **Focal point** to choose which part of the image stays in view when the image has an [aspect ratio](#aspect-ratio) set. This setting is most useful when **Scale** is set to **Cover**, because Cover may crop part of the image to fill the selected aspect ratio.

[Watch the video](https://wordpress.org/documentation/files/2019/03/image-block-focal-point.mp4)

#### Border & shadow

The Image block provides border settings options to add border color, width, radius and shadow.

> [!NOTE]
> For details refer to this support article: [Border & Shadow Settings overview](../../write/block-settings/border.md)

## Classic Editor

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/inserting-images-into-posts-and-pages-classic/; edit it into the page. -->

### Overview

When creating or editing a WordPress page or blog post, you can easily add images at any time using the WordPress Media Uploader tool. Here’s how to add an image, step-by-step, using the media uploader:

### Step 1 – Placing your cursor

![Cursor at beginning of a paragraph](https://wordpress.org/documentation/files/2018/11/add-image-insert-cursor.png)

*Placing cursor where the image should appear*

In order to add an image to your page or post, you must first insert your cursor in the place in the text where you want the image to appear. By placing your cursor within your text, you can add images inline with your content. You can also place your cursor on a blank line if you want the image to appear by itself instead.

*Tip: It’s a good idea to **place your cursor on the left margin of your text**, even if you want the image to appear on the right. That’s because there is a special setting called Alignment that allows you to control whether the image appears on the right or the left side of the text. It even controls how text flows around the image automatically.*

### Step 2 – Click the add media button

Once you’ve placed your cursor on the line where you want your image to appear, click on the Add Media button to launch the media uploader interface, and then select the Insert Media option from the list of actions in the left side of the media uploader window.

![Add Media button circled](https://wordpress.org/documentation/files/2018/11/add-media-button.png)

*“Add Media” button above editor*

### Step 3 – Add or select your image

You can add or select the image you want to add to your page or post by choosing from either of the following options in the center of the media uploader window:

-   **Upload Files:** Upload the image you want to use from your computer by dragging it into the upload area.
-   **Media Library:** Select from any previously uploaded images in the media library by clicking on the one you wish to add to your page or post.

![](https://wordpress.org/documentation/files/2018/11/media-uploader.png)

Once you have selected or uploaded the image you want to add, You will see a checkbox next to the thumbnail confirming your selection, and see information about it displayed in the Attachment Details pane on the right hand side of the media uploader interface.

### Step 4 – Attachment details

![Attachment details pane with: title, caption, alt text, and description](https://wordpress.org/documentation/files/2018/11/attachement-details.png)

*Attachment details*

The **Attachment Details** pane displays a small un-cropped thumbnail of the image, as well as important information such as the filename, date uploaded, and image dimensions in pixels.

There are also action links that allow you to **Edit Image**, which takes you to the page, or to **Delete Permanently** to remove the image from your site.

In addition, you can edit the following media information:

-   **Title:** The title of this media.
-   **Caption:** The caption for this image. The text you enter here will be displayed below the image.
-   **Alternate Text:** Enter the Alt text for the image, e.g. “The Mona Lisa” to describe the media.
-   **Description:** A description for this particular media.

For more information on these media settings, see the [Edit Media](../../write/media/edit-media.md) page.

### Step 5 – Attachment display settings

![Attachment display settings: alignment, link to, and size](https://wordpress.org/documentation/files/2018/11/attachment-display-settings.png)

*Attachment display settings*

The **Attachment Display Settings** pane controls how the image is displayed when viewed on the site.

You have options to set how you would like the image aligned on the page (in relation to the text and margins) and what the link behavior of the image will be, In addition you can set what size image you would like to display on your page.

#### Image alignment

The **Alignment** setting allows you to determine where you would like the image to appear in your content area and how it interacts with any text on the page. You have the following image alignment options to choose from:

-   **Left:** Aligns the image on the left hand margin, and any text that is on the page wraps (or flows) around the image to the available space on the right.
-   **Right:** Aligns the image on the right hand margin, and any text that is on the page wraps (or flows) around the image to the available space on the left.
-   **Center:** Aligns the image to the center of the page, with no text displayed around it.
-   **None:** Inserts the image in to the page with no alignment

![Different image alignments](https://wordpress.org/documentation/files/2018/11/750px-image-alignment-4up.png)

*Aligning images using editor controls*

#### Image link

The Link To settings determine the URL/web address to which the image will be linked when clicked on by a visitor to your site. You can specify the following image link settings:

-   **Attachment Page:** Links your inserted image to its WordPress media attachment page.
-   **Media File:** Links your inserted image directly to the original, full-size version of the file.
-   **Custom URL:** Allows you to set a custom link URL for your inserted image to link to when clicked.
-   **None:** This setting will remove the link completely, rendering the image “un-clickable”.

#### Image size

The Size settings determine the size of the image you are adding to your site. By default WordPress creates a range of four image size for you to choose from:

-   **Thumbnail:** Displays a small thumbnail-sized version of your image on the page/post. Note, by default the Thumbnail size is a square, so some cropping of your original image may occur.
-   **Medium:** Displays a medium-sized version of your image on the page/post. This is a good size to use with Left/Right alignments, as it leaves sufficient space for legible text to either side.
-   **Large**: Displays a large-sized version of your image on the page/post. Note: WordPress will determine the width of the content column of your theme, and display the largest possible image for that space.
-   **Full Size:** Displays a full-sized version of your image on the page/post. Note: WordPress will determine the width of the content column of your theme, and display the largest possible image for that space. If your original image is larger than this column width, the full size of the image may not be displayed.

![Different image sizes](https://wordpress.org/documentation/files/2018/11/750px-image-sizes-3up.png)

*Different image sizes*

You can visit the **[Settings > Media](../../manage/settings/media.md)** section of your WordPress dashboard to customize the above image sizes.

#### Step 5 – Inserting the image

![Selecting the edit image option whenever hovering over an image](https://wordpress.org/documentation/files/2018/11/400px-re-edit-image.png)

*Edit image option*

Once you have determined your image settings, click on the blue Insert into post or Insert into the page button, to add the image to your page or post. After the image uploader window closes, you will see the image in the text editor window, including a preview of the alignment of the image, if you have specified an image alignment.

At any time, you can edit the image settings by clicking on the **Edit Image** button in the upper left hand corner. You can remove the image from your page/post by clicking on the **Remove Image** button.

### Further reading

-   [Media Add New Screen](../../write/media/add-media.md)
-   [Edit Media](../../write/media/edit-media.md)
-   [Media library screen](../../write/media/README.md)
-   [Settings Media Screen](../../manage/settings/media.md)
-   [Use Images](../../write/media/README.md)
-   [Use image and file attachments](../../write/media/README.md)
-   [Image Size and Quality](../../write/media/image-sizes.md)
-   [Inserting Images into Posts and Pages (Block Editor)](image.md)
