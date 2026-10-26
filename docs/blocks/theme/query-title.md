---
title: Query Title
description: Show a heading that matches the archive or search results being viewed with the Query Title block.
type: reference
slug: query-title-block
redirect_from:
  - /documentation/article/archive-title-block/
  - /documentation/article/query-title-block/
  - /documentation/article/search-results-title-block/
---

# Query Title

The Query Title block displays a dynamic heading based on the type of content being viewed, such as a category name, search term etc.

It has two main variations:

## Archive title

-   Displays the title of the current archive page, such as a category, tag, author, or date.
-   To add a Archive Title block, click the Block Inserter (+) icon, search for “Archive Title”, and select it from the list to insert it into your template.

![Archive Title](https://wordpress.org/documentation/files/2025/08/query-title-1-6.8.png)

## Search result title

-   Displays a heading based on the user’s search query.
-   To add a Search Results Title block, click the Block Inserter (+) icon, search for “Search Results Title”, and select it from the list to insert it into your template.

![Search Result Title](https://wordpress.org/documentation/files/2025/08/query-title-2-6.8.png)

> [!NOTE]
> Both of these are built on top of the same underlying block (core/query-title) and share the same functionality and controls, they differ only in what type of content they’re designed to display.

## Block toolbar

To view the block toolbar, click on the block, and the toolbar will be displayed.

> [!NOTE]
> Every block comes with unique toolbar icons and blocks specific user controls that allow you to manipulate the block right in the editor.

**The Query Title block shows seven buttons in the block toolbar ( From Left to Right ):**

![Block toolbar](https://wordpress.org/documentation/files/2025/08/query-title-3-6.8.png)

-   Transform to
-   Drag icon
-   Move arrows
-   Heading Level
-   Text Alignment
-   More options

### Transform To

Click on the Transform button to convert the Archive Title block into a Columns, Details, or Groupblock:

![Block toolbar - Transform To](https://wordpress.org/documentation/files/2025/08/query-title-4-6.8.png)

### Drag

To drag and drop the block to a new location on the page template, click and hold the rectangle of dots, then drag it to the new location. The blue separator line indicates where the block will be placed. Release the left mouse button when you find the new location to place the block.

![Block toolbar - Drag](https://wordpress.org/documentation/files/2025/08/query-title-5-6.8.png)

### Move up / down arrows

The up and down arrow icons can be used to move the block up and down on the page.

[Get more information about moving a block within the editor.](../../write/blocks/move-blocks.md)

![Block toolbar - Move Up and Down Arrows](https://wordpress.org/documentation/files/2025/08/query-title-6-6.8.png)

### Heading level

You can choose the heading level for the Archive Title from H1–H6.

![Block toolbar - Heading Level](https://wordpress.org/documentation/files/2025/08/query-title-7-6.8.png)

### Text alignment

Click the Change alignment button in the Block toolbar to display the alignment drop-down. You can align the block text to the left, make it center-aligned or align it to the right.

![Block toolbar - Text Alignment](https://wordpress.org/documentation/files/2025/08/query-title-8-6.8.png)

### Options menu

The [More Options menu](../../write/blocks/more-options.md) represented by three vertical dots on the far right of the toolbar gives you more features such as the ability to duplicate, remove, or edit your block as HTML.

![Block toolbar - Options Menu](https://wordpress.org/documentation/files/2025/08/query-title-9-6.8.png)

## Block settings

The block settings panel contains customization options specific to the block. To get to the settings, select the block and click to open the Inspector sidebar. You should see the block settings displayed below with the title “Archive Title” at the top:

### Block settings

![Block Settings panel](https://wordpress.org/documentation/files/2025/08/query-title-10-6.8.png)

#### Show archive type in title

Toggle this option to include or exclude the archive type (e.g., “Category”, “Tag”, “Author”) in the title.

-   Enabled (default): Displays titles like Category: Travel
-   Disabled: Displays just Travel

### Style settings

![Style Settings panel](https://wordpress.org/documentation/files/2025/08/query-title-11-6.8.png)

#### Color

Text and background colors can be set on a per-block basis, allowing you to call attention to important content. Using the Color settings, you can customize the block by adding text, background, and link colors.

> [!NOTE]
> [See this guide for more information about changing colors.](../../write/block-settings/color.md)

![Color panel](https://wordpress.org/documentation/files/2025/08/query-title-12-6.8.png)

#### Typography

The Typography settings enable you to customize the font and text appearance of the content within the Archive Title block. The settings have various options, such as font family, size, appearance, line height, letter case, letter spacing, and decoration.

> [!NOTE]
> [Get more details about changing typography settings.](../../write/block-settings/typography.md)

#### Dimensions

The Archive Title block provides various options to adjust its dimensions, such as width and height, allowing you to customize the text layout to ensure visual consistency.

#### Border

The Archive Title block provides border settings options to add border color, width, and radius.

> [!NOTE]
> For details refer to this support article: [Border settings overview](../../write/block-settings/border.md)

#### Advanced

The following Advanced settings options are available: HTML Anchor, Additional CSS Class(es), Additional CSS, and Styles.

> [!NOTE]
> [Learn more about advanced settings.](../../write/block-settings/advanced.md)

## Archive Title block

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/archive-title-block/; edit it into the page. -->

Use the *Archive Title block* to display the name of the Category, Tag, or custom Taxonomy, on the archive pages.

![The archive title block on the Site Editor](https://wordpress.org/documentation/files/2023/02/archive-title-block.png)

> [!NOTE]
> This block works only in the archive pages and will not be visible on other pages of the website. This block should be used only in the [Site Editor](../../design/site-editor/README.md) to edit the archive page templates.

To add an *Archive Title block*, click the **Block Inserter** icon when editing the archive page template. Search for the *Archive Title block*. Click on it to add the block to your page template.

![Adding an archive title block](https://wordpress.org/documentation/files/2023/02/adding-an-archive-title.gif)

You can also use the keyboard shortcut <kbd>/archive-title</kbd> to quickly insert an *Archive Title block*.

> [!NOTE]
> [Detailed instructions on adding blocks](../../write/blocks/add-a-block.md)

### Block toolbar

To view the block toolbar, click on the block, and the toolbar will be displayed.

![Archive title block toolbar](https://wordpress.org/documentation/files/2023/02/block-toolbar.png)

Every block comes with unique toolbar icons and blocks specific user controls that allow you to manipulate the block right in the editor.

The *Archive Title block* shows seven buttons in the block toolbar:

-   Transform to
-   Drag icon
-   Move arrows
-   Change alignment
-   Change heading level
-   Change text alignment
-   More options

**Transform to**

![Transform options for the archive title block](https://wordpress.org/documentation/files/2023/02/transform-2.png)

Click on the **Transform** button to convert the *Archive Title bloc*k into a *Group* block or *Columns* block.

**Drag icon**

![Drag and drop tool on the toolbar](https://wordpress.org/documentation/files/2023/02/drag-and-drop-tools.png)

To drag and drop the block to a new location on the page template, click and hold the rectangle of dots, then drag it to the new location. The blue separator line indicates where the block will be placed. Release the left mouse button when you find the new location to place the block.

**Move arrows**

![Block moving tools on the block toolbar](https://wordpress.org/documentation/files/2023/02/block-moving-tools.png)

The up and down arrow icons can be used to move the block up and down on the page.

> [!NOTE]
> [Get more information about moving a block within the editor.](../../write/blocks/move-blocks.md)

**Change alignment**

![Block alignment tools](https://wordpress.org/documentation/files/2023/02/block-align.png)

Use the change alignment tool to align the *Archive Title block*. Choose one of the following options:

-   **None –** Leaves the block the current size.
-   **Wide width –** Increase the width of the block beyond the content size.
-   **Full width –** Extend the block to cover the full width of the screen.

**Change heading level**

![](https://wordpress.org/documentation/files/2023/02/heading-settings.png)

You can choose the heading level for the archive title from H1-H6.

**Change text alignment**

![Text alignment tools](https://wordpress.org/documentation/files/2023/02/block-alignment.png)

Click the **Change alignment** button in the block toolbar to display the alignment drop-down. You can align the block text to the left, make it center-aligned or align it to the right.

**Options**

The **Options** button on a block toolbar gives you more features to customize the block.

> [!NOTE]
> [Read about these and other settings.](../../write/blocks/more-options.md)

### Block settings

The block settings panel contains customization options specific to the block. To open it, select the block and click the **Settings** icon next to the **Publish** button.

![Block settings button icon](https://wordpress.org/documentation/files/2023/02/settings-icon.png)

Here are the options for the *Archive Title* *block*:

**Settings**

It’s possible to toggle between an option to either show the archive type in the title or not.

![Show archive tipe toggle setting](https://wordpress.org/documentation/files/2023/02/block-settings.png)

An example with this setting enabled:

![Archive title with the type enabled](https://wordpress.org/documentation/files/2023/02/archive-type-enabled.png)

An example with this setting disabled:

![Archive title with the type disabled](https://wordpress.org/documentation/files/2023/02/archive-type-disabled.png)

**Color**

The *Archive Title block* provides color settings options to change the text and background colors.

![Color Settings in the Archive Title Block](https://lh4.googleusercontent.com/vGd1bPidVEXdbHGSIQXoK_PJsIlt2uxxSNBruY4CYExWqpxY19xNxdJR1gWrU8DI0u8TUnckQaBp-MDl4431435PIQWztwspNaJJiDouBJ5K9bfsXUVWWfBNgOVfZV0r45EG1vA6)

*Color Settings in the Archive Title Block*

> [!NOTE]
> [See this guide for more information about changing colors.](../../write/block-settings/color.md)

**Typography**

The *Archive Title block* provides typography settings to change the font family, size, appearance, line height, letter case, letter spacing, and decoration.

> [!NOTE]
> [Get more details about changing typography settings.](../../write/block-settings/typography.md)

**Dimensions**

The *Archive Title block* provides dimensions settings options to change padding and margin size.

![Archive title dimension settings](https://wordpress.org/documentation/files/2023/02/dimensions-settings.png)

> [!NOTE]
> [Learn more about dimension controls.](../../write/block-settings/dimensions.md)

**Advanced settings**

The following Advanced settings options are available: HTML Anchor, Additional CSS Class(es), Additional CSS, and Styles.

> [!NOTE]
> [Learn more about advanced settings.](../../write/block-settings/advanced.md)

## Search Results Title block

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/search-results-title-block/; edit it into the page. -->

The **Search Results Title** block displays a title above the search results. You can add this block to the search template in a theme that supports full site editing.

If you add this block in other templates, a page, or a post, the block won’t appear on the website’s front end.

To add one, open the search template in the [Site Editor](../../design/site-editor/README.md) by clicking on the site icon (or the W icon, if no site icon is set for the site) and select **Templates**. Then choose the **Search** template from the list (If you don’t find the **Search** template, click **Add New** button and add the **Search** template to your theme). In the **Search** template, click the **Block Inserter** (+) icon and add the **Search Results Title** block to the template.

![Searching the "Search Results Title" in the block](https://wordpress.org/documentation/files/2022/11/search-result-title-1-6.8.png)

> [!NOTE]
> Refer to this support article for [detailed instructions on adding blocks](../../write/blocks/add-a-block.md).

Now, if you perform a search on your website, you’ll see the search results title on the search page.

![Search page results when using "Search Results Title" block](https://wordpress.org/documentation/files/2022/11/search-result-title-2-6.8.png)

### Block toolbar

Each block has its own toolbar, which contains unique controls that let you customize or configure the block. The Search Results Title block has the following options:

**Transform to**

![Transform options in the search results title block](https://wordpress.org/documentation/files/2022/11/search-result-title-3-6.8.png)

If you click the **Search Results Title** icon on the toolbar, you’ll open the **Transform to** options to convert the block into **Columns** and **Group** blocks.

**Block moving tools**

The **Drag** button lets you drag and drop the Search Results Title block and reposition it anywhere on the editor, while the **Move up** and **Move down** buttons let you move the Search Results Title block up or down on the editor.

![Block moving tools in the search results title block](https://wordpress.org/documentation/files/2022/11/search-result-title-4-6.8.png)

**Heading level**

The **Change Heading Level** button lets you open a drop-down menu where you can select the heading level for the search results title. You can choose from H1 to H6 heading levels.

![Change heading in the search results title block](https://wordpress.org/documentation/files/2022/11/search-result-title-5-6.8.png)

**Text alignment**

Text alignment options let you choose to align the title left, center, or right.

![Text alignment in the search results title block](https://wordpress.org/documentation/files/2022/11/search-result-title-6-6.8.png)

**More options**

![More options in the search results title block](https://wordpress.org/documentation/files/2023/07/more-options-pattern-reusable-block.png)

Click on the **Options** button to show more block options. A drop-down menu will appear, and here are the actions you can find:

-   *Show/Hide more settings* opens or closes the block settings panel on the editor’s sidebar. Its functionality is similar to clicking the **Settings** button at the top-right section of the editor.
-   *Select parent block* will move you to the parent block that contains the Search Results Title block. This option is only available if the Search Results Title block is inside a container block.
-   *Copy block* adds the Search Results Title block into the clipboard. Then, you can paste it anywhere you want in the block editor.
-   *Duplicate* creates a copy of the selected block that appears after the current block.
-   *Insert before* adds a new block before the selected block(s).
-   *Insert after* adds a new block after the selected block(s).
-   *Move to* lets you use a blue line on the editor to indicate the new position for the selected block. Use your keyboard’s up and down arrows to move the blue line. When the line is in the desired position, press **Enter** to move the selected block to that position.
-   *Lock* lets you prevent users from moving or deleting the selected block. A pop-up window will appear to set the block locking attribute to the selected block. You can opt to disable movement, prevent removal, or both for the selected block.
-   *Create Template part* allows you to create a new template from the selected block. A pop-up window will appear to name the template part and select the template area.
-   *Create pattern/reusable block* makes the selected blocks a pattern. A pop-up window will appear to set the name for the pattern and enable synced option.
-   *Group* turns the selected block(s) into a group of blocks so you can configure them as a unit.
-   *Remove Search Results Title* deletes the selected block from the content.

### Block settings

Every block has specific options in the block settings panel. To open it, select the block and click the **Settings** button at the top-right section of the editor, or click the **Options** button on the block toolbar and select **show more settings**.

**Settings**

The **Show search term in title** option lets you add the search query in the title. If disabled, the Search Results Title block only shows the “Search Results” text.

![Settings in the search results title block](https://wordpress.org/documentation/files/2022/11/search-result-title-7-6.8.png)

**Color**

The **Search Results Title block** provides Color settings options to change the text and background.

For details refer to this support article: [Color settings overview](../../write/block-settings/color.md)

![Color settings panel with options for text and background color](https://wordpress.org/documentation/files/2022/11/search-result-title-8-6.8.png)

**Typography**

The **Search Results Title block** provides typography settings to change the font family, appearance, line height, letter spacing, decoration, letter case, and font size.

For details refer to this support article: [Typography settings overview](../../write/block-settings/typography.md)

![Typography controls including font familt, size, appearance, line height, letter spacing, decoration and letter case](https://wordpress.org/documentation/files/2022/11/search-result-title-9-6.8.png)

**Dimensions**

The **Search Results Title block** provides dimension settings options to add padding and margin.

For details refer to this support article: [Dimension settings overview](../../write/block-settings/dimensions.md)

![Responsive dimension settings](https://wordpress.org/documentation/files/2022/11/search-result-title-10-6.8.png)

**Advanced**

The following Advanced settings options are available: HTML Anchor, Additional CSS Class(es), Additional CSS, and Styles.

> [!NOTE]
> [Learn more about advanced settings.](../../write/block-settings/advanced.md)
