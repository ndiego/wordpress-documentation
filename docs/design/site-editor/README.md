---
title: The Site Editor
description: "Design your whole site with blocks in the Site Editor, from the header and footer to every template."
type: guide
order: 20
redirect_from:
  - /documentation/article/additional-guide-to-using-the-site-editor/
  - /documentation/article/site-editor-pages/
  - /documentation/article/site-editor/
  - /documentation/article/zoom-out-view/
---

# The Site Editor

The Site Editor is where you design your whole site with blocks: the header and footer, the templates that lay out each kind of page, and the styles (colors, fonts, spacing) that apply everywhere. Where the post editor changes one post, the Site Editor changes what every page has in common.

This page shows how to open the Site Editor, what is in its menu and workspace, and the tasks you do there. The pages in this group cover each part in depth: [templates](templates.md), [styles](styles.md), [fonts](fonts.md), [navigation](navigation.md), the [site icon](site-icon.md) and the [Command Palette](command-palette.md).

> [!NOTE]
> The Site Editor is **only** available when you install and activate a [block theme](../themes/block-themes.md) on your site.

## How to access the Site Editor

To work with the Site Editor, you need to use a [block theme](../themes/block-themes.md) on your site. A block theme is a theme that uses [blocks](../../blocks/README.md) for all parts of a site, including navigation menus, header, content, and site footer.

