---
title: Block Directory
description: "The Block Directory is a new way for block editor users to discover, test, and install new blocks on their website."
type: guide
order: 80
redirect_from:
  - /documentation/article/block-directory/
---

# Block Directory

The Block Directory is a new way for block editor users to discover, test, and install new blocks on their website. It is available to content creators who have the capability to install and activate plugins.

## How to use the Block Directory

1.  Select the “+” icon at the top, left-hand corner of the editor to open the Block Inserter.

![The editor with icons displayed at the top, above the page content](https://wordpress.org/documentation/files/2020/07/block-directory-inserter-0-6.7.jpg)

2.  Type a keyword in the search field of the Inserter, like “team” or “staff”.

WordPress first searches the current site for the block named “team” or “staff”. If it doesn’t find a block, it searches in the Block Directory, which is a special corner of the WordPress plugin repository, where single block plugins are available.

If the search finds blocks, they will be displayed in the inserter, including a preview section. Decide which block to use and select it to add it to the page.

![Blocks found in the block directory](https://wordpress.org/documentation/files/2020/07/block-directory-inserter-1-6.7.jpg)

In the background, the single-block plugin is installed and activated, and the user can continue creating the page.

3.  If no blocks are found in either case, a [link to the Block Editor Handbook](https://github.com/WordPress/gutenberg/blob/trunk/docs/README.md) is displayed with details on how to create your own blocks.

![No results in the Block Directory, which displays a notice about creating your own block](https://wordpress.org/documentation/files/2020/07/block-directory-inserter-2-6.7.jpg)

4.  If the first choice doesn’t suit your needs, you can go back to the search and select a different one that will also be installed.

### Examples of tested single-block plugins

-   [Block for Apple Maps](https://wordpress.org/plugins/maps-block-apple/),
-   [Event block](https://wordpress.org/plugins/event/),
-   [User Profile Block](https://wordpress.org/plugins/user-profile-block/)

## How to uninstall the block

Blocks from the Block Directory are installed as a plugin. To uninstall a block that you installed from the Block Directory, go to the Plugins screen. Find the block plugin and deactivate and delete it to uninstall the block.

![How to uninstall the block](https://wordpress.org/documentation/files/2023/02/Screenshot-2023-02-09-at-4.42.00-PM.png)

## How to reinstall a block

If a previously used block is no longer available on the site, you have the option to reinstall it.

When the page is first loaded, a search will be done in the background to check if that block is still available. If it has been found, an **Install [block name]** button will be displayed in place of the missing block on the page. Select the button to automatically reinstall the missing block.

![Examples: Missing block with “Install \[block name\]" and “Keep as HTML” options.](https://wordpress.org/documentation/files/2020/07/block-directory-reinstall-6.3.png)

A **Keep as HTML** button will also be displayed, or it will be the only button present if no matching block was found when the page loaded.

You can choose that option instead. It lets you convert the content into a custom HTML block, so you still have a chance to use the content of the block you had before.

You could also choose to remove the missing block and choose another one from the Block Directory using the steps outlined above.

## Video showing how the Block Directory works

[Watch the video on VideoPress](https://videopress.com/v/RpDhdRqj)

https://videopress.com/v/RpDhdRqj

This video shows you how the Block Directory works. It starts at the 3:00 time stamp. Start it at the beginning if you are new to the block editor and need a refresher.

*On* [Learn.WordPress.org](https://learn.wordpress.org/), *contributors started creating workshop videos for self-study and [scheduled discussion groups online](https://www.meetup.com/learn-wordpress-discussions). Check it out.*

## Resource links

-   [Introduction to the Block Directory (Video)](https://learn.wordpress.org/workshop/intro-to-the-block-directory/)
-   [Series: Introduction to Publishing with the Block Editor](https://learn.wordpress.org/workshop/intro-to-publishing-with-the-block-editor/)
-   [Single Block Plugins available through the Block Directory](https://wordpress.org/plugins/browse/block/)
-   [Proposed Block Directory guidelines](https://make.wordpress.org/plugins/2020/07/22/proposed-block-directory-guidelines/)
