---
title: Media settings
description: "Set the sizes WordPress creates for uploaded images and how uploads are organized on the Settings > Media screen."
type: reference
order: 50
slug: media-settings
redirect_from:
  - /documentation/article/settings-media-screen/
---

# Media settings

The **Settings Media Screen** controls the various settings related to images and other media that are used in writing posts and pages.

![](https://wordpress.org/documentation/files/2018/11/media-setting.png)

You will need php-gd (GD graphics library) installed on your server to use this feature.

## Media settings

### Image sizes

The sizes listed below determine the maximum dimensions in pixels to use when inserting an image into the body of a post.

-   **Thumbnail size** – Enter the **Width** and **Height**
    -   **Crop thumbnail to exact dimensions (normally thumbnails are proportional)** – checkbox
-   **Medium size** – Enter the **Max Width** and **Max Height**
-   **Large size** – Enter the **Max Width** and **Max Height**

### Uploading files

Default settings used for during the media upload process when writing a post.

-   **Organize my uploads into month- and year-based folders** – Check this box if you wish to organize your uploads into folders based on the year and the month of the upload. As of 3.5, wp-content/uploads is the default path setting for the uploads folder. Assuming this is your path setting, if you check this box, a file uploaded in June of 2018 would be placed into the wp-content/uploads/2018/06 folder. Note: At the time of the actual upload, WordPress will automatically create the folders, such as wp-content/uploads/2018 and wp-content/uploads/2018/06, as long as your wp-content folder is writeable.

### Save changes

Click the **Save Changes** button to ensure any changes you have made to your Settings are saved to your database. Once you click the button, a confirmation text box will appear at the top of the page telling you your settings have been saved.

## Further reading

-   [Image Size and Quality](../../write/media/image-sizes.md)
-   [Media Add New Screen](../../write/media/add-media.md)
-   [Media library screen](../../write/media/README.md)
-   [Edit Media](../../write/media/edit-media.md)
-   [Use Images](../../write/media/README.md)
-   [Use image and file attachments](../../write/media/README.md)
-   [Inserting Images into Posts and Pages (Block Editor)](../../blocks/media/image.md)
-   [Inserting Images into Posts and Pages (Classic Editor)](../../blocks/media/image.md#classic-editor)
