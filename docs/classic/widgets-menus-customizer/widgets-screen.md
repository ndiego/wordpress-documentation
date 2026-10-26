---
title: Widgets screen
description: "Add, arrange and remove widgets in a classic theme's widget areas on the Appearance > Widgets screen."
type: reference
order: 20
redirect_from:
  - /documentation/article/appearance-widgets-screen-classic-editor/
  - /documentation/article/manage-wordpress-widgets/
---

# Widgets screen

**Note:** This is documentation for the Classic Widgets Screen. The documentation for the [Block-based Widgets editor can be found here.](block-widgets-editor.md)

Themes usually have at least 1 or 2 sidebars. Each section in the sidebar is known as a “Widget” that you can add or remove, and move up or down. You configure Widgets in your sidebar by via the **Appearance Widgets Screen**. Some themes also are configured to accept widgets in certain parts of the footer and header.

[![](https://wordpress.org/documentation/files/2019/01/wigets-screen.png)](https://wordpress.org/support/?attachment_id=11132735)

*widgets screen*

## Widgets management in Customizer

You can add, rearrange and remove Widgets just like in Appearance Widgets Screen, but you also get a live preview of your changes. From the Appearance Widgets Screen, click the “Manage in Customizer” link at the top to access the Widgets section of Theme Customizer.

### Configuring your widgets

1.  Click on **Appearance > Widgets** from the main navigation menu in your Dashboard.
2.  Add new widgets from the Available Widgets section by dragging them
    to the Sidebar you want to customize. (There might be more than one
    sidebar option, depending on your theme.)
3.  Preview your site and you should see the content from your new Widget.
4.  Return to the Widgets Screen to continue adding Widgets to the Sidebar as needed.
5.  To arrange the Widgets within the Sidebar, **click, drag and drop** the widgets in the order you want.
6.  To customize the Widget features, click the **down arrow** (or edit link) in the upper right corner to expand the Widget’s interface.
7.  To save the Widget’s customization, click **Save**. (If simply moving a widget to the sidebar without making customizations, you do not need to click the Save button.)
8.  Preview your site again, and all of your changes should be visible.

### Remove a widget

1.  Click on **Appearance > Widgets** from the main navigation menu in your Dashboard.
2.  Decide which Sidebar from which you want to remove your widget if there is more than one option.
3.  For the Widget that is to be removed, click the **down arrow** (or edit link) in the upper right corner to expand the Widget’s interface
4.  Click the **Delete** link in the dialog box.
5.  The Widget will now be removed permanently.
6.  Preview your site to see your changes.

**Note:** If you would like to remove a widget temporarily and
keep your settings, drag the widget from the Sidebar into the Inactive
Widgets section. When you are ready to return the widget, drag it from
your Inactive Widgets section back to the Sidebar.

### Moving a widget

To move a Widget:

1.  The Widget must be located in a Sidebar or other active content area before it can be moved.
2.  Click on the Widget Title and hold the mouse button down, then drag
    the Widget bar up or down to the location desired. At that point
    release the mouse button. That process is called drag-and-drop.

### Descriptions of each widget

Here’s a description of the various types of widget along with their configuration options:
**Archives** – displays archive links for each month that has posts.

-   Title: description that appears over the list of archive links.
-   Display as a drop down: if checked, this box causes the archives to be displayed in a drop-down box.
-   Show post counts: if checked, this box causes a count of the number of posts for each archive period.

**Calendar** – displays a calendar of the current month. Dates appear as links if there are posts for that day.

-   Title: description that appears over the calendar

**Categories** – displays a list of post categories as links to those posts.

-   Title: description that appears over the list of categories.
-   Display as dropdown: if checked, this box causes the categories to be displayed in a dropdown box.
-   Show post counts: if checked, this box causes the count of the number of posts to display with each category.
-   Show hierarchy: if checked, shows parent/child relationships in an indented manner.

**Custom Menu** – displays a custom menu.

-   Title: description that appears over the menu
-   Select Menu: select the desired created menu

**Meta** – displays links to meta functions such as Register, Site Admin, Login/out, Entries RSS, Comments RSS, and WordPress.org.

-   Title: description that appears over the list of meta links.

**Pages** – displays a link to each Page.

-   Title: description that appears over the list of pages.
-   Sort by: select the order to sort the list of pages. Choose Page Title, Page Order, or Page ID from pulldown box
-   Exclude (Page IDs, separated by commas): enter the Page ID(s) to exclude, separating each Page ID with a comma

**Recent Comments** – displays a list of the blog’s most recent approved comments.

-   Title: description that appears over the list of recent comments.
-   Number of comments to show: (at most 15); enter the number of comments to be displayed.

**Recent Posts** – displays list of the blog’s most recent posts.

-   Title: description that appears over the list of recent posts.
-   Number of posts to show: (at most 15): enter the number of posts to display.
-   Display post date?: check this to display the date the post was published.

**RSS**  – displays an RSS Feed. Multiple instances of this widget can be added to the Current Widgets list.

-   Enter the RSS feed URL here: enter a complete feed URL.
-   Give the feed a title (optional): enter a description that appears over the list of feed items
-   How many items would you like to display?: enter the number of items from the feed you want displayed.
-   Display item content?: check this to display the content of the feed
-   Display item author if available?: check this to display the author of this particular item content
-   Display item date?: check this to display the date the item was published

**Search** – displays a Search box to enter text to search your blog. A submit button is also provided.

-   Title: description that appears over the Search box.

**Tag Cloud** – displays list of the blog’s top 45 used tags in a tag cloud.

-   Title: description that appears over the tag cloud.
-   Taxonomy: select the desired registered taxonomy (e.g. Tags, Category).

**Text** – used to enter HTML, JavaScript, or just plain text. Multiple instances of this widget can be added to the Current Widgets list.

-   Title area: a description of the text widget
-   Text area: use this area to enter text, valid HTML, or even valid JavaScript.
-   Automatically add paragraphs: check this to automatically add
    paragraphs to wrap each block of text in an HTML paragraph tag
    (recommended for text).

### Adding multiple widgets of the same kind

To add multiple text widgets, RSS widgets, or any other widgets, just
drag and drop the widget from Available Widgets to your Sidebar as many
times as you need.

### No sidebars defined

If the current active Theme is not widget compatible, meaning the
theme is not coded for widgets, you will see the message, “You are
seeing this message because the theme you are currently using isn’t
widget-aware, meaning that it has no sidebars that you are able to
change. For information on making your theme widget-aware, please [follow these instructions](http://automattic.com/code/widgets/themes/)“.

## Manage WordPress widgets

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/manage-wordpress-widgets/; edit it into the page. -->

> [!NOTE]
> This article covers “Classic Widgets”. If you are using the newer block-based widgets, please check [this article](block-widgets-editor.md).

WordPress widgets add content and functionality to the widget area. The widget area is a pre-defined area by the theme, typically located in the sidebar or footer, but varies from theme to theme. Examples are the default widgets that come with WordPress; for Categories, Tag cloud, Search, etc. Plugins will often add their own widgets.

Widgets were originally designed to provide a simple and easy-to-use way of giving design and structure control of the WordPress Theme to the user, which is now available on properly “widgetized” WordPress Themes to include the header, footer, and elsewhere in the WordPress design and structure.

Widgets require no code experience or expertise. They can be added, removed, and rearranged on the **Theme Customizer** or **Appearance > Widgets** in the WordPress Administration Screens.

Some WordPress Widgets offer customization and options such as forms to fill out, includes or excludes of data and information, optional images, and other customization features.

The [Block-based Widgets Editor](block-widgets-editor.md) explains how to use the updated Widgets experience with blocks.

The [Appearance Widgets Screen](widgets-screen.md) explains how to use the various Widgets that come with WordPress in the Classic experience.

Plugins that come bundled with widgets can be found in the [WordPress Plugin Directory](https://wordpress.org/extend/plugins/).

### Installing widgets

WordPress comes pre-packaged with a variety of [Widgets](../../get-started/glossary.md#widget). If those are insufficient for your needs you can install new ones by searching the [WordPress Plugin Directory](https://wordpress.org/extend/plugins/) which is accessible from the WordPress Administration **Plugins > Add New** Screen.

### Displaying widgets

#### Existing widgets in existing widget areas

Before you can add a Widget you must verify that the Theme you’re using supports Widgets (more specifically: [Widget Area](../../get-started/glossary.md#widget-area)). You can do so by simply navigating to the Appearance menu and looking for a sub menu titled “Widgets”.

If your Theme supports Theme Customizer then you can use the following Steps. In Theme Customizer, the live preview of changes is available.

![](https://wordpress.org/documentation/files/2018/10/appearance-customize-widgets.png)

1.  Go to **Appearance > Customize** in the WordPress Administration Screens.
2.  Click the **Widget** menu in the Theme Customizer to access to the Widget Customize Screen.
3.  Click the **down arrow** of Widget Area to list the already registered Widgets.
4.  Click Add a Widget button at the bottom of sidebar. It shows the list of available widgets.
5.  Click a widget you want to add. The widgets should be added in the sidebar.
6.  Preview your site and you should see the content from your new Widget.
7.  To arrange the Widgets within the Sidebar, drag and drop the widgets in the order you want or click Reorder link and click up arrow and down allow of each widget and click Done after the arrange operation.
8.  To customize the Widget features, click the **down arrow** in the right to expand the Widget’s interface.
9.  To remove the widget, click **Remove** from Widget’s interface in above step.

If your Theme does not support Theme Customizer then you can use the following conventional steps:

![](https://wordpress.org/documentation/files/2018/10/designwidget-2.png)

1.  Go to **Appearance > Widgets** in the WordPress Administration Screens.
2.  Choose a Widget and either drag it to the sidebar where you wish it to appear, or click the widget, (select a destination sidebar if your theme has more than one) and click the Add Widget button. There might be more than one sidebar option, so begin with the first one. Once in place, WordPress automatically updates the Theme.
3.  Preview the site. You should find that the “default” sidebar elements are now gone and only the new addition is visible.
4.  Return to the Widgets Screen to continue adding Widgets.
5.  To arrange the Widgets within the sidebar or Widget area, click and drag it into place.
6.  To customize the Widget features, click the down arrow in the upper right corner to expand the Widget’s interface.
7.  To save the Widget’s customization, click Save.
8.  To remove the Widget, click Delete.

If you want to remove the widget but save its setting for possible future use, just drag it into the Inactive Widgets area. You can add them back anytime from there. This is especially helpful when you switch to a theme with fewer or different widget areas.

When changing themes, there is often some variation in the number and setup of widget areas/sidebars and sometimes these conflicts make the transition a bit less smooth. If you changed themes and seem to be missing widgets, scroll down on the screen to the Inactive Widgets area, where all of your widgets and their settings will have been saved.

Enabling Accessibility Mode, via Screen Options, allows you to use Add and Edit buttons instead of using drag and drop.

#### Widget areas

While widget areas typically occur in webpage sidebars, a theme can place widget areas anywhere on a page. For example, besides the usual sidebar locations, the [Twenty Seventeen](../../design/themes/default-themes/twenty-seventeen.md) theme has a widget area in the footer of every page.

### Using text widgets

The Text Widget is one of the most commonly used WordPress Widgets that comes with every WordPress installation. It allows users to add text, video, images, custom lists, and more to their WordPress sites.

To use the WordPress Text Widget:

1.  Go to **Appearance > Customize** in the WordPress Administration Screens and click the **Widget** menu in the Theme Customizer. Or Go to **Appearance > Widgets** in the WordPress Administration Screens.
2.  Open the sidebar to which you wish to add the Text Widget.
3.  Find the Text Widget in the list of Widgets.
4.  Click and drag the Widget to the spot you wish it to appear.

To open and edit the Text Widget:

1.  Click the down arrow to the right of the Text Widget title.
2.  Set the Text Widget Title (optional).
3.  Add the text or HTML code to the box or edit what is currently there.
4.  Choose the option to **Automatically add paragraphs** to wrap each block of text in an HTML paragraph tag (recommended for text).
5.  Click Save to save the Text Widget.
6.  Click Close to close the Text Widget.
7.  Switch tabs in your browser and preview the results and make changes if necessary.

The Text Widget can hold a variety of HTML, XHTML, and multimedia links and players such as video and object embeds.

#### Adding code to the text widget

Basic HTML, embeds, and JavaScript are added easily to the WordPress Text Widget. Most embed codes from social sharing sites for multimedia will work in a WordPress Text Widget. However, active code and programming languages such as PHP will not work as the Widget will strip out code it cannot display.

To add active code to the Text Widget, use one of the many WordPress Plugins from the [WordPress Plugin Directory](https://wordpress.org/plugins/) that override WordPress restrictions on using PHP in posts. Check that they will work on Widgets as some will not.

### Using RSS widgets

The RSS Widget allows you to integrate an external feed source for content into a Widget area of your site, such as your Twitter account, Facebook posts, Google+ posts, or other blogs.

The RSS Widget displays the most recently published content from any source with an active feed. This is an ideal way of integrating outside content into your site.

By default, WordPress RSS Widget displays the post title or the first 100 or so characters of a Tweet or long untitled post. These are either in the form of a link or features a link to the original source depending upon the feed’s design and structure.

1.  Enter the RSS feed URL in the first box, copied from the source page for the content you wish to include in your sidebar or other widgetized space.
2.  Give the feed a title: This is optional and gives you the chance to showcase the source of the content.
3.  How many items would you like to display?: By default, 10 are show, but you can choose from 1-20 posts.
4.  Display item content?: This allows you to show an excerpt of the content not just the title.
5.  Display item author if available?: If you wish to give credit to the original author of the content, check this to display the author.
6.  Display item date?: If available, the date of the original content will be shown.

You may add multiple RSS Widgets for incoming feeds to your WordPress sidebar and other widgetized areas of your site.

### Resources

-   [WordPress Widgets Announcement (historical reference)](https://wordpress.org/development/2006/03/widgets-plugin/)
