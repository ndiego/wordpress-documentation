---
title: Site icon
description: Set the small icon that browsers show in tabs and bookmarks for your site.
type: guide
order: 50
redirect_from:
  - /documentation/article/create-a-favicon/
  - /documentation/article/site-editor-identity/
---

# Site icon

A *favicon* (short for “favorite icon”) is an icon associated with a particular website or web page. It is generally intended to be used when you bookmark a web page. Web browsers use them in the URL bar, on tabs, and elsewhere to help identify a website visually. Favicons are also used as application icons on mobile devices.

## WordPress Version 6.5 or later

WordPress [Version 6.5](https://wordpress.org/documentation/wordpress-version/version-6-5/) moved the site icon to **General Settings**.

Follow the steps below to set **Site Icon** from General settings.

1.  Prepare the image file and upload to media library. (It must be square, having a height and width of at least 512 px. and a .png is the recommended format)
2.  Navigate to [General Settings](../../manage/settings/general.md)
3.  Click Choose a Site icon.
4.  Select image file that you prepared in the previous step.

![screenshot of the general settings tab where the site icon is added in WordPress since version 6.5](https://wordpress.org/documentation/files/2018/11/6-5-favicon-general-settings.png)

## WordPress version 4.3 to 6.4

WordPress [Version 4.3](https://wordpress.org/documentation/wordpress-version/version-4-3/) implemented a Site Icon feature that enables favicons on your web site.

When you use the Site Icon feature, you don’t need to prepare the `favicon.ico` file by yourself, or modify your template file. All you have to do is navigate to the Customize screen and specify a square image that has a height and width of at least 512 px.

Later paragraphs in this article contain instructions for manually setting up your own favicon. However, it is highly recommended that you use the Site Icon feature (a feature that is built-in to WordPress) instead.

Follow the steps below to use Site Icon to set up a favicon for your site.

1.  Prepare the image file. (It must be square, having a height and width of at least 512 px.)
2.  Navigate to [Administration Screen](../../manage/dashboard/README.md) > Appearance > Customize
3.  Click **Site Identity**
4.  Click **Select Image** (located under the **Site Icon** subheading).
5.  Click on the **Upload Files** tab, then click **Select Files** to upload the image file that you prepared in the previous step.

![customizer-siteicon](https://wordpress.org/documentation/files/2018/11/customizer-siteicon.jpg)

## Site Editor identity

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/site-editor-identity/; edit it into the page. -->

In the Site Editor, there is an Identity section where you can add and edit your Site Title, Site Tagline, Site Logo, and Site Icon at a high level without needing to edit any blocks directly. You can also edit these directly in the canvas of the Site Editor. Any changes you make in the Identity section will be reflected on the canvas and available after saving on your site.

> [!NOTE]
> The Site Editor Identity menu is **only** available when you install and activate a [Block theme](../themes/block-themes.md) on your site. You can learn about the Site Editor in this support article: [Site Editor](README.md).

### How to access the Identity section

Once you install and activate a Block theme on your site, go to **Appearance** > **Editor** to open the Site Editor. In the sidebar menu, select **Identity**:

![View of the Site Editor with the Identity section open.](https://wordpress.org/documentation/files/2026/08/Screenshot-2026-08-18-at-2.48.16-PM.png)

### Identity features

In this section, you can edit important identity related parts of your site:

-   Site Title: Displays in your site’s layout via the Site Title block.
-   Site Tagline: In a few words, explain what this site is about. Displays in your site’s layout via the Site Tagline block.
-   Site Logo: Displays in your site’s layout via the Site Logo block.
-   Site Icon: Shown in browser tabs, bookmarks, and mobile apps. It should be square and at least 512 by 512 pixels.

For the Site Logo and Site Icon, you can replace any image you add and remove it using the X when you hover. If you click on the image itself, the media library will appear and you can upload or select a different image to use:

![](https://wordpress.org/documentation/files/2026/08/Screenshot-2026-08-18-at-2.50.33-PM.png)

### Demo

[Watch the video on VideoPress](https://videopress.com/v/dvBHYnNg)

### Resource links

-   [Site Editor](README.md)
