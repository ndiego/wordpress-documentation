---
title: Gallery
description: "Show several images together with the Gallery block, and choose its columns, image sizes and links."
type: reference
slug: gallery-block
redirect_from:
  - /documentation/article/gallery-block/
  - /documentation/article/the-wordpress-gallery-block-editor/
  - /documentation/article/the-wordpress-gallery-classic-editor/
---

# Gallery

The Gallery block allows you to easily add multiple photos and automatically arrange them in a gallery. You can control the number of columns and the size of the images in the gallery.

## Add a Gallery block

Add the Gallery block to a page by clicking on the **Block Inserter +** icon and selecting the Gallery block.

![Image showing the Quick Inserter with gallery in the search field.](https://wordpress.org/documentation/files/2021/12/Screen-Shot-2021-12-21-at-4.09.44-PM.png)

*Adding the Gallery block*

Alternatively, you can type `/gallery` and press Enter.

![Image of the slash inserter with the gallery block listed.](https://wordpress.org/documentation/files/2021/12/Screen-Shot-2021-12-21-at-4.08.17-PM.png)

_Adding the Gallery block with */gallery* shortcut_

> [!NOTE]
> [Detailed instructions on adding blocks](../../write/blocks/add-a-block.md)

### Use attached images

[Watch the video on VideoPress](https://videopress.com/v/Pj4XiuBr)

Select the **Use attached images** button after adding a gallery block to create a dynamic gallery that will automatically add images that are attached to your post. If you add a new image, the gallery will automatically update.

![Gallery initial state with Upload, Media Library and Use Attached images options.](https://wordpress.org/documentation/files/2019/03/Screenshot-2026-09-18-at-2.42.27-PM.png)

If you wish to convert the dynamic gallery to a regular gallery, you can use the Detach button from the block toolbar or the Detach Gallery button in the block settings sidebar.

![Detach button in Block toolbar for Dynamic Gallery](https://wordpress.org/documentation/files/2019/03/Screenshot-2026-09-18-at-2.47.10-PM.png)

> [!NOTE]
> [Learn more about image and file attachments.](../../write/media/README.md)

## Block toolbar

Each block has its own block-specific controls that allow you to manipulate the block right in the editor.

### For the entire block

The Gallery block has a toolbar for the individual images as well as a toolbar for the entire Gallery block.

![Block editor toolbar showing image tools and formatting options, with a Replace button on the right.](https://wordpress.org/documentation/files/2019/03/2026-02-15_12-20.jpg)

*Block editor toolbar showing image tools and formatting options, with a Replace button on the right.*

#### Transform to

![Transform to** menu showing the blocks the Gallery block can convert to.](https://wordpress.org/documentation/files/2019/03/gallery-block-transform-options.png)

_**Transform to** menu showing the blocks the Gallery block can convert to._

The buttons in **Transform to** let you change the block to an Image, Columns, Group, Details, or Grid block.

Choosing Image converts each gallery image into its own Image block. Choosing Grid places those Image blocks inside a Grid block.

#### Block moving handles

![Moving a gallery block](https://wordpress.org/documentation/files/2022/08/Screen-Shot-2022-08-20-at-10.16.08-AM.png)

The block-moving handles allow you to move the block up and down the editor. Use the grab handle (six dots button) to drag and drop the Gallery block and place it anywhere on the page. Alternatively, click on the up and down arrows to move the block up or down by one step.

> [!NOTE]
> [Get more information about moving a block within the editor.](../../write/blocks/move-blocks.md)

#### Change alignment

![Gallery block alignment and width](https://wordpress.org/documentation/files/2022/08/Screen-Shot-2022-08-20-at-10.16.28-AM.png)

-   **Align left** – Align the block to the left
-   **Align center** – Center the block
-   **Align right** – Align the block to the right
-   **Wide width** – Increase the width of the block beyond the content size
-   **Full width** – Extend the block to cover the full width of the screen

**Wide width** and **Full width** alignment options are only available if they are enabled in your theme.

#### Link

You can choose link options to apply to all images in your gallery.

![Gallery link options.](https://wordpress.org/documentation/files/2019/03/Screenshot-2026-03-06-at-3.05.21-PM-1024x408.jpg)

-   **Link images to attachment pages** – Selecting this option will link the image to its WordPress media [attachment](image.md#step-4--attachment-details) page.
    -   This is an informational page about your image, which includes the image, the caption, the image description, and a comment field.
-   **Link images to media files** – Selecting this option will link the image to the image file in the original size in a new browser window.
-   **Enlarge on click** – Selecting this option lets visitors open gallery images in a larger view, also known as a lightbox, without leaving the page. Visitors will be able to move forward and backward through each image in the lightbox.
-   **None**: Selecting this option will not link the image to anything.

#### Caption for the gallery

You can add a caption to the whole gallery by clicking on the **Caption** icon on the block settings toolbar.

![Adding a caption to the gallery block](https://wordpress.org/documentation/files/2019/03/gallery-caption.png)

*Adding a caption to the Gallery block*

You can add captions for individual images using the caption button in each image block’s toolbar.

![Caption text on top of an individual image in the Gallery block](https://wordpress.org/documentation/files/2019/03/gallery-block-individual-image-caption.png)

*Caption text on an individual image in the Gallery block*

#### Adding images

The **Add** button in the Gallery block lets you add images to the gallery. You have two ways of doing this: **Open Media Library** and **Upload**.

![Adding images to the gallery block](https://wordpress.org/documentation/files/2022/08/Screen-Shot-2022-08-20-at-10.16.45-AM.png)

*Adding images to the Gallery block*

The Upload option allows you to upload a new image or multiple images to the Gallery block. It will add them to your Media Library at the same time. The Media Library option lets you choose from images you uploaded to your Media Library earlier.

You can also drag and drop multiple images at the same time from your explorer or finder window into the Gallery block.

Alternatively, you can open the main inserter panel on the editor and open the media tab. Then, you can drag and drop images from the media library and Openverse into the Gallery block.

#### More options

These controls give you the option to copy, duplicate, and edit your block as HTML.

> [!NOTE]
> [Read about these and other settings.](../../write/blocks/more-options.md)

### For an individual image

Each image inside a Gallery block is an Image block. When you select an individual image, the toolbar shows Image block controls for that image, such as link, crop, replace, and more. These settings affect only the selected image, not the entire Gallery block.

![Individual image block toolbar with the 'Select parent block: Gallery' button in focus](https://wordpress.org/documentation/files/2019/03/gallery-block-toolbar-select-gallery-button.png)

If you want to return to the full Gallery block settings, use the **Select parent block: Gallery** button in the toolbar. This lets you edit gallery-wide settings, such as columns, image resolution, cropping, and layout.

> [!NOTE]
> Some options such as **Add text over image** or **Align** may not be present or may not work as expected when an Image block is inside a Gallery block.

#### Move images

Once you have added images to your Gallery block, you can change the order of the images in the gallery. Click on an image, and in the block toolbar use the **move left** and **move right** arrow handles or the grab handle (six dots button) to arrange the images as you like.

[Watch the video](https://wordpress.org/documentation/files/2019/03/gallery-block-moving-images.mp4)

> [!NOTE]
> [Learn about additional block settings on the Image block page.](image.md)

## Block settings

As well as the options in the block toolbar, every block has specific options in the editor sidebar. If you don’t see the sidebar, click on the **Settings** button next to the **Save/Publish** button.

![Settings button highlighted in the block editor next to the Save button.](https://wordpress.org/documentation/files/2019/03/block-settings-7-0.png)

The Gallery block settings panel is divided into three tabs – **List View**, **Settings**, and **Styles**.

### List View tab

The **List View** tab allows you to drag and drop images within the gallery to reorder them. When hovering over an image in List View, click on the More options (three dots) button for additional block controls like copy, duplicate, hide, delete, and more.

[Watch the video on VideoPress](https://videopress.com/v/oHegtvHd)

> [!NOTE]
> [Learn about the More options menu](../../write/blocks/more-options.md).

### Settings tab

The Gallery block includes the following settings:

![Gallery block settings including column slider, resolution dropdown, and image controls.](https://wordpress.org/documentation/files/2026/09/gallery-block-settings-e1779421075171-edited.png)

#### Columns

Use the Columns setting to choose how many columns appear in the gallery.

You can choose 1 to 8 columns, but only up to the number of images in the gallery. For example, a gallery with 4 images can have up to 4 columns. Add more images to use more columns, up to the maximum of 8.

To change the number of columns, either:

-   Enter a number in the field
-   Use the slider to increase or decrease the number of columns

#### Resolution

You can also choose the **Resolution** of your image with options that may include **Full Size**, **Large**, **Medium** and **Thumbnail** depending on what your theme supports and the size of the originally uploaded image.

> [!NOTE]
> [Learn more about image size and quality.](../../write/media/image-sizes.md)

#### Crop images to fit

You can select whether or not you’d like all of your images to be cropped in your Gallery block.

This option is useful if you have images of varying sizes and shapes. Cropping them will make the images in each row of the gallery the same size. Toggle this option on and off to see which way you’d prefer.

#### Open images in a new tab

If any [Link options](#link) are enabled for the gallery, you can choose whether you want images to open in a new browser tab window when the visitor clicks on them.

#### Randomize order

This button will juggle the order of images in the Gallery block.

> [!NOTE]
> In the block editor, the images will still appear in the order they were added. But on the published post, they will be displayed in a random order.

#### Aspect ratio

This setting changes the aspect ratio of all of the images in the Gallery to one consistent ratio.

[Watch the video](https://wordpress.org/documentation/files/2019/03/gallery-block-aspect-ratio.mp4)

#### Navigation button type

If **Enlarge on click** is enabled in [Link options](#link) for the Gallery, you can choose the style of the lightbox’s previous, next, and close navigation buttons.

-   **Icon**: only icons display
-   **Text**: only text labels display
-   **Both**: both icons and text labels display

[Watch the video](https://wordpress.org/documentation/files/2019/03/gallery-block-lightbox-navigation-buttons.mp4)

#### Advanced settings

The Gallery block provides the following Advanced settings options: HTML Anchor, Additional CSS Class(es), Additional CSS, and Styles.

> [!NOTE]
> [Learn more about advanced settings.](../../write/block-settings/advanced.md)

### Styles tab

![](https://wordpress.org/documentation/files/2019/03/gallery-block-styles.png)

#### Color

The Gallery block provides color settings options to change the background for the block

> [!NOTE]
> For details, refer to this support article: [Color settings overview.](../../write/block-settings/color.md)

#### Dimensions

The Gallery block provides dimension settings options to add padding and margin.

> [!NOTE]
> For details, refer to this support article: [Dimension settings overview.](../../write/block-settings/dimensions.md)

#### Border

The Gallery block provides border settings options to add border color, width, and radius.

> [!NOTE]
> For details, refer to this support article: [Border settings overview.](../../write/block-settings/border.md)

## The WordPress gallery (block editor)

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/the-wordpress-gallery-block-editor/; edit it into the page. -->

### Overview

Image galleries are a great way to share groups of pictures on your WordPress site. The **Create Gallery** feature of the WordPress media uploader allows you to add a simple image gallery to pages or posts on your site.

![A published gallery with captions](https://wordpress.org/documentation/files/2018/11/published-gallery.png)

*End result of published gallery*

This article introduces how to add an image gallery using the media library.

### Adding image gallery using media library

Here’s how to add an image gallery step-by-step, using the media uploader:

> [!NOTE]
> Before adding a gallery, you should be comfortable using the* Add media *feature and the media uploader to [add images to your media library and place them into posts](image.md#classic-editor).

#### Step 1 – Place your cursor

A gallery can go anywhere on a page or post – by itself on a blank page, or above, below, or in the midst of text. Start by placing your cursor where you want the gallery to appear – if it’s in between blocks of text, like in the photo example below, consider adding a return and placing your cursor on a new line so there’s space above and below.

![Place cursor where gallery should be.](https://wordpress.org/documentation/files/2019/05/Screenshot_24.png)

*Place cursor where gallery should be*

#### Step 2 – Select the Gallery block

Once you’ve placed your cursor where you want your image gallery to appear, click on the **+** symbol on the left of the cursor and select Gallery.

![](https://wordpress.org/documentation/files/2019/05/Gutenberg-Gallery-Block-1.png)

#### Step 3 – Add and/or select the images you want to include

You can add or select the images you want to include in your image gallery by choosing from either of the following options in the center of the media uploader window:

-   **Upload Files:** Upload the images you want to use from your computer by dragging them into the upload area. You can add more than one image, and they will be automatically grouped together as an image gallery.
-   **Media Library:** Select from previously uploaded images in the media library by clicking on the ones you wish to add to the gallery. You will see a checkbox next to your selections.

![Select the images you want to add from the media gallery.](https://wordpress.org/documentation/files/2019/05/Screenshot_25.png)

*Select the images you want to add from the media gallery*

> [!NOTE]
> You can create an image gallery using directly images from your computer simply by switching back and forth between the Upload Files and Media Library options.

As you upload and/or select images, you will see your selection confirmed on the Insert Media screen by checkboxes at the top corner of each thumbnail. Also, a row of thumbnails appears at the bottom of the window to help you keep track of all the images you’ve selected. When you are happy with your selection, click the **Create a new gallery** button.

![](https://wordpress.org/documentation/files/2019/05/Screenshot_25.png)

#### Step 4 – Edit your gallery

On the Edit Gallery page, you can do the following things before inserting the gallery you have created into your page or post:

-   **Rearrange your images:** Drag and Drop image thumbnails to rearrange the order of images in your gallery.
-   **Reverse Order:** Reverses the order of the images in your gallery.
-   **Add image descriptions:** Add descriptions to your images (optional) which appear as image captions below each thumbnail in the gallery.
-   **Remove images:** Hover over a thumbnail and click on the “X” to remove any of the images you previously selected.
-   **Add more images:** Click on the “Add to Gallery” link in the left-hand sidebar and add or select the images you want to include in your image gallery by choosing from either “Upload Files” or “Media Library” tabs.
-   **Cancel Gallery:** Click on the “Cancel Gallery” link from the actions on the left to exit the Edit Gallery page and cancel your image gallery.

![](https://wordpress.org/documentation/files/2019/05/Screenshot_26.png)

After inserting your gallery, you also have several Gallery Settings available in the right pane of your editor screen:

![](https://wordpress.org/documentation/files/2019/05/Screenshot_27.png)

-   **Links To:** Controls whether the gallery thumbnails (on the published page/post) link to the image attachment page or directly to the source image file itself.
-   **Columns:** Set the number of columns you would like to have in your gallery. 3 Columns is the default settings, which is ideal for most sites.

#### Editing existing galleries

Within the visual editor, the image gallery is displayed as a series of thumbnail images.

![Gallery in WordPress editor.](https://wordpress.org/documentation/files/2019/05/Screenshot_29.png)

*Gallery in WordPress editor*

When you click any area of the image gallery, icon buttons appear top of the area. At any time, you can edit the images or settings of your gallery by clicking on the Edit button. You can remove the image gallery at any time by clicking on the Remove button.

![Edit image to edit.](https://wordpress.org/documentation/files/2019/05/Screenshot_31.png)

*Edit image to edit*

### Resources & gallery plugins

-   [Gallery Plugins](https://wordpress.org/plugins/search/gallery)

## Classic Editor

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/the-wordpress-gallery-classic-editor/; edit it into the page. -->

> [!NOTE]
> This document is for the Classic Editor. If you are using the block-editor on your site, the [Gallery Block is documented on this page](gallery.md).

### Overview

Image galleries are a great way to share groups of pictures on your WordPress site. The **Create Gallery** feature of the WordPress media uploader allows you to add a simple image gallery to pages or posts on your site.

![A published gallery with captions](https://wordpress.org/documentation/files/2018/11/published-gallery.png)

*End result of published gallery*

This article introduces how to add an image gallery using the media library, and explains gallery shortcode which will be generated and embedded into the post or page.

### Adding image gallery using media library

Here’s how to add an image gallery step-by-step, using the media uploader:

> [!NOTE]
> Before adding a gallery, you should be comfortable using the* Add media *feature and the media uploader to [add images to your media library and place them into posts](image.md#classic-editor).

#### Step 1 – Place your cursor

A gallery can go anywhere on a page or post – by itself on a blank page, or above, below, or in the midst of text. Start by placing your cursor where you want the gallery to appear – if it’s in between blocks of text, like in the photo example below, consider adding a return and placing your cursor on a new line so there’s space above and below.

![Placing cursor where gallery should be](https://wordpress.org/documentation/files/2018/11/gallery-place-cursor.png)

*Place cursor where gallery should be*

#### Step 2 – Click the add media button

Once you’ve placed your cursor where you want your image gallery to appear, click on the Add Media button (located left above the editing window) to launch the media uploader interface. In the resulting popup window, select the ‘Create a Gallery’ option from the list of actions on the left.

![Clicking the add media button above editor](https://wordpress.org/documentation/files/2018/11/gallery-add-media-button.png)

*Click “Add Media” button*

#### Step 3 – Add and/or select the images you want to include

You can add or select the images you want to include in your image gallery by choosing from either of the following options in the center of the media uploader window:

-   **Upload Files:** Upload the images you want to use from your computer by dragging them into the upload area. You can add more than one image, and they will be automatically grouped together as an image gallery.
-   **Media Library:** Select from previously uploaded images in the media library by clicking on the ones you wish to add to the gallery. You will see a checkbox next to your selections.

![Drag and drop files into media library to create gallery](https://wordpress.org/documentation/files/2018/11/drag-to-start-gallery.png)

*Drag and drop multiple files to Media Library*

> [!NOTE]
> You can create an image gallery using any combination of new images and previously uploaded images simply by switching back and forth between the Upload Files and Media Library tabs.

As you upload and/or select images, you will see your selection confirmed on the Insert Media screen by check boxes at the top corner of each thumbnail. Also, a row of thumbnails appears at the bottom of the window to help you keep track of all the images you’ve selected. When you are happy with your selection, click the **Create a new gallery** button.

![Media Library selecting images to appear in gallery](https://wordpress.org/documentation/files/2018/11/create-gallery.png)

*Selecting images to appear in gallery*

#### Step 4 – Edit your gallery

On the Edit Gallery page, you can do the following things before inserting the gallery you have created into your page or post:

-   **Rearrange your images:** Drag and Drop image thumbnails to rearrange the order of images in your gallery.
-   **Reverse Order:** Reverses the order of the images in your gallery.
-   **Add image descriptions:** Add descriptions to your images (optional) which appear as image captions below each thumbnail in the gallery.
-   **Remove images:** Hover over a thumbnail and click on the “X” to remove any of the images you previously selected.
-   **Add more images:** Click on the “Add to Gallery” link in the left hand sidebar and add or select the images you want to include in your image gallery by choosing from either “Upload Files” or “Media Library” tabs.
-   **Cancel Gallery:** Click on the “Cancel Gallery” link from the actions on the left to exit the Edit Gallery page and cancel your image gallery.

![Dragging images in Media Library to organize gallery](https://wordpress.org/documentation/files/2018/11/edit-gallery-drag.png)

*Drag and drop images to organize gallery*

Before inserting your gallery, you also have several Gallery Settings available in a pane on the right to control the following:

-   **Links To:** Controls whether the gallery thumbnails (on the published page/post) link to the image attachment page or directly to the source image file itself.
-   **Columns:** Set the number of columns you would like to have in your gallery. 3 Columns is the default settings, which is ideal for most sites.
-   **Random Order:** Enables your gallery to display your image thumbnails in a random order each time they are viewed on the site.
-   **Size:** Changes each image size in gallery. Available options are Thumbnail, Media, Large and Full Size.

#### Editing existing galleries

Within the visual editor, the image gallery is displayed as a series of thumbnail images.

![Gallery in the WordPress TinyMCE editor](https://wordpress.org/documentation/files/2018/11/gallery-in-visual-editor.png)

*Gallery in WordPress editor*

When you click any area of the image gallery, icon buttons appear top of the area. At any time, you can edit the images or settings of your gallery by clicking on the Edit button. You can remove the image gallery at any time by clicking on the Remove button.

![Click pencil icon to edit image](https://wordpress.org/documentation/files/2018/11/edit-gallery.png)

*Edit image to edit*

### Gallery shortcode

Above steps generates Gallery shortcode with image ids and other options, and embedded into the Post or Page, like this:

```json
[gallery ids="729,732,731,720"]
```

You can specify options direct to this shortcode.

#### Usage

There are several options that may be specified using this syntax:

```json
[gallery option1="value1" option2="value2"]
```

#### Options

The following basic options are supported:

**orderby**

Specifies how to sort the displayed thumbnails. The default is “menu_order.”

Options:

-   **menu_order** – You can reorder the images in the Gallery tab of the Add Media pop-up.
-   **title** – Order images in the Media Library, based on the image title.
-   **post_date** – Sort images by date/time.
-   **rand** – Order images randomly.
-   **ID**

**order**

Specifies the sort order used to display thumbnails. ASC or DESC. For example, to sort by ID, use DESC:

```json
[gallery order="DESC" orderby="ID"]
```

**columns**

Specifies the number of columns. The gallery will include a break tag at the end of each row, and calculate the column width as appropriate. The default value is 3. If columns is set to 0, no row breaks will be included. For example, to display a 4 column gallery:

```json
[gallery columns="4"]
```

**id**

Specifies the post ID. The gallery will display images which are attached to that post. The default behavior, if no ID is specified, is to display images attached to the current post. For example, to display images attached to post 123:

```json
[gallery id="123"]
```

**size**

Specifies the image size to use for the thumbnail display. Valid values include “thumbnail,” “medium,” “large,” “full” or any other additional image size that was registered with  [add_image_size()](https://developer.wordpress.org/reference/functions/add_image_size). The default value is “thumbnail.” The size of the images for “thumbnail,” “medium,” and “large” can be configured in the WordPress admin panel under Settings > Media. For example, to display a gallery of medium sized images:

```json
[gallery size="medium"]
```

Some advanced options include:

**itemtag**

The name of the XHTML tag used to enclose each item in the gallery. The default is “dl.”

**icontag**

The name of the XHTML tag used to enclose each thumbnail icon in the gallery. The default is “dt.”

**captiontag**

The name of the XHTML tag used to enclose each caption. The default is “dd.” For example, to change the gallery markup to use div, span and p tags:

```json
[gallery itemtag="div" icontag="span" captiontag="p"]
```

**link**

Specify where you want the image to link. The default value links to the attachment’s permalink. Options:

-   **file** – Link directly to the image file.
-   **none** – No link.

```json
[gallery link="file"]
```

**include**

Comma-separated attachment IDs that include only the images from these attachments.

```json
[gallery include="23,39,45"]
```

**exclude**

Comma-separated attachment IDs that exclude specific images from these attachments. Please note that **include** and **exclude** cannot be used together.

```json
[gallery exclude="21,32,43"]
```

### Resources & gallery plugins

-   [Gallery Plugins](https://wordpress.org/plugins/search/gallery)
