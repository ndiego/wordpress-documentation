---
title: RSS
description: An RSS feed is a machine-readable version of the content of a blog or a website.
type: reference
slug: rss-block
redirect_from:
  - /documentation/article/rss-block/
---

# RSS

An RSS feed is a machine-readable version of the content of a blog or a website.

With the *RSS* block, you can display content from any site’s RSS feed on your website. You can choose to display the Title, Author, Date, and Excerpt for each item in the feed. You can display the items in a list or as a grid in a set number of columns.

[Watch the video](https://wordpress.org/documentation/files/2019/11/rss-overview.mp4)

Steps to embed an RSS block

1.  First, you need to know the URL of the RSS feed that you want to embed. Some websites display an orange icon ![](https://wordpress.org/documentation/files/2019/11/RSS-feed-icon.png) with the link of the feed. You can usually find this icon together with social network icons.

    Our example uses the feed of the [News](https://wordpress.org/news/) section on WordPress.org.  <https://wordpress.org/news/feed>

2.  Click the **Block Inserter** (+) icon to add an *RSS* block to your WordPress page/post. Alternatively, you can type <kbd>/rss</kbd> and hit enter in a new *paragraph block* to add one quickly.

![Adding RSS block via the WordPress slash command /rss](https://wordpress.org/documentation/files/2022/09/RSS-Feed-HelpHub-SS-1.png)

> [!NOTE]
> [Detailed instructions on adding blocks](../../write/blocks/add-a-block.md)

3.  Paste the link of the RSS feed into the text box and click on the **Use URL** button

![Enter URL here user interface for the RSS block.](https://wordpress.org/documentation/files/2022/09/RSS-Feed-HelpHub-SS-2.png)

The *RSS* block now displays the titles of the feed items.

![Display of the RSS feed.](https://wordpress.org/documentation/files/2022/09/RSS-Feed-HelpHub-SS-3.png)

If you use an URL that can’t be embedded, the block shows the message *“RSS Error: WP HTTP Error: A valid URL was not provided.”*.

![Example of a URL that cannot be used in the RSS block.](https://wordpress.org/documentation/files/2022/09/RSS-Feed-HelpHub-SS-6.png)

Use the options in the **Block Toolbar** and the controls in the **Block Settings** panel in your editor’s sidebar to fine-tune the display.

## Block toolbar

Besides the *Mover* and *Drag & Drop* handle, the Block Toolbar for the *RSS* block shows six other buttons:

-   Transform To
-   Change alignment
-   Edit RSS URL
-   List view
-   Grid view
-   More options

![Block toolbar for the RSS block.](https://wordpress.org/documentation/files/2022/09/RSS-Feed-HelpHub-SS-4-1.png)

### Transform to

You can transform the **RSS block** into **Columns, Details**, or a **Group** block to better suit your layout and design preferences:

-   **Group** – Wrap the RSS block in a Group to gain access to additional layout and styling options, such as background color, spacing, and borders.
-   **Columns** – Organize the RSS feed into multiple columns for a more structured, grid-like layout.
-   **Details** – Use the Details block to wrap the RSS content inside a collapsible section, helping manage long or dense feeds.

![Transform options for the RSS block.](https://wordpress.org/documentation/files/2019/11/rss-transforms.png)

### Change alignment

-   **Align left** – Make the block left-aligned.
-   **Align center** – Make the block alignment centered.
-   **Align right** – Make the block right-aligned.
-   **Wide width** – Increase the width of the block beyond the content size.
-   **Full width** – Extend the block to cover the full width of the screen.

![Change alignment options for RSS block.](https://wordpress.org/documentation/files/2022/09/RSS-Feed-HelpHub-SS-7.png)

The “Wide width” and “Full width” alignment settings must be enabled by your WordPress theme.

### Edit RSS URL

Via the edit URL, you can change the RSS feed URL in the block. Overwrite the existing URL and click on the **Use URL** button.

![Edit RSS Feed URL in the block.](https://wordpress.org/documentation/files/2022/09/RSS-Feed-HelpHub-SS-2.png)

### List view

The **List view** option displays the feed items in an unordered list. Use the Block settings controls to customize the **List view**.

![List view for the RSS block.](https://wordpress.org/documentation/files/2022/09/RSS-Feed-HelpHub-SS-8.png)

### Grid view

Display the feed items in a grid. Use the Block settings controls to adjust the number of columns and the other display options.

![Grid view for the RSS block.](https://wordpress.org/documentation/files/2022/09/RSS-Feed-HelpHub-SS-9.png)

### More options

These controls give you the option to copy, duplicate, and edit your block as HTML.

> [!NOTE]
> [Detailed instructions on adding blocks](../../write/blocks/add-a-block.md)

## Block settings

Every block has specific options in the editor sidebar in addition to the options found in the block toolbar. If you do not see the sidebar, simply click the ‘cog’ icon.

![Cog icon to display the Block sidebar](https://wordpress.org/documentation/files/2022/06/Screen-Shot-2022-06-23-at-9.39.34-AM.png)

![Block settings for the RSS block.](https://wordpress.org/documentation/files/2022/11/197761657-5fa6467c-b73a-41ca-9c38-b79833af866e.png)

### Settings

**Number of items**: Slider and number box to adjust the number of feed items you’d like to display. To change the number move the dot on the slider or update the number in the box next to it.

**Display author**: Switch on/off the display of the author’s name

**Display date**: Switch on/off the display of the published date of the feed items

**Display excerpt**: Switch on/off the display of an excerpt from the feed items’ content.

**Max number of words in excerpt**: Slider and number box to choose the maximum number of words that can be displayed in the excerpt. The minimum number is 10. This section is not visible if **Display excerpt** is in the OFF position.

**Columns**: Slider and number box to control the number of columns for the grid view. This option is only visible when you select the **Grid view** on the Block Toolbar.

### Dimensions

The *paragraph* block provides various options to adjust its dimensions, such as width and height, allowing you to customize the text layout to ensure visual consistency.

> [!NOTE]
> For details refer to this support article: [Dimension settings overview](../../write/block-settings/dimensions.md)

### Border

The Paragraph block provides border settings options to add border color, width, and radius.

> [!NOTE]
> For details refer to this support article: [Border settings overview](../../write/block-settings/border.md)

### Advanced

The RSS block provides the following Advanced settings options: HTML anchor, Additional CSS Class(es), Additional CSS, and Styles.

> [!NOTE]
> [Learn more about advanced settings](../../write/block-settings/advanced.md)

## Resources

-   [Learn more about RSS on Wikipedia](https://en.wikipedia.org/wiki/RSS)
-   [Learn more about WordPress Feeds](https://github.com/WordPress/Advanced-administration-handbook/blob/main/wordpress/feeds.md)
