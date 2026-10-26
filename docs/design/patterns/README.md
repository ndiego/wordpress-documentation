---
title: Patterns
description: Patterns are ready-made groups of blocks that you insert and then change to fit your content.
type: concept
order: 30
redirect_from:
  - /documentation/article/block-pattern/
  - /documentation/article/comparing-patterns-template-parts-and-reusable-blocks/
  - /documentation/article/reusable-blocks/
  - /documentation/article/site-editor-patterns/
---

# Patterns

Block Patterns are a collection of blocks that you can insert into posts and pages and then customize with your own content. Using a Block Pattern can reduce the time required to create content on your site, as well as being a great way to learn how different blocks can be combined to produce interesting effects.

To find more patterns, you can also [use the Block Pattern Directory](pattern-directory.md).

-   [How to use a Block Pattern](#how-to-use-a-block-pattern)
-   [How to customize a block pattern](#how-to-manage-a-block-pattern)
-   [How to find contextual patterns](#how-to-find-contextual-patterns)
-   [Resources](#resources)
-   [Frequently asked questions](#frequently-asked-questions)

Since WordPress 6.3, you can create your own patterns. Patterns work exactly the same as predefined patterns stored in the Patterns Directory. Also, with the “Sync” option enabled, the synced pattern will behave in exactly the same way as a reusable block. Editing the synced pattern will update it anywhere it is used. After creating a synced pattern, you can ‘Detach’ it to a regular block, and edit the block without affecting your already saved synced pattern.

> [!NOTE]
> WordPress 6.3 renamed Reusable Blocks to Patterns. A synced pattern will behave in exactly the same way as a reusable block.

## How to use a block pattern

1.  Click the + icon to add a new block from the top toolbar in the [WordPress Block editor](../../write/editor/README.md).
2.  Click on the **Patterns** tab or **Synced Patterns** tab.
3.  For the Patterns tab, use the dropdown to choose which category of patterns you want to use, or click **Explore** to open a modal that allows you to have a larger view of each pattern.
4.  Either click the pattern you wish to insert or drag and drop it into your content. If you click on the pattern, it will be inserted at the location of your cursor.

[Watch the video](https://wordpress.org/documentation/files/2021/12/Block-pattern-5.9.mov)

### How to edit content added from a Block Pattern

Once you insert a block pattern onto your page, you can edit its elements using content-only editing. In this mode, editing options are restricted to basic content changes, such as modifying text or swapping images, which prevents accidental changes to the layout.

To unlock full editing capabilities for the individual blocks inside the pattern, select the **Edit pattern** button either by selecting the pattern in the block inspector or by locating the button on the Block Settings sidebar.

[Watch the video on VideoPress](https://videopress.com/v/vieUNG8x)

https://videopress.com/v/vieUNG8x

## How to create a block pattern

Since WordPress 6.3, you can create your own patterns.

1.  Select the block or blocks you want to turn into a pattern.
2.  Click on the **three dot** menu that opens up the **additional settings**.
3.  Click on “**Create pattern/reusable block**“.
4.  Enter the name of the pattern.
5.  To synchronize patterns, turn on the **Sync option**. Editing the pattern will update it anywhere it is used.
6.  Click Create.

[Watch the video](https://wordpress.org/documentation/files/2023/08/256239744-52edd86c-a582-4719-97e3-d11159161e46.mp4)

You’ll then be able to locate the created patterns at **Patterns -> My Pattern** or Synced Patterns (overlapping rhombus icon) of Block Inserter.

![Location of "My Patterns" within the block inserter.](https://wordpress.org/documentation/files/2023/08/WP-6-3-create-patterns.jpeg)

## How to manage a block pattern

You can manage your pattern from the Site Editor.

1.  Select **Appearance** -> **Editor** on the Administration Screen.
2.  Click **Patterns**.

    Selecting **Options** -> Manage Patterns in the Block Editor opens the same panel.

### How to work with patterns

You can Rename, Duplicate, Export as JSON, and Delete the pattern from Actions menu (three dot icon) of each pattern.

![Site Editor listing all custom patterns and how to edit them.](https://wordpress.org/documentation/files/2024/03/257561238-782eee25-933c-4f66-95b7-439ae8022e28-6.png)

### How to edit the content of the pattern

To modify a pattern, click the pattern, and click Edit (pencil icon).

[Watch the video](https://wordpress.org/documentation/files/2023/08/2p-6-3-How-to-edit-a-pattern.mp4)

### How to customize a block pattern

Once you insert a Block Pattern, the blocks can be edited in the same way as any other blocks.

Click on any block in the pattern to edit the content within the block.

![Image of a block pattern showing an arrow pointing to the Replace option for the image in the pattern.](https://wordpress.org/documentation/files/2021/07/Screen-Shot-2021-07-08-at-5.22.08-PM.png)

You can also add more blocks to a Block Pattern and insert more Block Patterns to your page anywhere you want.

For the synced pattern, you’ll see the synced pattern mentioned in the saving flow when you save the post or page itself. Saving will update it anywhere it is used, even in other posts or pages.

![Message confirming that a pattern is about to be saved.](https://wordpress.org/documentation/files/2023/08/wp-6-3-saving-a-pattern.jpeg)

### How to find contextual patterns

Some blocks such as the [Social Icons](../../blocks/widgets/social-links.md) block and [Query Loop](../../blocks/theme/query.md) block have patterns built into the settings of the block. To find the contextual patterns for the **Social Icons** block, select the **Social Icon** in the **Block toolbar** and navigate to **Patterns** in the drop-down:

![Contextual patterns found in Social Icons block](https://wordpress.org/documentation/files/2020/09/social-icons-contextual-pattern.gif)

*Demonstration of contextual pattern within the Social Icons block in Twenty Twenty-Two theme*

For the **Query Loop** block, patterns are shown as part of the configuration of the block itself. You can learn more about the [Query Loop block here](../../blocks/theme/query.md).

## How to find more patterns

If you want more patterns to choose from, you can explore the [Block Pattern Directory](https://wordpress.org/patterns/). This is a new directory that allows you to search and find new patterns to use on your site. After searching and finding a pattern you like, select **Copy,** and it will be saved to your clipboard. From there, return to your page or post and use the **Paste** function to add the pattern to your content.

You can read more about the [Block Pattern Directory here](pattern-directory.md).

## Resources

-   [“Introduction to Block Patterns”](https://learn.wordpress.org/workshop/intro-to-block-patterns/) – a short workshop published by the Training team.
-   [“Using Block Patterns”](https://learn.wordpress.org/tutorial/using-block-patterns/)– a tutorial published by the Training team.
-   “[Contextual patterns for easier creation](https://make.wordpress.org/core/2021/05/20/core-editor-improvement-contextual-patterns-for-easier-creation/)” – a post on the WordPress Core blog.

## Frequently asked questions

**Can I use the default images within Block Patterns on my own site?**

Yes! The images provided within Block Patterns are free to use on your site. However, because these images are being referenced from an external source (i.e. they are not added to your site’s Media Library), there is always a chance they could change or be removed.

We recommend replacing these images with your own content, but if you would like to use the ones in the patterns, please consider uploading them to your own Media Library by using the “*Upload external image*” button.

![Screenshot of an image block toolbar displaying the "upload image to media library".](https://wordpress.org/documentation/files/2024/03/257561238-782eee25-933c-4f66-95b7-439ae8022e28-7.png)

When you publish a post, the pre-publish check will ask you if you want to upload external images to the media library.

![Pre-publish option for uploading all external images to media library.](https://wordpress.org/documentation/files/2024/03/257561238-782eee25-933c-4f66-95b7-439ae8022e28-10.png)

**Will Block Patterns be changed? Will changes to patterns that I use impact my site?**

New Block Patterns will be continuously added, and existing Block Patterns may be changed or removed over time. However, once you add a Block Pattern to your site, there is no link to the original pattern in the Add Block menu, and any subsequent changes would not impact anything on your site’s pages or posts.

## Patterns

<!-- TODO: merge: this section was absorbed from helphub:editing-and-design/block-editor/patterns; edit it into the page. -->

Patterns are ready-made collections of blocks you can insert and customise. Synced patterns
(formerly reusable blocks) update everywhere they are used when you edit them.

Learn how to use patterns, find more in the Pattern Directory, submit your own, and how
patterns differ from template parts.

## Synced patterns (Reusable blocks)

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/reusable-blocks/; edit it into the page. -->

A Synced Pattern is a type of block pattern that enables the Synced option, and it will behave in exactly the same way as a reusable block. Editing the synced pattern will update it anywhere it is used. After creating a synced pattern, you can ‘detach’ it to a regular block, and edit the block without affecting your already saved synced pattern. For more information, you can learn more in the [Synced Pattern article](https://wordpress.org/news/2023/07/synced-patterns-the-evolution-of-reusable-blocks/).

> [!NOTE]
> WordPress 6.3 renamed Reusable Blocks to Patterns. A synced pattern will behave in exactly the same way as a reusable block.

### Creating a synced pattern

Let’s say you have a paragraph block which you often fill with the same text at the end of your post. This could be everything from how to get in touch to your business hours to your social media accounts. To avoid having to add the same content to a paragraph block every time you want to place it at the end of your post, you can make it a synced pattern. To accomplish this, follow these steps:

1.  Select the block or blocks you want to turn into a pattern.
2.  Click on the three dot menu that opens up the additional settings.
3.  Click on “Create pattern”.
4.  Enter the name of the pattern.
5.  Turn on the Synced option
6.  Click Create.

[Watch the video](https://wordpress.org/documentation/files/2023/08/256239744-52edd86c-a582-4719-97e3-d11159161e46.mp4)

You’ll then be able to locate the created synced patterns at Synced Patterns (crossing rhombus icon) of Block Inserter.

![The Block inserter with the "Synced Patterns" icon highlighted.](https://wordpress.org/documentation/files/2023/07/WP-6-3-working-with-patterns.jpeg)

### Using a synced pattern

After you’ve created a Synced Pattern, you can then use it wherever you’d like. You’ll also have a few more options for adding one into your content:

-   You can open up the **Block Inserter** and switch to the **Synced Patterns** section to add whichever option you want.
-   Click on the add block button and search for the name of the synced pattern you want to use.
-   You can type <kbd>/</kbd> followed by the name of the synced pattern you want to use.

After inserting the Synced Pattern you want to use, make sure to select the ‘**Detach pattern**‘ (formerly known as “**Convert to Regular Block**“) option shown below if you wish to make any changes to the block on that page or post only. Note that this option won’t be available if the Synced Pattern is locked.

![Synced Pattern Toolbar with the "Detach Pattern" option highlighted.](https://wordpress.org/documentation/files/2023/07/wp-6-3-detach-pattern.jpeg)

### Selecting and editing a synced pattern

If you’d like to edit a synced pattern, you can do so in two ways:

-   You can add the block directly into a post or page and edit it from there. If you do this, you’ll see the synced pattern mentioned in the saving flow when you save the post or page itself.
-   You can go to **Options > Manage Patterns**, which will take you to a specific interface where you can directly edit patterns as you’d like.

*Keep in mind that, when a synced pattern is changed, the change will be reflected in all the places where the same synced pattern was used.*

### Removing a synced pattern

To remove a synced pattern, click on the **three dots** icon and select the option to **Manage Patterns**. From there you can edit and delete patterns as you’d like.

Keep in mind that when a synced pattern is removed, the removal will be reflected in all the places where the same synced pattern was used. You’ll see the message below where the removed synced pattern existed:

![A block with a message saying "Block has been deleted or Is unavailable."](https://wordpress.org/documentation/files/2023/07/wp-6-3-missing-reusable-block.jpeg)

### Detaching a synced pattern

After inserting the Synced Pattern you want to use, make sure to select the ‘Detach‘ (formerly known as “Convert to Regular Block“) option shown below if you wish to make any changes to the block on that page or post only. Note that this option won’t be available if the Synced Pattern is locked.

![How to detach a Synced Pattern](https://wordpress.org/documentation/files/2021/07/373936608-d8b8886d-1837-426f-a0ae-e2fd06713fd9.jpg)

### Demonstration of a synced pattern

In this demo, we insert Synced Patterns in the three ways described above (Block Inserter, Add Block icon, ‘/’ key). A change in one pattern (in this case, a change in text color) will be reflected in others. Next, detach the middle Synced Pattern. Synchronization is then lost. And if you look at it in the list view, it is back to a normal block.

[Watch the video](https://wordpress.org/documentation/files/2023/07/wp6.3-synced-pattern-demo.mp4)

## Site Editor patterns

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/site-editor-patterns/; edit it into the page. -->

Since WordPress version 6.3, it is possible to create and manage your site’s [Patterns and template parts](README.md) via the Site Editor’s sidebar. You can learn about the Site Editor in this article: [Site Editor](../site-editor/README.md).

> [!NOTE]
> The Site Editor Patterns menu is **only** available when you install and activate a [Block theme](https://developer.wordpress.org/themes/getting-started/what-is-a-theme/) on your site.

### Working with patterns

Navigate to **Appearance > Editor > Patterns** to access your Patterns and template parts.

Please note that template parts are now listed under **Patterns**.

![Showing the location Pattern menu itim](https://wordpress.org/documentation/files/2023/08/patterns.png)

### Template parts

The first type of pattern you will find are **Template parts**. Template parts are **included with block themes** and are typically used on multiple templates across your site.

If you click on the **Actions** (ellipsis) button, you will see options to **edit** or **duplicate** that Template part.

Finally, you can edit the Template part by clicking directly on it.

![Template parts and their option](https://wordpress.org/documentation/files/2023/08/template_parts.png)

### My patterns

The first item in the Patterns section is **My patterns**. This section lists all the custom patterns you added to your site yourself. They can be filtered by [**Synced**](README.md) or **Standard** (non-synced).

> [!NOTE]
> If you have a lot of Patterns, the **Command Palette** is another great find them. Learn more about the [Command Palette here](../site-editor/command-palette.md).

If you click on the **Actions** (ellipsis) button next to each pattern, you will see options to **Edit**, **Duplicate**, **Rename, Export as JSON** or **Delete** that pattern.

![My patterns action menu](https://wordpress.org/documentation/files/2023/08/my_patterns_options.png)

You can edit any pattern just by clicking on the pattern itself.

### Theme patterns

Underneath **My patterns**, you can find regular patterns that come bundled with your theme. These patterns **cannot be edited directly** (hence they are marked with a lock symbol). Instead, you can click on the **Actions** (ellipsis) button and click **Duplicate** to create an editable copy of that pattern. This copy will be listed under **My patterns**.

![Theme patterns' duplicate option](https://wordpress.org/documentation/files/2023/08/theme_patterns_duplicate-1.png)

### Add or import new patterns

There is an **Add Pattern** button in the right corner that you can click on to create new patterns. If you click on it, you will see three options: **Add Pattern, Add Template part,** and **Import pattern from JSON**.

![Plus sign icon to create new patterns](https://wordpress.org/documentation/files/2023/08/add_pattern_button.png)

> [!NOTE]
> You can learn more about the difference between [Patterns and template parts here](README.md).

### Export patterns

You can export patterns from the **My Patterns** section in the Site Editor. Patterns that come with a theme are locked and cannot be exported.

To export a single pattern, go to **Patterns > My Patterns**. Click the **Actions** (ellipsis) button next to the pattern. Select **Export as JSON**, which downloads the pattern as a .json file.

To export multiple patterns, in My Patterns, select the box to check all patterns located at the bottom. And then click the **Download icon**. This downloads a .zip file containing .json files for each pattern chosen.Besides that, the box to check all patterns located at the bottom allows you to bulk **Delete** patterns as well.

![Export patterns option showcased on single pattern and as a part of the bulk edit.](https://wordpress.org/documentation/files/2023/08/export_patterns.png)

### Appearance settings

In the top-right corner of the **Patterns** screen, just below the **Add Pattern** button, you’ll find options to customize how patterns are displayed.

The first icon, **Layout**, lets you switch between grid and list views, depending on your preference.

The second icon, **View Options**, provides more detailed controls. You can change the sort order of patterns, adjust the preview size, set the number of patterns per page, and choose which pattern details are displayed in the list.

![Appearance Settings icons and opened appearance settings section](https://wordpress.org/documentation/files/2023/08/layout.png)

## Comparing patterns, template parts, and synced patterns (Reusable blocks)

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/comparing-patterns-template-parts-and-reusable-blocks/; edit it into the page. -->

### Overview

With more types of reusable content you can create with WordPress, this article seeks to clarify when it makes sense to use certain types in different situations to help guide you to make the best decisions possible. At a high level, this will focus on Template Part blocks, Block Patterns, and Synced Patterns (Reusable Blocks).

> [!NOTE]
> WordPress 6.3 renamed Reusable Blocks to Patterns. A synced pattern will behave in exactly the same way as a reusable block.

#### Template part

The Template Part block is an advanced block that can be used with a block theme or a theme that supports [template editing](https://wordpress.org/themes/tags/template-editing/). They often come with your theme and are used to organize and display your site structure. For more information, you can learn more in the [Template Part block support article](../../blocks/theme/template-part.md).

#### Synced pattern (Reusable block)

Synced pattern is a kind of block pattern that enabled Synced option, and it will behave in exactly the same way as a reusable block. Editing the synced pattern will update it anywhere it is used. After creating a synced pattern, you can ‘Detach’ it to a regular block, and edit the block without affecting your already saved synced pattern. For more information, you can learn more in the [Synced Pattern article](README.md).

#### Block patterns

Block Patterns are a collection of predefined blocks that you can insert into posts and pages and then customize with your own content. For more information, you can learn more in the [Block Pattern support article](README.md).

Here’s a table comparing these different options to each other:

|  | Template Part | Synced Patterns (Reusable Block) | Patterns |
| --- | --- | --- | --- |
| Type | Site Structure | User Content | User Content |
| Syncing Ability | Synced | Synced | Un-synced |
| Example | Footer | Business hours | Call to action |

Site structure means it should not be a part of your content, like a post or page. Syncing ability touches on whether if you update it in one spot, it updates everywhere the same block is used.

### Guidelines

Based on the above, this means it’s best to use template parts and Synced pattern for things you want to have in sync with each other whereas patterns are best for content that you expect to change across your site.

In general, template parts should not be added to a Synced pattern or a regular pattern since this is meant to represent site structure rather than content. A template part can include a Synced pattern though or be built using patterns! You can also use block patterns to build templates and template parts, but you should not use a template part inside a pattern.

### Situationals

#### Repeated content across your site

This could be everything from how to get in touch to your business hours to your social media accounts. To avoid having to add the same content to a paragraph block every time you want to place it at the end of your post, you can make it a Synced pattern.

#### Repeated structure across your site

For anything that’s more about site structure that’s repeated across your site, like a Header or Footer, it’s best to use a template part. These are intended for structural elements in a block theme, so it’s important to distinguish them from patterns.

#### Repeated design or layout

When it’s less about content and more about wanting to repeat a design or layout, patterns are best to use. This is because the content doesn’t need to be synced and, instead, what you want repeated is how something visually looks.

## For theme developers

Shipping patterns with a theme, registering them, using PHP in them and placing them in templates is covered in [Patterns](https://developer.wordpress.org/themes/patterns/) in the developer documentation.