All [blocks](../../blocks/README.md) that are available in the [WordPress Block editor](../../write/editor/README.md) can be used in the Site Editor. A set of blocks called [Theme blocks](../../blocks/README.md#theme-blocks) are specifically built for the Site Editor.

To find block themes, from the WordPress dashboard, go to **Appearance** > **Themes** and select **Add Theme**. In the **Add Themes** page, select **Block Themes** to find the growing list of [Block themes](../themes/block-themes.md) in the [WordPress theme directory](https://wordpress.org/themes/tags/full-site-editing/).

![Appearance > Themes showing block theme options](https://wordpress.org/documentation/files/2022/01/Appearance-Themes-showing-block-themes.png)

*How to find a block theme*

Once you install and activate a Block theme on your site, go to **Appearance** > **Editor** to open the Site Editor.

![Appearance section of the admin interface showing the Themes and Editor entry points after activating a block theme.](https://wordpress.org/documentation/files/2022/01/Screen-Shot-2023-03-27-at-6.23.05-PM.png)

*Appearance menu after activating a block theme*

## Things to do in the Site Editor

Once you enter the Site Editor, you will see these menu items.

![Main menu screen in the Site Editor.](https://wordpress.org/documentation/files/2026/08/site-editor.jpg)

-   [Identity](site-icon.md): Allows you to set Site Title, Site Tagline, Site Logo, and Site Icon at a high level.
-   [Styles](styles.md): Provides a direct access to edit your site’s style variations.
-   **Pages**: Allows you to edit the content of your pages inside the Site Editor itself.
-   [Navigation](navigation.md): Allows you to browse your menus and make basic changes.
-   [Patterns](../patterns/README.md): Your Synced patterns and template parts can be managed here.
-   [Templates](templates.md): Review the different default layouts for the different sections on your site, as well as custom pages (search results, 404, etc).

You will also see an icon of a magnifying glass in the Admin bar. Click on it to access the [Command Palette.](command-palette.md)

Below is an overview of the different sections in the Site Editor.

[Watch the video](https://wordpress.org/documentation/files/2023/08/site-editor-overview.mp4)

## The Site Editor workspace

The Site Editor loads the home page of your site (based on what you have set in the [Reading Settings](../../manage/settings/reading.md#reading-settings)) to start editing.

The top menu in the Site Editor includes the following options:

![Site Editor toolbar with numbers indicating various options to explore.](https://wordpress.org/documentation/files/2026/08/site-editor-persistent-admin-bar-marked-1.jpg)

1.  **Back:** Click the left-chevron Back button to leave the current editing view and return to the previous Site Editor screen. The WordPress Toolbar remains visible above the Site Editor and provides access to WordPress and site navigation.

2.  **The + Block inserter button**: Add a new [block](../../blocks/README.md), [block pattern](../patterns/README.md), Media, or synced pattern (if the site has synched patterns) to the Site Editor.

![Block Inserter Panel](https://wordpress.org/documentation/files/2023/08/6-3-inserter.png)

*Block inserter panel*

3.  **Undo:** Undo the most recent action taken.
4.  **Redo:** Redo an action you reversed using the **Undo** button.
5.  [**List View**](../../write/blocks/list-view.md): See a list of all of the blocks that are on the page and easily navigate between the blocks on your page. This is useful for seeing the page’s structure and editing, moving, and removing blocks.
6.  **[Command Palette](command-palette.md):** Click here to access all your site’s content, templates, and patterns quickly, as well as invoking other actions (settings, new page, etc). Command Palette can always be accessed from the admin bar as well, regardless of which screen you are currently on.

[Watch the video on VideoPress](https://videopress.com/v/pPGxe58s)

7.  **Preview**: Preview changes before saving them. Here you can also save changes as a Responsive styles for a specific viewport.

![Screenshot of the Preview dropdown in Site Editor](https://wordpress.org/documentation/files/2026/08/site-editor-preview.jpg)

8.  **Settings**: Show or hide the Template and Block Settings sidebar menu.

[Watch the video](https://wordpress.org/documentation/files/2023/08/site-editor-reset-customizations.mp4)

9.  [**Styles**](styles.md): Browse style variations available for the theme you have, set the typography, color palettes, and layout for the entire site, or customize the appearance of specific blocks for the whole site.
10. **Save:** Save the changes you made in the Site Editor.
    -   When you click the **Save** button, you will get a list of all the [synced patterns](../patterns/README.md), [navigation menus](navigation.md), [templates](templates.md) and [template parts](../../blocks/theme/template-part.md) where you have made changes.
    -   You can choose to save all or just some of them.
    -   Note that some changes (like changes to the Header and Footer templates) will apply to all pages of your site that use those templates, and not just the page you were working on.

[Watch the video](https://wordpress.org/documentation/files/2023/08/site-editor-save-changes.mp4)

11. **More Options:** Click the three vertical dots icon to open additional settings and tools.

![Site Editor with an arrow pointing to the three dot menu where extra settings can be found.](https://wordpress.org/documentation/files/2023/08/Site-Editor-More-options.png)

12. **Admin bar**: WordPress 7.1 brings a persistent Admin bar into every Site Editor screen. It provides consistent access to WordPress and site navigation while you work in the editor. If a Site Icon is set, it is displayed in the Toolbar. The Toolbar is hidden when Distraction Free mode is enabled.

**View top toolbar**: Display or hide the top toolbar in the editor. When you enable this option, block toolbars are pinned to the top of the WordPress block editor (right under the top toolbar) instead of appearing directly above the block.

![Top toolbar enabled](https://wordpress.org/documentation/files/2026/08/site-editor-view-top-toolbar.jpg)

*Top toolbar enabled*

[Watch the video on VideoPress](https://videopress.com/v/CgczRt4h)

**Spotlight mode**: All blocks are greyed out except for the one you’re working on so that you can focus on a single block at a time.

![Spotlight mode](https://wordpress.org/documentation/files/2022/05/Screen-Shot-2022-05-12-at-10.01.48-PM-1.png)

*Spotlight mode*

**Distraction Free**: When this options is activated, all non-essential parts of the UI will be hidden to provide a more immersive editing experience. Enabling Distraction Free mode also hides the WordPress Toolbar.

**Editor**: By default, you will be in the **Visual editor**. Switch to the **Code editor** to view the entire page in HTML code editor.

**Plugins**: Open the sidebars that plugins add to the Site Editor. This section appears only when an active plugin adds one.

**Tools**: Here, you can download your theme with the updated templates and styles (**Export**), learn [keyboard shortcuts](../../write/editor/keyboard-shortcuts.md), visit the Site Editor welcome guide, copy all blocks, or view additional support articles.

**Preferences**: Use the [Preferences](../../write/editor/preferences.md) menu to customize the editing experience and change how you interact with blocks.

## How to use the Site Editor

### To edit the site’s styles

You can use the Site Editor to customize the styles for the entire website and for the blocks. Styles settings are available regardless of what template or template part you are editing.

-   Go to **Appearance** > **Editor**.
-   Click the Styles menu item or on the icon next to the block settings sidebar.

![The Styles item in the Site Editor menu.](https://wordpress.org/documentation/files/2023/08/site-editor-styles-menu.png)

![The Styles icon next to the settings icon in the Site Editor toolbar.](https://wordpress.org/documentation/files/2023/08/site-editor-styles-icon.png)

In the **Styles** section, you can browse the style variations available for the theme you have, change the color palettes and typography, and layout across the entire site and also change the appearance of blocks which are also applicable across the whole site.

To review your **style revisions or reset the changes** you made completely, click the three-dot menu icon in the right corner and select either option.

[Watch the video](https://wordpress.org/documentation/files/2023/08/site-editor-styles-overview-revisions-reset-1.mp4)

> [!NOTE]
> Learn more about Styles in this support article: [Styles overview](styles.md).

### To customize the site’s layout

You can use the Site Editor to build the structure and layout of your entire site, using blocks. For example, areas like headers, footers, and the structural appearance of your site’s posts and pages.

All [blocks](../../blocks/README.md) that are available in the [WordPress Block Editor](../../write/editor/README.md) can be used in the Site Editor. A set of blocks called [Theme blocks](../../blocks/README.md#theme-blocks) are specifically built for the Site Editor.

Examples: the [Query Loop Block](../../blocks/theme/query.md) allows you to customize the look and feel of your post layout, the [Navigation Block](../../blocks/theme/navigation.md) lets you customize the site’s navigation menu, the [Site Title Block](../../blocks/theme/site-title.md) helps to customize the Site Title and more.

> [!NOTE]
> Check out the full list of [Theme blocks](../../blocks/README.md#theme-blocks).

#### Example – how to customize Twenty Twenty-Three using the Site Editor

[Twenty Twenty-Three](../themes/default-themes/twenty-twenty-three.md) supports the Site Editor and can be customized using it. The menu names and padding values below are specific to that theme and differ in other themes. As an example, let’s remove the gap at the top of the home page in Twenty Twenty-Three. To do this, remove the padding at the bottom of the header template part and the padding at the top of the content area.

![Before](https://wordpress.org/documentation/files/2023/08/before-editing-2023.jpg)

*Before*

![After](https://wordpress.org/documentation/files/2023/08/after-editing-2023.jpg)

*After*

First, remove bottom padding of Header Template Parts.

1.  From Administration Screen, Select **Appearance** > **Editor**
2.  Select **Patterns** > **Template Parts** > **Header** > **Header**, and click Pencil icon to edit it.
3.  Select the **Group** > **Row** block. Use the bottom block navigation.
4.  From Block Settings, Click Styles.

![Styles of Header Template Parts](https://wordpress.org/documentation/files/2023/08/header-styles-2023.jpg)

*Styles of Header Template Parts*

5.  Scroll down to the Padding > Bottom. Current value is 2.
6.  Set it to 0.
7.  Save the template parts.

Next, remove top padding of content area.

8.  Back to the Site Editor.
9.  Select Templates > Home, and click Pencil icon to edit it.
10. Select the top Group block. Use the bottom block navigation.
11. From Block Settings, Click Styles.

![Home Template Styles](https://wordpress.org/documentation/files/2023/08/home-templates-styles-2023.jpg)

*Home Template Styles*

12. Scroll down to the Padding > Top. Current value is 3.
13. Set it to 0.
14. Save the template.

### To browse the templates and template parts

From the Site Editor, you can easily browse the [templates](templates.md) and [templates parts](../../blocks/theme/template-part.md) available for your site.

-   Go to **Appearance** > **Editor** to open the Site Editor. This will bring you to a view where you can choose to browse your templates or template parts.
-   Click on **Templates** to preview the list of templates available for your site.
-   Click on **Patterns** to preview the list of template parts.

[Watch the video](https://wordpress.org/documentation/files/2022/01/site-editor-template-overview-6.6.mp4)

### To manage the site’s templates

WordPress uses [templates](templates.md) to create the layout and structure for specific page types on your site. The Site Editor displays the template choices that you can add to your site and lets you create custom templates using the [Template Editor](templates.md).

From the **Appearance** > **Editor**, you will be shown a view that includes a sidebar with your list of Templates and Patterns that includes the list of template parts.

[Watch the video](https://wordpress.org/documentation/files/2022/01/site-editor-templates-6.6.mp4)

> [!NOTE]
> Learn more about Templates in this support article: [Template Editor](templates.md).

### To manage the template parts

A Template part is a block for managing the repeating global areas of the site such as a Header, Footer, Sidebar, etc. They are primarily meant to define the site structure and can be reused. You can also create custom Template Parts that can be reused through the templates.

From the **Appearance** > **Editor**, click the **Patterns** option. From All templates parts, you can access to them.

[Watch the video](https://wordpress.org/documentation/files/2022/01/site-editor-template-parts-6.6.mp4)

> [!NOTE]
> Learn more about Template Parts in this support article: [Template Part](../../blocks/theme/template-part.md).

### To manage pages

Since version 6.3, it is possible to manage, edit and create pages via the Site Editor, under the “Pages” section.

[Watch the video](https://wordpress.org/documentation/files/2022/01/site-editor-pages-6.6.mp4)

> [!NOTE]
> Learn more about managing pages via the Site Editor in [Site Editor pages](#site-editor-pages).

## How to return to the Dashboard

To return to the dashboard, select your site's name in the WordPress toolbar at the top of the screen, then **Dashboard**. Use the **Back button** (the left-chevron icon) in the upper-left area of the Site Editor to return to the previous Site Editor screen.

The WordPress Toolbar remains available above the Site Editor and provides access to your site’s administration screens. If you have unsaved changes when leaving an editing view, WordPress will prompt you to save or review those changes before leaving.

![How to exit the Site Editor by clicking on the Back button.](https://wordpress.org/documentation/files/2026/08/site-editor-return-to-dashboard.jpg)

## How to export templates and styles

You can export your theme with the changes you made in the Site Editor, including the templates, template parts, and style settings.

-   Open the Site Editor by going to **Appearance** > **Editor**.
-   Select the three vertical dots icon next to your **Styles** settings option.
-   Under **Tools**, select **Export**. This will begin the export process and you will receive a downloaded zip file of your theme with the templates and template parts included.

![How to find the "Export" option under the three-dot "More Options" menu on the top right part of the screen.](https://wordpress.org/documentation/files/2023/08/Screen-Shot-on-2023-08-05-at-073719.png)

## Useful tools when using the Site Editor

The following tools are helpful when using the Site Editor.

### The Command Palette

The Command Palette offers you a quick way to navigate the **content** of your site and to invoke different **actions** such as creating new posts/pages, toggling preferences, and accessing your styles and custom CSS settings.

You can open the Command Palette from the WordPress Admin bar while working in the Site Editor. In Site View, you can also access it from the search control in the Site Editor navigation. You can open it from the keyboard with `Cmd+K` on macOS or `Ctrl+K` on Windows and Linux.

[Watch the video on VideoPress](https://videopress.com/v/pPGxe58s)

> [!NOTE]
> Learn more about the Command Palette in this support article: [Site Editor Command Palette](command-palette.md).

### List View

List View helps you navigate complex block layouts and nested block structures. You can select exactly which block you need, and get a quick overview of the block layout on the page you are working on. You can easily select multiple blocks and edit, move or group them.

[Watch the video](https://wordpress.org/documentation/files/2023/08/site-editor-list-view.mp4)

> [!NOTE]
> Learn more about List View in this support article:  [List View](../../write/blocks/list-view.md).

### Block patterns

Block Patterns are a collection of predefined blocks that you can insert into posts and pages. You can then customize them further. WordPress comes with a set of standard Block Patterns. You can also find Block Patterns bundled with the [block themes](../themes/block-themes.md).

> [!NOTE]
> Learn more about Block Patterns in this support article: [Block Pattern](../patterns/README.md).

### Copy and paste styles

With WordPress 6.2, a new option was added to allow you to copy and paste block styles, making it easy to reuse designs you’ve created. You can find this from the three dot menu in any block and it’s meant to be used to copy and paste between the same type of block:

[Watch the video](https://wordpress.org/documentation/files/2023/08/site-editor-copy-paste-styles.mp4)

### Apply style changes globally

If you’re more comfortable with more advanced options when creating a design or customizing individual blocks, as of WordPress 6.2, you can take changes made to an individual block and apply it to **all blocks of the same type**. For example, you could apply a single design for an individual block to all blocks in your site with a new option under the **Advanced** section of block settings.

![How to apply the current's block style to all styles of that same type across your site by clicking on Block Settings > Advanced > Apply Globally](https://wordpress.org/documentation/files/2023/08/site-editor-apply-styles-globally.png)

### Resize the preview of the Site Editor

When you’re in the Site Editor, you might want to change the preview of the template or template part you’re viewing. You can do this by selecting the handles of the dark gray sidebar and moving it to your liking.

[Watch the video](https://wordpress.org/documentation/files/2023/08/site-editor-resize-pattern-preview.mov)

### Zoom out mode

![Zoom out toggle](https://wordpress.org/documentation/files/2021/01/zoom-out-toggle.png)

Zoom Out View provides a condensed visual overview of the entire page structure, enabling users to quickly assess the hierarchy, placement, and design of individual sections without having to scroll through each block in detail.

> [!NOTE]
> [Learn more about Zoom out mode.](#zoom-out-view)

## Resource links

-   [Additional guide to using the Site Editor](#additional-guide-to-using-the-site-editor)
-   [Simple Site Design and Site Editing](https://learn.wordpress.org/course/simple-site-design-with-full-site-editing/)
-   [Intro into the Site Editor and Template Editor](https://learn.wordpress.org/workshop/intro-to-the-site-editor-and-template-editor/)

## Additional guide to using the Site Editor

### How to update what your homepage displays

Your homepage can show a list of your latest blog posts or a static page with custom content. Which setting you use depends on the templates that are included in your theme. To view the list of templates, go to the Administration Screen > Appearance > Editor > Templates.

-   If your theme does not have a Home or Front page template, select the Add New button and create a new Front Page.
-   If your theme has a Front Page template, click on the link with the template name to open the editor.
-   If your theme has a Home template, you can edit the template or set what you want to appear in the Administration Screen > Settings > Reading.

To learn how to select a static page for your homepage, please see the support article [Creating a Static Front Page](../../write/organize/static-front-page.md).

### How to customize your homepage

**Latest Blog Posts**

To customize your blog, go to Administration Screen > Appearance > Editor. The editor will open to your homepage, and you can start editing.

Block themes display lists of blog posts with the Query Loop block and the Post Template block.

The [support article for the Query Loop Block](../../blocks/theme/query.md) explains how to configure the block.

When you add a block inside the post template block, it is repeated for every post in the list. The Post Title and Post Featured Image, Post Author, Post Date, Post Category, and Post tags are examples of blocks that you can use to customize your blog.

**Static page**

If you have selected a static page for your home page, and you want it to have a different design than other pages, you need to assign it a different template.

Follow these steps to assign an existing template:

1.  From your wp-admin dashboard, head to Pages > All Pages.
2.  From the list of pages, select the option to edit page you have set as your home page.
3.  Once in the editor, open the settings sidebar.
4.  Under “Template”, you can then select whatever Template you want your home page to use.
5.  When you’re done, select **Save** to save the changes.

Follow these steps to create a new template:

1.  From your wp-admin dashboard, head to Pages > All Pages.
2.  From the list of pages, select the option to edit page you have set as your home page.
3.  Once in the editor, open the settings sidebar.
4.  Under “Template”, select New.
5.  This will open the Site Editor to add blocks for create your template for your static homepage.
6.  When you’re done, select **Save** to save the changes.

Please note that if you add a Front Page template in the Site Editor, it will always be used as the front page regardless of what setting you choose under Admin > Settings > Reading. You will need to either customize that template to your liking or remove it to then adjust the homepage settings again.

### How to update your site icon

Block themes include the ability to use the Site Logo block which has built within it an option to set your Site Logo as your Site Icon. For context, the Site Logo displays whatever logo you set for your site whereas your Site Icon is also known as a favicon and it is used to help identify your website. To learn more about setting your Site Icon or favicon, please see the support article [Creating a Favicon](site-icon.md).

Follow the steps below to use the same image for the Site Logo and Site Icon:

1.  Head to Appearance > Editor. This will open up your homepage.
2.  Either find your Site Logo block added by your theme or add it to yourself wherever you’d like. Detailed instructions for adding blocks [can be found here](../../write/blocks/add-a-block.md).
3.  From there, you’ll see the option to upload or select an image to use from your Media Library.
4.  After choosing an image and while still selecting the Site Logo block, open the block settings sidebar (uses the cog icon).
5.  Under the settings for the Site Logo block, toggle on the option to “Use as site icon”.
6.  Save your changes.

![Image showing the options to set a site logo as a site icon in the settings sidebar.](https://wordpress.org/documentation/files/2022/01/site_icon.png)

### How to customize your site design at a global level

Since WordPress 5.9, you can set the colors, typography, layout, spacing, and more, for the entire site via Styles. You can also edit the default appearance of blocks to streamline the look and feel of your site.

For more details, refer [Styles Overview](styles.md).

## Site Editor pages

Site Editor Pages is a page editing and page management tool in the Site Editor where you can create, view, edit, and trash pages. It shows your page content as part of the template instead of using placeholder content.

> [!NOTE]
> The Site Editor Pages menu is **only** available when you install and activate a [block theme](../themes/block-themes.md) on your site. You can learn about the Site Editor in this support article: [Site Editor](README.md).

In Site Editor Pages, you can edit both the page content and the template. The template is locked until you enable the template editing option.

Here you will also find the page details like information about the page status (for example, if a page is a draft or published) when the page was last updated, the number of words on the page, and how long it will take to read.

### How to access Site Editor pages

Once you install and activate a Block theme on your site, go to **Appearance** > **Editor** to open the Site Editor. In the sidebar menu, select **Pages**:

![The WordPress Site Editor with a menu on the left and a preview of the website to the right.](https://wordpress.org/documentation/files/2023/07/63-site-editor-pages-first-menu.jpg)

### Sidebar features

When you select **Pages**, WordPress shows a sidebar with a list of pages, page-related shortcuts, and an option to create new pages.

To go back to the WordPress dashboard, use the toolbar above the Site Editor.

At the top of the sidebar are your site title and a button that opens the [Command Palette](command-palette.md). You will recognize the Command Palette button by the icon of the magnifying glass. You can select the back button if you want to go back to the main Site Editor menu.

![The page sidebar with a menu with all pages that are published or drafts.](https://wordpress.org/documentation/files/2023/07/63-pages-sidebar-inner.png)

#### Page list

The page list includes all pages on your site that are either published or drafts. Each page in the page list is represented by an icon. Your front page uses an icon of a house. And if your site shows blog posts on a [separate page](../../manage/settings/reading.md), the blog page uses an icon of a feather pen.

Clicking on the page title opens the page and the page details sidebar.

#### Shortcuts

At the bottom of the sidebar are links that help you edit your site faster: Links to the 404-page template, the Search Results template, and Manage all pages, which takes you to the [Pages screen](../../write/create-a-page.md#pages-screen) in the WordPress admin.

#### Save status

If you have unsaved changes to the page or the template, the save button at the bottom of the sidebar will be activated and highlighted with a blue background.

If there are unsaved changes to both the template and the page, you can review the changes before you save. Clicking the button opens a save modal where you can select if you want to save all changes:

![The save modal lists unsaved changes together with a checkbox. The checkbox is checked by default. At the top of the modal is a save button and a cancel button.](https://wordpress.org/documentation/files/2023/07/63-site-editor-pages-review-changes.png)

#### The page details sidebar

This sidebar displays the name of the chosen page, a preview link for the front of the website, the featured image (if one exists), and a description.

**Page details:**

-   Status – Draft or publishing date
-   Slug
-   Template – The name of the template that the page uses
-   Words – The number of words in the content
-   Time to read
-   Last modified

![The page details sidebar displays information about the page below the page title.](https://wordpress.org/documentation/files/2023/07/63-site-editor-page-details-sidebar.png)

The ellipsis menu next to the page title opens a modal where you can trash the page:

![The "Move to Trash" button.](https://wordpress.org/documentation/files/2023/07/63-site-editor-page-trash.png)

The pen icon represents editing: it redirects you to where you can edit the page in the Site Editor.

#### The blog page details sidebar

Different types of pages show different details in the sidebar. When you select a page that displays the latest posts, you can update settings related to your blog directly in the sidebar. You can:

-   Edit the page title
-   Select the number of posts per page
-   Allow or disallow comments

There are also two shortcuts to editing your site header and site footer.

![The blog page details sidebar](https://wordpress.org/documentation/files/2023/07/63-site-editor-page-blog-details-sidebar.png)

### Create new pages in the Site Editor

You can click the **plus icon** on the Site Editor Pages sidebar to draft a new page. Selecting this button opens a new modal where you can add an optional page title:

![The modal has an input field for adding a page title, a close button, a cancel button and a button that submits the form, with the text "Create draft".](https://wordpress.org/documentation/files/2023/07/63-site-editor-pages-new-draft-title.png)

Selecting the **Create draft** button in the modal creates a new draft and redirects you to the screen where you can edit the new page.

### Edit pages in the Site Editor

To start editing a page in the Site Editor, click anywhere in the preview window or select a page from the Pages menu and click the pen icon.

When you edit pages in the Site Editor, you can see your page content in the template. Depending on the template, you may see your site header, the page content, and your site footer:

![The Site Editor displays a single page. The list view is opened and the blocks have icons that show that they are locked. The settings sidebar shows that the Pages template is used for this page.](https://wordpress.org/documentation/files/2023/07/63-site-editor-page-editing.png)

In the top right corner is a save button, a toggle button that opens the settings sidebar, a button that opens the [Styles interface](styles.md), and an options menu.

The page settings tab has four panels:

-   The page title
-   A summary panel with information about the page status and the publishing date.
-   The content panel lists the editable blocks, such as the title and post content blocks.
-   The template panel shows the name and preview of the current template.

**Status:**

You can use the status option in the summary panel to change the page to a draft, schedule it, or add a password:

![The status option is a modal where you can choose the page's publishing status from a row of radio boxes. Draft, pending, private, scheduled and published.](https://wordpress.org/documentation/files/2023/07/63-site-editor-pages-summary-panel-status.png)

**Publish:**

You can use the publish option in the summary panel to change the publishing date of the page. You can enter a date and time using the input fields or select a date from the calendar. You can use the arrow buttons to change the month of the calendar.

![The publish option displays input fields for date and time.](https://wordpress.org/documentation/files/2023/07/63-site-editor-pages-summary-panel-publish.png)

#### Locked and editable blocks

Blocks in the **template** are locked and can not be selected without enabling the **Edit template** option. This prevents accidental editing of the template.

The blocks in the **content panel** in the settings sidebar can be edited, but not moved or deleted. These blocks can be selected, but do not have a block toolbar. Clicking on a block in the content panel selects the block in the editor.

In the example image below, the content panel includes a post featured image, the title block, and the post content block.

-   Selecting the post featured image block will let you upload or add an image from the media library, but you can not remove the block.
-   Selecting the title block will let you change the page title. But you can not change the title’s color or font size.

![Content panel with options for featured image, title, and post content.](https://wordpress.org/documentation/files/2023/07/63-site-editor-pages-content-panel.png)

*The content panel in the settings sidebar*

Blocks that are **placed inside the Post Content block** are editable. You can add new blocks, edit, move, and remove blocks. **These are the same blocks that you would see in the block editor when editing the page.**

In this example image, the editable blocks are the paragraph and quote blocks:

![WordPress editor list view showing featured image, title, and post content blocks.](https://wordpress.org/documentation/files/2023/07/63-site-editor-pages-editing-list-view.png)

*The post featured image block, title, and post content blocks are locked in the list view. The blocks nested inside the post content block are unlocked and can be edited.*

### Enable template editing

When you click on a block in the template, WordPress shows a notification in the bottom left corner that says: Edit your template to edit this block.

![Edit template notification](https://wordpress.org/documentation/files/2023/07/63-site-editor-pages-template-blocks.png)

You can also enable template editing by selecting the “Edit template” button in the template panel in the settings sidebar:

![The template panel in the settings sidebar shows the name of the template, a preview, and a "Edit template" button.](https://wordpress.org/documentation/files/2023/07/63-site-editor-pages-editing-settings-template-panel.png)

Now you are redirected, and you can make changes to the template.

To go back to the page, you can use the back button above the editor:

![The toolbar at the top of the editor.](https://wordpress.org/documentation/files/2023/07/63-site-editor-pages-template-back.png)

Or, you can click on the WordPress logo or site icon in the top left corner to open the Site Editor sidebar.

### Resource links

-   [Site Editor](README.md)
-   [Create Pages](../../write/create-a-page.md)

## Zoom out view

The Zoom out view is a powerful editing mode in the WordPress Site Editor that allows users to get a broader, high-level perspective of their page layout. It is designed to enhance usability and streamline the design workflow, especially when managing full-page layouts or working with multiple template parts.

This mode is particularly useful for:

-   Designers reviewing the page’s visual flow.
-   Site administrators applying consistent section styles across multiple blocks.
-   Users managing complex templates with multiple content areas.

### How to use Zoom out

To access the Zoom out view, click on the icon that looks like two arrows pointing away from each other near the settings toggle at the top of the editor.

![Zoom out view location](https://wordpress.org/documentation/files/2019/03/zoom-out-toggle.png)

You can also use keyboard shortcuts to toggle Zoom out mode on and off:

-   Windows: **Ctrl + Shift + `0`**
-   Mac: **⇧ + ⌘ + 0**

> [!NOTE]
> [Learn more about keyboard shortcuts.](../../write/editor/keyboard-shortcuts.md)

#### When editing a page

When editing a page while using a block theme, choose **Show template** to view the page content with the shared theme elements such as header and footer. From here you will see the Zoom out toggle.

[Watch the video on VideoPress](https://videopress.com/v/WFbkdPm1)

> [!NOTE]
> The Zoom out icon is only visible when **Show Template** is activated within the Preview setting.

#### In the Site Editor

When you insert a pattern into a template while using the Site Editor, you will automatically enter Zoom out mode. Press the Zoom out toggle button to return to the default view.

[Watch the video on VideoPress](https://videopress.com/v/UYoUOaIm)

> [!NOTE]
> [Learn more about the Site Editor.](README.md)
