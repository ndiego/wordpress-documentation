---
title: Glossary
description: Definitions of the terms used in WordPress and in this documentation.
type: reference
order: 90
redirect_from:
  - /documentation/article/wordpress-glossary/
  - /documentation/article/wordpress-semantics/
---

# Glossary

The words you meet in WordPress and in this documentation, from *absolute path* to *XML-RPC*, in alphabetical order. Each entry links to related entries and, where there is one, to the page that covers the topic in full.

<!-- Add only terms with a meaning specific to WordPress, not generic ones such as API or PHP. -->

## Absolute path

*(also known as a **full path**)*

The complete location of a file or directory within a computer filesystem. An absolute path starts at the root directory (or drive letter) and continues up the directory hierarchy until the specific file or directory is reached. This contrasts with a [relative path](#relative-path), which does not start at the root directory.

The syntax of absolute paths differs by operating system. On Microsoft Windows, they begin with a drive letter and use a backslash to separate directory names. Absolute paths on macOS and Linux lack drive letters and use a forward slash as the directory separator.

Examples:

-   Windows: `C:\Users\Matt\www\blog\images\icecream.jpg`
-   macOS: `/Users/Matt/www/blog/images/icecream.jpg`
-   Linux: `/home/Matt/www/blog/images/icecream.jpg`

To find the absolute filesystem path of the directory containing a web page, copy the code below into a new text file, save the file as *path.php* (thus making a simple PHP web page), and move that file to your [web server](#web-server). Then direct your web browser to the [URL](#url) address of that file (e.g. *<http://www.example.com/path.php>*).

```php
<?php
echo getcwd();
?>
```

See also: [Path (computing) at Wikipedia](http://en.wikipedia.org/wiki/Path_(computing))

## Absolute URI

*(also known as a **full URI**)*

A URI that contains the complete location of a resource (as opposed to a [relative URI](#relative-uri)).

Examples:

-   `http://www.example.com/blog/images/icecream.jpg`
-   `ftp://ftp.example.com/users/h/harriet/www/`

## Action

In WordPress, an action is a [PHP function](http://www.w3schools.com/php/php_functions.asp) that is executed at specific points throughout the WordPress Core.

Developers can create a **custom** Action using the [Action API](https://developer.wordpress.org/reference/functions/add_action/) to add or remove code from an existing Action by specifying any [existing Hook](https://developer.wordpress.org/apis/hooks/action-reference/). This process is called “[hooking](#hook)“.

**For example:** A developer may want to **add** code to the footer of a Theme. This could be accomplished by writing new function, then Hooking it to the [wp_footer](https://codex.wordpress.org/Plugin_API/Action_Reference/wp_footer) Action.

**Custom Actions differ from custom *[Filters](#filter)*** because custom Actions allow you to **add or remove** code from existing Actions. Whereas custom Filters allow you to **replace** specific data (such as a variable) found within an existing Action.

-   See also: [Filter](#filter), [Hook](#hook), [Terminology Confusion](#terminology-confusion)
-   Related articles: [Actions](https://developer.wordpress.org/plugins/hooks/), [Action Reference](https://developer.wordpress.org/apis/hooks/action-reference/), [add_action()](https://developer.wordpress.org/reference/functions/add_action/)
-   Forum posts: [Filters vs. Actions Discussion and Explanation](https://wordpress.org/support/topic/fliters-vs-actions-from-a-newbe)

## Admin bar

An area of the screen just above your site that gives you quick
access to features such as adding a new post or editing your profile.
It is only visible if you are logged in.

The admin bar concept was added to WordPress in [Version 3.1](https://wordpress.org/documentation/wordpress-version/version-3-1/) and was replaced by the [Toolbar](https://codex.wordpress.org/Toolbar) in WordPress [Version 3.3](https://wordpress.org/documentation/wordpress-version/version-3-3/). To turn it on (or off), open the Dashboard and navigate to [Administration](../manage/dashboard/README.md) > [Users](../manage/dashboard/README.md#your-profile) > [Your Profile](../manage/users/your-profile.md).

-   Related articles: [Toolbar](https://codex.wordpress.org/Toolbar)
-   See also: [Your Profile Screen](../manage/users/your-profile.md)

## Ajax

**Ajax** is a technique that web pages use to have the server perform certain processing without reloading the web page. For example, when you approve a comment in a WordPress blog, WordPress uses Ajax to change the comment’s status, and you see the change without having to reload the Comments screen.

-   Related article: [AJAX](https://codex.wordpress.org/AJAX)
-   External link: [AJAX](http://en.wikipedia.org/wiki/Ajax) (Wikipedia)

## Apache

**Apache** is short for **[Apache HTTP Server Project](http://httpd.apache.org/)**, a robust, commercial-grade, featureful, and freely-available open source HTTP [Web server](#web-server) software produced by the [Apache Software Foundation](http://www.apache.org/). It is the most commonly used web server on the internet, and is available on many platforms, including Windows, [Unix](#unix)/[Linux](#linux), and [Mac OS X](#mac-os-x). Apache serves as a great foundation for publishing WordPress-powered sites.

## API

Please refer to [Wikipedia page](http://en.wikipedia.org/wiki/Application_programming_interface) for a definition.

## Array

An **array** is one of the basic data structures used in computer programming. An *array* contains a list (or *vector*) of items such as numeric or string values. *Arrays* allow programmers to randomly access data. Data can be stored in either *one-dimensional* or *multi-dimensional arrays*.

A one-dimension array seven (7) elements would be:

| 105 | 200 | 54 | 53 | 102 | 13 | 405 |
| --- | --- | --- | --- | --- | --- | --- |

The [Template Tag](https://developer.wordpress.org/themes/basics/template-tags/) [wp_list_categories()](https://developer.wordpress.org/reference/functions/wp_list_categories/) uses a one-dimensional array for the ‘exclude’ parameter.

An example of two-dimensional array, 7 by 3 elements in size, would be:

| 105 | 200 | 54 | 53 | 102 | 13 | 405 |
| --- | --- | --- | --- | --- | --- | --- |
| 15 | 210 | 14 | 513 | 2 | 2313 | 4512 |
| 501 | 500 | 499 | 488 | 552 | 75 | 1952 |

-   External links: [Array Programming at Wikipedia](http://en.wikipedia.org/wiki/Array_programming), [Array at freedictionary.com](http://encyclopedia.thefreedictionary.com/array)

## ASCII

**ASCII** (pronounced as “ask ee”) is a standard but limited [character set](#character-set) containing only English letters, numbers, a few common symbols, and common English punctuation marks. WordPress [content](#content) is not restricted to ASCII, but can include any [Unicode](#unicode) characters.

ASCII is short for **A**merican **S**tandard **C**ode for **I**nformation **I**nterchange.

-   External links: [ASCII](http://en.wikipedia.org/wiki/ASCII) (Wikipedia, with character set table)

## Atom

A format for syndicating content on news-like sites, viewable by Atom-aware programs called news readers or aggregators.

-   See also: [News reader](#news-reader), [RSS](#rss), [RDF](#rdf)
-   External links: [Atom (standard) at Wikipedia](http://en.wikipedia.org/wiki/Atom_(standard))

## Attribute sources

An object describing the attributes shape of a block. The keys can be named as most appropriate to describe the state of a block type. The value for each key is a function which describes the strategy by which the attribute value should be extracted from the content of a saved post’s content. When processed, a new object is created, taking the form of the keys defined in the attribute sources, where each value is the result of the attribute source function.

## Attributes

The object representation of the current state of a block in post content. When loading a saved post, this is determined by the attribute sources for the block type. These values can change over time during an editing session when the user modifies a block, and are used when determining how to serialize the block.

## Autosave

When you are writing or editing your posts and pages, the changes you
make are automatically saved every 2 minutes. In the lower right corner
of the editor, you’ll see a notification of when the entry was last
saved to the database.
Autosaves are automatically enabled for all posts and pages. There is
only one autosave for each post/page. Each new autosave overwrites the
previous autosave in the database.

-   Related articles: [Revision Management](https://codex.wordpress.org/Revision_Management)
-   External links: [WordPress.com Support – Autosave](http://en.support.wordpress.com/autosave/)

## Avatar

An **avatar** is a graphic image or picture that represents a user.

-   See also: [Gravatar](#gravatar)
-   Related articles: [Using Gravatars](../manage/users/gravatars.md)
-   External links: [Avatar (computing) at Wikipedia](http://en.wikipedia.org/wiki/Avatar_%28computing%29)

## Back end

The back end is the area that authorized users can sign into to add,
remove and modify content on the website. This may also be referred to
as “WordPress”, “admin” or “the administration area”.

## Binaries

**Binaries** refer to compiled computer programs, or executables. Many [open source](http://en.wikipedia.org/wiki/Open_source) projects, which can be re-compiled from [source code](http://en.wikipedia.org/wiki/Source_code), offer pre-compiled binaries for the most popular platforms and operating systems.

## Block

The abstract term used to describe units of markup that, composed together, form the content or layout of a webpage. The idea combines concepts of what in WordPress today we achieve with shortcodes, custom HTML, and embed discovery into a single consistent API and user experience.

## Block (inserter) library

Primary interface for selecting from the [available blocks](../blocks/README.md), triggered by plus icon buttons on Blocks or in the top-left of the editor interface.

## Block categories

These are not a WordPress taxonomy, but instead used internally to sort blocks in the Block Library.

## Block name

A unique identifier for a block type, consisting of a plugin-specific namespace and a short label describing the block’s intent. e.g. `core/image`

## Block styles

The CSS styles that are part of the block, either via its stylesheet or via the block markup itself. For example, a class attached to the block markup is considered block styles.

Compare to ***Global Styles***. In contraposition to Global Styles, block styles are sometimes referred to as [Local Styles](#local-styles).

Learn more about [Block Styles](https://github.com/WordPress/gutenberg/blob/trunk/docs/explanations/architecture/styles.md#block-styles).

## Block supports

An API for blocks to declare what features they support. By declaring support for a feature, the API would add additional [attributes](#attributes) to the block and matching UI controls for most of the existing block supports.

See [Block Supports reference documentation](https://github.com/WordPress/gutenberg/blob/trunk/docs/reference-guides/block-api/block-supports.md) for a deep dive into the API.

## Block template parts

Building on Block Templates, these parts help set structure for reusable items like a Footer or Header that one typically sees in a WordPress site. They are primarily site structure and are never to be mixed with the post content editor. With Full Site Editing and block based themes, users can create their own arbitrary Template Parts, save those in the database for their site, and re-use them throughout their site. Template parts are equivalent – in blocks – of theme template parts. They are generally defined by a theme first, carry some semantic meaning (could be swapped between themes such as a header), and can only be inserted in the site editor context (within “templates”).

## Block templates

A template is a predefined arrangement of blocks, possibly with predefined attributes or placeholder content. You can provide a template for a post type, to give users a starting point when creating a new piece of content, or inside a custom block with the `InnerBlocks` component. At their core, templates are simply HTML files of block markup that map to templates from the standard WordPress template hierarchy, for example index, single or archive. This helps control the front-end defaults of a site that are not edited via the Page Editor or the Post Editor. See the [templates documentation](https://developer.wordpress.org/block-editor/developers/block-api/block-templates/) for more information.

## Block themes

A theme built in block forward way that allows Full Site Editing to work. The core of a block theme are its block templates and block template parts. To date, block theme templates have been HTML files of block markup that map to templates from the standard WordPress template hierarchy.

## Block type

In contrast with the blocks composing a particular post, a block type describes the blueprint by which any block of that type should behave. So while there may be many images within a post, each behaves consistent with a unified image block type definition.

## Blog

A **blog**, or **weblog**, is an online journal, diary, or serial published by a person or group of people.

Blogs are commonly used by individuals, peer groups, companies, or organizations.

Blogs often contain public as well as private content. Depending on the functionality of the [CMS](#content-management-system) software that is used, some authors may restrict access, through the use of accounts or passwords, to content that is too personal to be published publicly.

## Blogging

**Blogging** is the act of writing in one’s blog. To *blog* something is to write about something in one’s blog. This sometimes involves [linking](http://en.wikipedia.org/wiki/Hyperlink) to something the author finds interesting on the internet.

-   See also: [Blogosphere](#blogosphere), [Blogroll](#blogroll)

## Blogosphere

The **blogosphere** is the subset of internet web sites which are, or relate to, [blogs](#blog).

-   See also: [Blog](#blog), [Blogroll](#blogroll)

## Blogroll

A **blogroll** is a list of links to various blogs or news sites. Often a blogroll is “rolled” by a service which tracks updates (using [feeds](#feed)) to each site in the list, and provides the list in a form which aggregates update information. The default blogroll (aka links) included in WordPress was removed in version 3.5.

-   See also: [Blog](#blog), [Blogosphere](#blogosphere), [Feed](#feed), [News reader](#news-reader)
-   External links: [News aggregator at Wikipedia](http://en.wikipedia.org/wiki/News_aggregator)

## Bookmarklet

A **bookmarklet** (or **favelet**) is a “faux” bookmark containing scripting code, usually written in [JavaScript](#javascript), that allows the user to perform a function.

Examples:

-   [Tantek’s favelets](http://tantek.com/favelets/)
-   [Wikipedia page](https://en.wikipedia.org/wiki/Bookmarklet) explains the concept and usage.

## Boolean

A variable or expression which evaluates to either true or false.

-   External links: [PHP Boolean data type](http://us2.php.net/manual/en/language.types.boolean.php)

## Category

Each [post](#post) in WordPress can be filed under one or more **categories**. Thoughtful categorization allows posts to be grouped with others of similar content and aids in the navigation of a site.

Please note that a **post** category should not be confused with a [**link** category](../manage/dashboard/README.md), which is used to classify and manage [links](../manage/dashboard/README.md).

## Capabilities

A **capability** is permission to perform one or more types of
task. Each user of a WordPress site might have some permissions but not
others, depending on their [role](#role).
For example, users who have the Author role usually have permission to
edit their own posts (the “edit_posts” capability), but not permission
to edit other users’ posts (the “edit_others_posts” capability).
WordPress comes with six roles and over fifty capabilities in its
role-based access system. Plugins can modify the system.

-   Related article: [Roles and Capabilities](https://codex.wordpress.org/Roles_and_Capabilities)
-   External link: [Role-based access control](http://en.wikipedia.org/wiki/Role-based_access_control) (Wikipedia)

## CGI

**CGI** (Common Gateway Interface) is a specification for [server-side](http://en.wikipedia.org/wiki/Server-side) communication scripts designed to transfer information between a [web server](#web-server) and a [web-client (browser)](http://en.wikipedia.org/wiki/Client-side). Typically, [HTML](#html) pages that collect data via forms use *CGI* programming to process the form data once the client submits it.

## Character entity

A **character entity** is a method used to display *special characters* normally *reserved* for use in [HTML](#html). For example, the *less than* (**<**) and *greater than* (**>**) are used as part the [HTML](#html) tag structure, so both symbols are *reserved* for that use. But, if you need to display those symbols on your site, you can use *character entities*. For example:
use **`&lt;`**  for the less than (<) symbol
use **`&gt;`**  for the greater than (>) symbol

-   Related articles: [Fun Character Entities](https://codex.wordpress.org/Fun_Character_Entities)

## Character set

A **character set** is a collection of symbols (letters, numbers,
punctuation, and special characters), when used together, represent
meaningful words in a language. Computers use an encoding scheme so
members of a character set are stored with a numeric value (e.g. 0=A,
1=B, 2=C, 3=D). In addition, a [collation](#collation) determines the order (i.e alphabetic) to use when sorting the character set.

By default, WordPress uses the Unicode UTF-8 (**utf8**) character set for the [WordPress MySQL database tables](https://codex.wordpress.org/Database_Description) created during the [installation process](https://codex.wordpress.org/Installing_WordPress). Beginning with [Version 2.2](https://wordpress.org/documentation/wordpress-version/version-2-2/), the database character set (and collation) is defined in the *wp-config.php* file.

-   See also: [Collation](#collation)
-   Related articles: [Editing wp-config.php](../manage/wp-config.md), [Converting Database Character Sets](https://codex.wordpress.org/Converting_Database_Character_Sets)
-   External links: [Character set at Wikipedia](http://en.wikipedia.org/wiki/Character_set), [Unicode at Wikipedia](http://en.wikipedia.org/wiki/Unicode), [UTF-8 at Wikipedia](http://en.wikipedia.org/wiki/UTF-8), [Character sets and collation at MySQL](http://dev.mysql.com/doc/refman/5.0/en/charset-general.html)

## chmod

**chmod** is a [Unix](#unix)/[Linux](#linux) [shell](#shell) command used to change [permissions](#permissions) on files. Its name is a contraction of “**ch**ange **mod**e.”

-   Related articles: [Changing File Permissions](https://developer.wordpress.org/advanced-administration/server/file-permissions/), [UNIX Shell Skills](https://codex.wordpress.org/UNIX_Shell_Skills), [htaccess for subdirectories](https://codex.wordpress.org/htaccess_for_subdirectories)

## Class

**Classes** are groupings of [CSS](#css) styles which can be applied to any [HTML](#html) element.
For classes in PHP, see the [Class (Computing)](http://en.wikipedia.org/wiki/Class#Computing) article at Wikipedia and [PHP Manual: Classes and Objects](http://php.net/manual/en/language.oop5.php).

-   Related articles: [CSS](https://codex.wordpress.org/CSS), [Blog Design and Layout](https://codex.wordpress.org/Blog_Design_and_Layout)

## Classic block

A block which embeds the TinyMCE editor as a block, TinyMCE was the base of the previous core editor. Older content created prior to the block editor will be loaded in to a single Classic block.

## Codex

The **Codex** is the series of articles that show users how to use
WordPress. WordPress users contribute documentation to the codex
voluntarily.

-   External links: [Codex](https://codex.wordpress.org/Main_Page)

## Collation

**Collation** refers to the order used to sort the letters, numbers, and symbols of a given [character set](#character-set). For example, because WordPress, by default, uses the UTF-8 (**utf8**) character set, and when the [WordPress MySQL database tables](https://codex.wordpress.org/Database_Description) are created during the [installation process](https://codex.wordpress.org/Installing_WordPress), MySQL assigns **utf8_general_ci** collation to those tables. Beginning with [Version 2.2](https://wordpress.org/documentation/wordpress-version/version-2-2/), the collation (and character set) used by WordPress is defined in the *wp-config.php* file.

-   See also: [Character set](#character-set)
-   Related articles: [Editing wp-config.php](../manage/wp-config.md), [Converting Database Character Sets](https://codex.wordpress.org/Converting_Database_Character_Sets)
-   External links: [Collation at Wikipedia](http://en.wikipedia.org/wiki/Collation), [Character set at Wikipedia](http://en.wikipedia.org/wiki/Character_set), [UTF-8 at Wikipedia](http://en.wikipedia.org/wiki/UTF-8), [Character sets and collation at MySQL](http://dev.mysql.com/doc/refman/5.0/en/charset-general.html)

## Comments

**Comments** are a feature of [blogs](#blog) which allow readers to respond to [posts](#post). Typically readers simply provide their own thoughts regarding the [content](#content) of the post, but users may also provide [links](http://en.wikipedia.org/wiki/Hyperlink) to other resources, generate discussion, or simply compliment the author for a well-written post.

You can control and regulate comments by filters for language and
content. Comments can be queued for approval before they are visible on
the web site. This is useful in dealing with [comment spam](../write/comments/comment-spam.md).

-   See also: [Blog](#blog)
-   Related articles: [Comment-related plugins](../manage/plugins.md), [Dealing with comment spam](../write/comments/comment-spam.md), [Settings Discussion SubPanel](https://codex.wordpress.org/Settings_Discussion_SubPanel)
-   External links: [Hyperlink at Wikipedia](http://en.wikipedia.org/wiki/Hyperlink)

## Content

**Content** consists of text, images, or other information shared in [posts](#post).
This is separate from the structural design of a web site, which
provides a framework into which the content is inserted, and the
presentation of a site, which involves graphic design. A [Content Management System](#content-management-system) changes and updates content, rather than the structural or graphic design of a web site.

## Content management system

A **Content Management System**, or **CMS**, is software for facilitating the maintenance of [content](#content), but not design, on a web site. A [blogging](#blog) tool is an example of a Content Management System.

-   See also: [Blog](#blog)

## cPanel

**cPanel** is a popular web-based administration tool that many [hosting providers](#hosting-provider) provide to allow users to configure their own accounts using an easy-to-use interface.

-   Related articles: [Using cPanel](https://codex.wordpress.org/Using_cPanel), [Adding New Themes by using cPanel](../design/themes/README.md)
-   External links: [cPanel website](http://cpanel.net/)

## CSS

**CSS**, or **Cascading Style Sheets**, is a [W3C](http://www.w3.org/) [open standards](http://en.wikipedia.org/wiki/Open_standard)
programming language for specifying how a web page is presented. It
allows web site designers to create formatting and layout for a web site
independently of its content.

-   Related articles: [CSS](https://codex.wordpress.org/CSS), [Blog Design and Layout](https://codex.wordpress.org/Blog_Design_and_Layout)
-   External links: [CSS at W3C](http://www.w3.org/Style/CSS/), [Open standards at Wikipedia](http://en.wikipedia.org/wiki/Open_standard), [W3C.org](http://www.w3.org/)

## CVS

**CVS** stands for **Concurrent Versions System** and is the software that used to be used to coordinate WordPress development. As of February 2005, this function is carried out by Subversion (SVN).

For more information on Subversion, see [Using Subversion](https://codex.wordpress.org/Using_Subversion).

## Dashboard

In WordPress a **Dashboard** is the main administration screen for
a site (a weblog), or for a network of sites. It summarizes information
about the site or network, and also external information, in one or
more [widgets](#widget) that the Dashboard user can enable, disable, and move around.

-   Related articles: [Dashboard Screen](https://codex.wordpress.org/Dashboard_Screen)

## Database

A **database** in computing terms is software used to manage information in an organized fashion. WordPress uses the [MySQL](#mysql) or [MariaDB](#mariadb) relational databases management system for storing and retrieving the content of your [blog](#blog), such as [posts](#post), [comments](#comments), and so on.

-   Related articles: [Database Description](https://codex.wordpress.org/Database_Description), [Backing Up Your Database](https://codex.wordpress.org/Backing_Up_Your_Database)

## Database version

In WordPress, the **database version** is a number that increases every time changes are made to the way WordPress organizes the data in its [database](#database). It is not the same as the version of the database software, [MySQL](#mysql) or [MariaDB](#mariadb).

For example, the database version in WordPress 3.3 was 19470, and
the database version in WordPress 3.3.1 did not change. This tells
anyone planning to use backed-up data from the older version that they
do not need to check for changes in the structure of the data.

WordPress stores its database version in the database, as the
option named “db_version” in every WordPress site’s “wp_options” table.
(The table name prefix “wp_” may be missing or different in some cases.)

-   Related articles: [Database Description](https://codex.wordpress.org/Database_Description), [How do you force a database upgrade?](https://codex.wordpress.org/FAQ_Installation#How_do_you_force_a_database_upgrade.3F)

## Default theme

Every installation of WordPress has a default theme. The default theme is sometimes called the **fallback theme**, because if the active theme is for some reason lost or deleted, WordPress will fallback to using the default theme.

## Deprecated

**Deprecated** functions or template tags are no longer supported, and will soon be obsolete.

-   Related articles: [“Deprecated Functions” Category](https://codex.wordpress.org/Category:Deprecated_Functions)

## Developer

A **developer**, or **dev**, is a computer programmer who is active in creating, modifying, and updating a software product.

-   Related articles: [Plugin API](https://developer.wordpress.org/plugins/hooks/)

## DIV

A **DIV** element in [HTML](#html) marks a section of text. DIVs are used extensively in WordPress to apply [CSS](#css) stylings to particular [blog](#blog) elements.

-   Related articles: [CSS](https://codex.wordpress.org/CSS), [Blog Design and Layout](https://codex.wordpress.org/Blog_Design_and_Layout)

## DNS

**DNS**, the domain name system, is the system that maps [domain names](#domain-name) to [IP addresses](#ip-address).
When you use a web browser to visit a website, your browser first
extracts the site’s domain name from the URL. Then it uses the DNS to
find the IP address for that domain name. Then it connects to that IP
address.

-   External link: [Domain Name System](http://en.wikipedia.org/wiki/Domain_Name_System) (Wikipedia)

## DOM

**DOM** (Document Object Model) is a standard,
platform-independent interface that allows programmers to dynamically
access HTML and XML to control the content and structure of documents.
DOM connects programming scripts to web pages.

-   External links: [DOM at Wikipedia](http://en.wikipedia.org/wiki/Document_Object_Model), [DOM at W3C.org](http://www.w3.org/DOM/)

## Domain name

A **domain name** is a name used for identification purposes on
the Internet. In WordPress a domain name usually identifies a server
where WordPress is installed. To make this work, the Internet’s domain
name system ([DNS](#dns)) maps the domain name to a server’s [IP address](#ip-address). For example, the domain name *example.com* maps to the IP address *192.0.43.10*.
Many domain names can map to the same IP address, allowing a single
server to run many websites. For example, the domain names *www.example.com* and *example.net* also map to the IP address *192.0.43.10*.

-   External link: [Domain name](http://en.wikipedia.org/wiki/Domain_name) (Wikipedia)

## Draft

The **draft** [post status](#post-status) is for WordPress [posts](#post) which are saved, but as yet unpublished. A draft post can only be edited through the [Administration Panel](../manage/dashboard/README.md), [Write Post SubPanel](https://codex.wordpress.org/Write_Post_SubPanel) by [users](https://codex.wordpress.org/Authors_and_Users_SubPanel#Table_of_Authors) of equal or greater [User Level](https://codex.wordpress.org/User_Levels) than the [post’s author](https://codex.wordpress.org/Authors_and_Users_SubPanel#Table_of_Registered_Users).

## Dynamic block

A type of block where the content of which may change and cannot be determined at the time of saving a post, instead calculated any time the post is shown on the front of a site. These blocks may save fallback content or no content at all in their JavaScript implementation, instead deferring to a PHP block implementation for runtime rendering.

## Excerpt

An **excerpt** is a condensed description of your blog [post](#post) and refers to the summary entered in the Excerpt field of the [Administration](../manage/dashboard/README.md) > [Posts](../manage/dashboard/README.md) > [Add New SubPanel](https://codex.wordpress.org/Posts_Add_New_SubPanel). The *excerpt* is used to describe your post in RSS feeds and is typically used in displaying search results. The *excerpt* is sometimes used in displaying the **Archives** and [Category](#category) views of your posts. Use the [Template Tag](https://developer.wordpress.org/themes/basics/template-tags/) [the_excerpt()](https://developer.wordpress.org/reference/functions/the_excerpt/)
to display the contents of this field. Note that if you do not enter
information into the Excerpt field when writing a post, and you use [the_excerpt()](https://developer.wordpress.org/reference/functions/the_excerpt/) in your theme template files, WordPress will automatically display the first 55 words of the [post](#post)‘s content.

An *excerpt* should not be confused with the **teaser**, which refers to words before the `<!--more-->` in a [post’s](#post) content. When typing a long post you can insert the `<!--more-->` [Quicktag](https://codex.wordpress.org/Posts_Add_New_SubPanel#Visual_Versus_HTML_Editor) after a few sentences to act as a cut-off point. When the post is displayed, the **teaser**, followed by a hyperlink (such as **Read the rest of this entry…**), is displayed. Your visitor can then click on that link to see the full version of your [post](#post). The [Template Tag](https://developer.wordpress.org/themes/basics/template-tags/), [the_content()](https://developer.wordpress.org/reference/functions/the_content/) should be used to display the teaser.

-   Related articles: [Customizing the Read More](https://codex.wordpress.org/Customizing_the_Read_More), [Excerpt](https://codex.wordpress.org/Excerpt)

## Feed

A **feed** is a function of special software that allows
“Feedreaders” to access a site automatically looking for new content and
then posting the information about new content and updates to another
site. This provides a way for users to keep up with the latest and
hottest information posted on different blogging sites. Some Feeds
include RSS (alternately defined as “Rich Site Summary” or “Really
Simple Syndication”), Atom or RDF files. Dave Shea, author of the web
design weblog [Mezzoblue](http://mezzoblue.com) has written [a comprehensive summary](http://www.mezzoblue.com/archives/2004/05/19/what_is_rssx/) of feeds. Feeds generally are based on [XML](#xml) technology.

## Feed reader

The role of Feedreader is to gather and display the webfeed from various website to one place.

## Filter

In WordPress, a Filter is a [function](http://www.w3schools.com/php/php_functions.asp) that is associated with an existing [Action](#action) by specifying any [existing Hook](https://developer.wordpress.org/apis/hooks/action-reference/).

Developers can create [**custom** Filters](https://developer.wordpress.org/reference/functions/add_filter/) using the [Filter API](https://developer.wordpress.org/apis/hooks/filter-reference/) to **replace** code from an existing Action. This process is called “[hooking](#hook)“.

**Custom Filters differ from custom *[Actions](#action)*** because custom Actions allow you to **add or remove** code from existing Actions. Whereas custom Filters allow you to **replace** specific data (such as a variable) found within an existing Action.

-   See also: [Action](#action), [Hook](#hook), [Terminology Confusion](#terminology-confusion)
-   Related articles: [Filters](https://developer.wordpress.org/plugins/hooks/), [Filter Reference](https://developer.wordpress.org/apis/hooks/filter-reference/), [add_filter()](https://developer.wordpress.org/reference/functions/add_filter/)

## Footer area

A **footer area** is a horizontal area provided by a [theme](#theme) for displaying information other than the main [content](#content) of the web page. Themes may provide one or more footer areas below the content. Footer areas usually contain [widgets](#widget) that an administrator of the site can customize.

In a theme, footer areas are generated by a [template](#template) file, typically named *sidebar-footer.php*.

-   See also: [Sidebar](#sidebar)
-   Related articles: [Templates](https://developer.wordpress.org/themes/basics/template-files/), [Customizing Your Sidebar](https://codex.wordpress.org/Customizing_Your_Sidebar), [Stepping Into Templates](https://developer.wordpress.org/themes/basics/template-files/), [Template Hierarchy](https://developer.wordpress.org/themes/basics/template-hierarchy/)

## Front end

The front end is what your visitors see and interact with when they come to your website, www.YourSite.com.

## FTP

**FTP**, or **File Transfer Protocol**, is a client-server
protocol for transferring files. It is one way to download files, and
the most common way to upload files to a server.

An FTP *client* is a program which can download files from, or upload files to, an FTP *server*.

You may need to use an FTP client to upload your WordPress files to your [web server](#web-server), particularly if you use a [hosting provider](#hosting-provider).

-   Related articles: [FTP Clients](https://codex.wordpress.org/FTP_Clients), [Uploading WordPress to a remote host](https://codex.wordpress.org/Uploading_WordPress_to_a_remote_host), [Using FileZilla](https://codex.wordpress.org/Using_FileZilla)

## Full site editing or FSE

This refers to a collection of features that ultimately allows users to edit their entire website using blocks as the starting point. This feature set includes everything from block patterns to global styles to templates to design tools for blocks (and more). First released in WordPress 5.9.

## Gallery

As defined by Andy Skelton, **Gallery**, introduced with [WordPress 2.5](https://wordpress.org/documentation/wordpress-version/version-2-5/),
is specifically an exposition of images attached to a post. In that
same vein, an upload is “attached to a post” when you upload it while
editing a post.

In the uploader there is a “Gallery” tab that shows all the
uploads attached to the post you are editing. When you have more than
one attachment in a post, you should see at the bottom of the Gallery
tab a button marked “Insert gallery”. That button inserts a shortcode
“” into the post. WordPress replaces that shortcode with an
exposition of all images attached to that post. Non-image file types are
excluded from the gallery.

> [!NOTE]
> If you don’t see the “Insert gallery” button, it may be because you have not attached two images to the post.

The pretty URLs for attachments are made only after you have published the post and should be composed as the post [permalink](#permalink) plus the attachment [slug](#slug).

-   Related articles: [Gallery Shortcode](https://codex.wordpress.org/Gallery_Shortcode), [Shortcode API](https://codex.wordpress.org/Shortcode_API)

## gettext

The **gettext** system is a set of tools and standards for
language translation, used by WordPress to provide versions in many
languages. In WordPress a text string for translation may have a domain
and a context. For example, a plugin might specify its own domain for
translations, and a context might help translators to provide different
translations of the same English word or phrase in different parts of
the user interface.

-   Related articles: [WordPress in Your Language](https://codex.wordpress.org/WordPress_in_Your_Language), [Translating WordPress](https://codex.wordpress.org/Translating_WordPress), [I18n for WordPress Developers](https://codex.wordpress.org/I18n_for_WordPress_Developers)
-   External links: [gettext](http://en.wikipedia.org/wiki/Gettext) (Wikipedia), [GNU gettext](http://www.gnu.org/software/gettext/gettext.html)

## GMT

**GMT** (“Greenwich Mean Time”, the time at the Royal Observatory
in Greenwich, England) is the old name of the time zone from which all
other time zones were measured. It has been replaced by [UTC](#utc)
(“Universal Time, Coordinated”), but for most practical purposes UTC
and GMT are the same, so the term GMT is still commonly used.

-   External links: [Greenwich Mean Time](http://en.wikipedia.org/wiki/Greenwich_Mean_Time), [Time zone](http://en.wikipedia.org/wiki/Time_zone), [UTC](http://en.wikipedia.org/wiki/Coordinated_Universal_Time) (Wikipedia)

## Gravatar

A **gravatar** is a globally recognized [avatar](#avatar)
(a graphic image or picture that represents a user). Typically a user’s
gravatar is associated with their email address, and using a service
such as [Gravatar.com](http://en.gravatar.com/). The site owner to can configure their site so that a user’s gravatar is displayed along with their comments.

-   See also: [Avatar](#avatar)
-   Related articles: [How to Use Gravatars in WordPress](https://codex.wordpress.org/How_to_Use_Gravatars_in_WordPress), [Using Gravatars](https://codex.wordpress.org/Using_Gravatars)
-   External links: [Gravatar at Wikipedia](http://en.wikipedia.org/wiki/Gravatar)

## GUI

GUI stands for Graphical User Interface, pronounced as “gooey”. It is
an interface that allows users to point the mouse or cursor to
graphical icons.

## Gutenberg

Gutenberg is newly developed, block-oriented editor. It uses blocks
to create all types of content, replacing a half-dozen inconsistent ways
of customizing WordPress, bringing it in line with modern coding
standards, and aligning with open web initiatives. These content blocks
transform how users, developers, and hosts interact with WordPress to
make building rich web content easier and more intuitive, democratizing
publishing, and work, for everyone, regardless of technical ability.

## Hack

A **hack** is a bit of code written to customize or extend the
functionality of a software product. Older versions of WordPress used a
hack-based extension system, but versions [1.2](https://codex.wordpress.org/Changelog/1.2) and above of WordPress use a [Plugin API](https://developer.wordpress.org/plugins/hooks/) with [hooks](#hook) for extensions.

-   See also: [Hacking](#hacking), [Plugin](#plugin)
-   Related articles: [Changelog](https://codex.wordpress.org/Changelog), [Plugin API](https://developer.wordpress.org/plugins/hooks/)
-   External links: [Open source at Wikipedia](http://en.wikipedia.org/wiki/Open_source)

## Hacking

**Hacking** is the process of writing code for, or contributing code to, a piece of software.

There is some controversy surrounding the meaning of this term.
It began as a benign term meaning “to exercise proficiency” or “to alter
or improve,” but the popular media have since construed it to mean “to
break into a computer system, usually with malicious intent.” Many in
the computer industry have recently begun trying to ‘take back’ the word
from its popular mutation, and many have adopted the term *cracking*
to replace the malicious interpretation. Because of the desire to
reclaim the word, you will often find the term used in conjunction with [open source](http://en.wikipedia.org/wiki/Open_source) projects, intended in its benign form. For more information about the history of the term, please see [Wikipedia’s article on *Hacker*](http://en.wikipedia.org/wiki/Hacker).

-   See also: [Hack](#hack)
-   Related articles: [Plugins](../manage/plugins.md)

## Header image

A **Header Image** is a wide picture that appears at the top of a WordPress website.

## Hook

Hooks are specified, by the developer, in Actions and Filters. Here is a (hopefully) complete list of all [existing Hooks](https://developer.wordpress.org/apis/hooks/action-reference/) within WordPress.

Because Hooks are required by Actions and Filter you may hear the
phrase “Action Hooks” and “Filter Hooks” used from time to time.

In technical and strict terms: a Hook is an event, i.e. event as understood by [Observer pattern](http://en.wikipedia.org/wiki/Observer_pattern), invoked by the [do_action()](https://developer.wordpress.org/reference/functions/do_action/) or [apply_filters()](https://developer.wordpress.org/reference/functions/apply_filters/) call that afterwards triggers all the [action](#action) or [filter](#filter) functions, previously hooked to that event using [add_action()](https://developer.wordpress.org/reference/functions/add_action/) or [add_filter()](https://developer.wordpress.org/reference/functions/add_filter/), respectively.

-   See also: [Action](#action), [Filter](#filter)
-   Related articles: [Hooks, Actions and Filters](https://developer.wordpress.org/plugins/hooks/), [Plugin API/Hooks](https://codex.wordpress.org/Plugin_API/Hooks)

### Terminology confusion

WordPress Codex and source code comments sometimes confuse the terms “[actions](#action)/[filters](#filter)” and “[hooks](#hook)“.

Actions, Filters and Hooks are also occasionally referred to as “action/filter hooks” or “action/filter/hook functions”.

## Hosting provider

A **hosting provider** is a company or organization which provides, usually for a fee, infrastructure for making information accessible via the web. This involves the use of a [web server](#web-server) (including web server software such as [Apache](#apache)), and may involve one or more related technologies, such as [FTP](#ftp), [PHP](#php), [MySQL](#mysql) or [MariaDB](#mariadb), and operating system software such as [Linux](#linux) or [Unix](#unix).

-   Related articles: [Hosting WordPress](https://wordpress.org/about/requirements/)

## .htaccess

A **.htaccess** file is a granular configuration file for the [Apache](#apache) [web server](#web-server)
software, used to set or alter the server’s configuration settings for
the directory in which it is present, and/or its child directories.

WordPress uses an *.htaccess* file in conjunction with the [mod_rewrite](#mod_rewrite) [Apache](#apache) module to produce [permalinks](#permalink).

Note that *.htaccess* is a *hidden file* in [Unix](#unix)/[Linux](#linux) (as dictated by the preceding period ‘.’), meaning it may not be visible using the default settings of some [FTP clients](https://codex.wordpress.org/FTP_Clients).

-   See also: [chmod](#chmod)
-   Related articles: [htaccess for subdirectories](https://codex.wordpress.org/htaccess_for_subdirectories), [Using Permalinks](../manage/settings/permalinks.md), [UNIX Shell Skills](https://codex.wordpress.org/UNIX_Shell_Skills), [Changing File Permissions](https://developer.wordpress.org/advanced-administration/server/file-permissions/)

## HTML

**HTML**, or **Hypertext Markup Language**, is a markup language used to describe the semantic content of web pages. It is usually used with [CSS](#css) and/or [JavaScript](#javascript). WordPress renders web pages to conform to the HTML5 standard. The standard is set by the World Wide Web Consortium ([W3C](http://www.w3.org)).

## IDE

Acronym for Integrated Development Environment. Is an application that provides several tools for software development.
An **IDE** usually includes:

-   source code editor, which is similar to a [Text Editor](#text-editor)
-   debugger, in the case of WordPress, useful debuggers are those for [PHP](#php) and [Javascript](#javascript) code
-   automated builder

For our recommended IDEs, please see [Editing Files](https://github.com/WordPress/Advanced-administration-handbook/blob/main/wordpress/edit-files.md#ides).

## Inspector

Deprecated term. See [Settings Sidebar](#settings-sidebar).

## IP address

An **IP address** is a unique number (e.g. *70.84.29.148*)
assigned to a computer (or other internet-capable information appliance,
such as a network printer) to enable it to communicate with other
devices using the *Internet Protocol*. It is a computer’s identity
on the internet, and every computer connected to the internet is
assigned at least one, although the methods of assigning these
addresses, and the permanence and duration of their assignment, differ
according to the use of the computer and the circumstances of its
internet use.

Every [web server](#web-server) is assigned an IP address as well, but often times [hosting providers](#hosting-provider)
will assign multiple IP addresses to one computer, in the event that
multiple web sites reside on the same physical server. This is the case
with most inexpensive ‘managed’ or ‘group’ hosting packages.

[Domain names](#domain-name)
were created to provide an easier means of accessing internet resources
than IP addresses, which are cumbersome to type and difficult to
remember. Every domain name has at least one corresponding IP address,
but only a small number of IP addresses have a domain name associated
with them, since only computers that are servers require domain names.
The domain name system ([DNS](#dns)) is what maps domain names to IP addresses.

-   External links: [IP address](http://en.wikipedia.org/wiki/IP_address) (Wikipedia)

## ISAPI

**ISAPI** (Internet Server Application Programming Interface) is a
set of programming standards designed to allow programmers to quickly
and easily develop efficient Web-based applications. Developed by
Process Software and Microsoft Corporation, *ISAPI* is intended to replace [CGI](#cgi) programs.

-   External links: [ISAPI at Wikipedia](http://en.wikipedia.org/wiki/ISAPI)

## JavaScript

**JavaScript** is a programming language that WordPress uses to
make certain processing occur in your web browser when it is
inconvenient or impossible for the server to do that processing. For
example, when you reply to a comment in a WordPress blog, WordPress uses
JavaScript to move the comment form inside the comment you are replying
to.

-   See also: [AJAX](#ajax), [HTML](#html), [XHTML](#xhtml)
-   Related article: [Using Javascript](https://codex.wordpress.org/Using_Javascript)
-   External link: [JavaScript](http://en.wikipedia.org/wiki/Javascript) (Wikipedia)

## Linux

**Linux** is an [open source](http://en.wikipedia.org/wiki/Open_source) computer operating system, created by Linus Torvalds, similar in style to [Unix](#unix). It is popular in [web server](#web-server)
and other high-performance computing environments, and has recently
begun to gain popularity in workstation environments as well.

-   External links: [Linux at Shortopedia](http://www.shortopedia.com/L/I/Linux)

## Local styles

See [Block Styles](#block-styles).

## Mac OS X

**[Mac OS X](http://www.apple.com/macosx/)**
is an operating system specifically for modern Macintosh computers. The
operating system was commercially released in 2001. It consists of two
main parts: Darwin, an open source [Unix](#unix)-like
environment which is based on the BSD source tree and the Mach
microkernel, adapted and further developed by Apple Computer with
involvement from independent developers; and a proprietary GUI named
Aqua, developed by Apple.

-   Related articles: [UNIX Shell Skills](https://codex.wordpress.org/UNIX_Shell_Skills)

## MariaDB

MariaDB is a fork of the [MySQL](#mysql) relational database system developed by most of the original developers of MySQL. It works equally well with WordPress.

## Menu

**Menus** are lists of links to pages and posts that appear on WordPress websites.

## Meta

**Meta** has several meanings, but generally means **information about**. In WordPress, *meta* usually refers to **administrative** type information. As described in [Meta Tags in WordPress](https://codex.wordpress.org/Meta_Tags_in_WordPress), *meta* is the [HTML](#html) tag used to describe and define a web page to the outside world (search engines). In the article [Post Meta Data](https://codex.wordpress.org/Post_Meta_Data_Section), *meta* refers to information associated with each **post**, such as the author’s name and the date posted. [Meta Rules](https://codex.wordpress.org/Codex:Guidelines#Meta_Rules) define the general protocol to follow in using the Codex. Also, many WordPress based sites offer a *Meta* section, usually found in the sidebar, with links to login or register at that site. Finally, *Meta* is a [MediaWiki](http://www.mediawiki.org) [namespace](http://meta.wikimedia.org/wiki/Namespace) that refers to administrative functions within Codex.

-   External links: [Wikipedia’s Article on Meta](http://en.wikipedia.org/wiki/Meta-)

## Microformats

**Microformats** provide a way for programs to read certain
information in web pages without making the pages look any different to
humans. They add semantics to the generic HTML markup in order for these
programs to understand the meaning of specific parts of a web page
content which is better recognized by humans. For example, a web page
displaying a user’s profile could use microformats to make it easy for a
program to extract the user’s contact information so that it can be
added to an address book in a single operation. In WordPress, some [themes](#theme) and [plugins](#plugin) support some microformats.

-   Related: [Themes](https://wordpress.org/extend/themes/tags/microformats) and [plugins](https://wordpress.org/extend/plugins/tags/microformats) providing microformats support
-   External links: [Microformats.org](http://microformats.org/)

## MIME

**MIME** stands for **Multipurpose Internet Mail Extension** and is an Internet standard that extends the format of email to support:

-   Text in character sets other than ASCII
-   Non-text attachments
-   Message bodies with multiple parts
-   Header information in non-ASCII character sets

MIME’s use, however, has grown beyond describing the content of email
and now is often used to describe content type in general including for
the web and as a storage for rich content in some commercial products.

-   External links: [IANA Media Types Specification](http://www.iana.org/assignments/media-types), [Wikipedia](http://en.wikipedia.org/wiki/MIME)

## Moblogging

**Moblogging** is the act of posting to one’s [blog](#blog) via a mobile device (e.g. mobile phone, smartphone, or tablet). It is pronounced as *mōbə-logging* or *mōb-logging*, or sometimes as *mŏb-logging* in reference to *smart mobs*.

-   Related articles: [Moblog Clients](https://codex.wordpress.org/Weblog_Client#Mobile), [Post to your blog using email](https://codex.wordpress.org/Post_to_your_blog_using_email)

## mod_rewrite

**mod_rewrite** is an extension module of the [Apache](#apache) [web server](#web-server) software which allows for “rewriting” of [URLs](http://en.wikipedia.org/wiki/Url) on-the-fly. Rewrite *rules* use [regular expressions](http://en.wikipedia.org/wiki/Regular_expression)
to parse the requested URL from the client, translate it into a
different URL, and serve the content of this new URL under the original
URL or pointing the client to make the new URL request.

WordPress uses *mod_rewrite* for its [permalink](#permalink) structure, and also for [multisite](#multisite) networks, which are both optional functionality.

-   Related articles: [Using Permalinks](../manage/settings/permalinks.md), [Create A Network](https://developer.wordpress.org/advanced-administration/multisite/create-network/)

## Multisite

**Multisite** is a feature of [WordPress 3.0](https://wordpress.org/documentation/wordpress-version/version-3-0/) and later versions that allows multiple virtual [sites](#site)
to share a single WordPress installation. When the multisite feature is
activated, the original WordPress site can be converted to support a [network](#network) of sites.

-   Related article: [Create A Network](https://github.com/WordPress/Advanced-administration-handbook/blob/main/multisite/create-network.md)

## MySQL

**MySQL** is a popular [open source](http://en.wikipedia.org/wiki/Open_source) SQL (Structured Query Language) database implementation, available for many platforms, including Windows, [Unix](#unix)/[Linux](#linux) and [Mac OS X](#mac-os-x).

WordPress requires a MySQL database to store all [blog](#blog) information, including [posts](#post), [comments](#comments), [metadata](#meta), and other information.

WordPress also works with MySQL-compatible databases such as [MariaDB](#mariadb) and Percona Server.

-   Related articles: [Database Description](https://codex.wordpress.org/Database_Description)
-   External links: [MySQL](http://mysql.com/), [MariaDB](http://mariadb.org/), [Percona Server](http://www.percona.com/software/percona-server/)

## Navigation

Navigation is the term used to describe text on a page that, when
selected, redirects you to a corresponding page elsewhere on the
website. Navigation may sometimes be referred to as the menu, links and
hyperlinks.

## Navigation block

A block that allows you to edit a site’s navigation menu, both in terms of structure and design.

## Network

In the WordPress user interface, a **network** is a collection of separate [sites](#site) created in a single WordPress installation by the [multisite](#multisite)
feature. The sites in a WordPress network are not interconnected like
the things in other kinds of networks. They are very like the separate
blogs at WordPress.com.

In WordPress code the network is known as the *site* and the sites are known as *blogs*.

-   Related articles: [Create A Network](https://developer.wordpress.org/advanced-administration/multisite/create-network/)

## News reader

A **news aggregator** or **news (feed) reader** is a computer program which tracks syndicated information [feeds](#feed), via [RSS](#rss), [RDF](#rdf), or [Atom](#atom).
Most news aggregators allow one to ‘subscribe’ to a feed, and
automatically keep track of the articles one has read, similar to an
email client tracking read emails.

Many [blogs](#blog) make their content available in [feed](#feed) form for the convenience of readers using news aggregators. WordPress can generate feeds in [RSS](#rss) and/or [Atom](#atom) formats.

-   External links: [News aggregator at Wikipedia](http://en.wikipedia.org/wiki/News_aggregator)

## Nonce

**Nonce** is used for security purposes to protect against
unexpected or duplicate requests that could cause undesired permanent or
irreversible changes to the web site and particularly to its database.
Specifically, a nonce is an one-time token generated by a web site
to identify future requests to that web site. When a request is
submitted, the web site verifies if a previously generated nonce
expected for this particular kind of request was sent along and decides
whether the request can be safely processed, or a notice of failure
should be returned. This could prevent unwanted repeated, expired or
malicious requests from being processed.

Nonce is usually included in a hidden HTML form field or as a
part of an URL and therefore sent with a request by submitting a form
field or visiting a link. If a request is not verified, the web site
could generate a new nonce in its response and prompt the user to
intentionally confirm the repetition of the request. In WordPress, the
response message is *“Are you sure you want to do this?”* by default.

-   Related articles: [WordPress Nonces](https://codex.wordpress.org/WordPress_Nonces)

## Open source

**Open source** is simply programming code that can be read,
viewed, modified, and distributed, by anyone who desires. WordPress is
distributed under an *open source* [GNU General Public License (GPL)](http://www.gnu.org/copyleft/gpl.html).

-   Related articles: [GPL](https://codex.wordpress.org/GPL), [License](https://codex.wordpress.org/License)
-   External links: [Open Source Initiative](http://www.opensource.org/), [Open Source at Wikipedia](http://en.wikipedia.org/wiki/Open_source), [Source Code at Wikipedia](http://en.wikipedia.org/wiki/Source_code)

## Options

**Options** are pieces of data that WordPress uses to store various preferences and configuration settings.
By using the [Options API](https://developer.wordpress.org/apis/options/) that is a simple and standardized way of storing data in the database, options can be [added](https://developer.wordpress.org/reference/functions/add_option/), [changed](https://developer.wordpress.org/reference/functions/update_option/), [removed](https://developer.wordpress.org/reference/functions/delete_option/), and [retrieved](https://developer.wordpress.org/reference/functions/get_option/), from the [wp_options table](https://codex.wordpress.org/Database_Description#Table:_wp_options).

-   Related articles: [Option Reference](https://codex.wordpress.org/Option_Reference), [Transients API](https://codex.wordpress.org/Transients_API), [Options API](https://developer.wordpress.org/apis/options/)

## Output compression

**Output Compression** is the removal of white spaces, carriage
returns, new lines and tabs from your HTML document. This reduces the
file size of the HTML document without changing the functionality.

-   Related articles: [Output Compression](https://codex.wordpress.org/Output_Compression)

## Page (post type)

A **Page** is often used to present “static” information about
yourself or your site. A good example of a Page is information you
would place on an About Page. A Page should not be confused with the
time-oriented objects called [posts](#post). Pages are typically “timeless” in nature and live “outside” your blog.

The word “page” has long been used to describe any HTML document
on the web. In WordPress, however, “Page” refers to a very specific
feature first introduced in WordPress version 1.5.

-   Related articles: [Pages](../write/create-a-page.md), [Write Page SubPanel](https://codex.wordpress.org/Write_Page_SubPanel)

## Patterns

> [!NOTE]
> WordPress 6.3 renamed Reusable Blocks to Patterns. A synced pattern will behave in exactly the same way as a reusable block.

Patterns are layouts of blocks that can be inserted as starter content that are meant to be changed by the user every time. Once inserted, they exist as a local save and are not global.

Related articles: [Patterns](../design/patterns/README.md), [Comparing Patterns to Template Parts](../design/patterns/README.md).

## Perl

**Perl** is an acronym for **Practical Extraction and Report Language**,
but it’s most commonly spelled as a proper name. It’s a very popular
and powerful scripting language used for web applications, although its
use is being largely replaced by [PHP](#php) in the mainstream. One of its strengths lies in its speedy and effective use of [regular expressions](http://en.wikipedia.org/wiki/Regular_expression). Its unofficial motto is, “There’s More Than One Way To Do It,” or “TMTOWTDI,” owing to the extreme flexibility of the syntax.

WordPress does not use Perl, and it is therefore not required.

## Permalink

A **permalink** is a [URL](http://en.wikipedia.org/wiki/Url) at which a resource or article will be permanently stored. Many pages driven by [Content Management Systems](#content-management-system)
contain excerpts of content which is frequently rotated, making linking
to bits of information within them a game of chance. Permalinks allow
users to bookmark full articles at a [URL](http://en.wikipedia.org/wiki/Url) they know will never change, and will always present the same content.

Permalinks are optional in WordPress, but are highly recommended as they greatly increase the cleanliness of [URL](http://en.wikipedia.org/wiki/Url). WordPress uses the [Apache](#apache) module *[mod_rewrite](#mod_rewrite)* to implement its permalink system.

-   Related articles: [Using Permalinks](../manage/settings/permalinks.md)
-   External links: [URL at Wikipedia](http://en.wikipedia.org/wiki/Url)

## Permissions

**Permissions** are security settings restricting or allowing users to perform certain functions. In the case of files on [Unix](#unix) or [Linux](#linux) systems, there are three types of permissions: *read*, *write*, and *execute*. In the case of [MySQL](#mysql) or [MariaDB](#mariadb) databases, there are many more: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, etc., although MySQL/MariaDB refer to them as *privileges*.

-   Related articles: [Changing File Permissions](https://developer.wordpress.org/advanced-administration/server/file-permissions/)

## PHP

**PHP** is a recursive acronym for **PHP: Hypertext Preprocessor**. It is a popular server-side scripting language designed specifically for integration with [HTML](#html), and is used (often in conjunction with [MySQL](#mysql) or [MariaDB](#mariadb)) in [Content Management Systems](#content-management-system) and other web applications. It is available on many platforms, including Windows, [Unix](#unix)/[Linux](#linux) and [Mac OS X](#mac-os-x), and is [open source](http://en.wikipedia.org/wiki/Open_source) software.

WordPress is written using PHP and requires it for operation.

-   External links: [PHP Website](http://php.net/), [PHP for Designers](http://web.archive.org/web/20150402040826/http://www.digital-web.com/articles/php_for_designers/): by WordPress lead [developer](#developer) [Matthew Mullenweg](https://codex.wordpress.org/User:Matt), [PHP at OnLAMP](http://www.onlamp.com/php/)

## phpMyAdmin

**phpMyAdmin** is a popular, powerful web-based interface for administering [MySQL](#mysql) or [MariaDB](#mariadb) databases. It is [open source](http://en.wikipedia.org/wiki/Open_source), written in [PHP](#php), and is among the better tools available for working with [MySQL](#mysql) or [MariaDB](#mariadb) databases.

-   Related articles: [phpMyAdmin](https://codex.wordpress.org/phpMyAdmin)
-   External links: [phpMyAdmin web site](https://www.phpmyadmin.net/)

## Ping

Within the WordPress interface, “ping” is sometimes used to refer to [Pingbacks](#pingback) and [Trackbacks](#trackback).

In general computer terms, “ping” is a common utility used in a TCP/IP environment to determine if a given [IP Address](#ip-address)
exists or is reachable. Typically, Ping is used to diagnose a network
connection problem. Many times you will be asked, “Can you ping that
address?”. That means, does the Ping utility return a success message
trying to reach the “problem” [IP Address](#ip-address)?

-   External links: [Ping at Wikipedia](http://en.wikipedia.org/wiki/Ping)

## Pingback

**Pingback** lets you notify the author of an article if you link
to his article (article on a blog, of course). If the links you include
in an article you write on a blog lead to a blog which is
pingback-enabled, then the author of that blog gets a notification in
the form of a pingback that you linked to his article.

If you’re feeling *really* geeky you may want to check out the [Pingback technical specification](http://hixie.ch/specs/pingback/pingback) or [Otto’s “How Pingbacks Work” explanation](http://lists.automattic.com/pipermail/wp-hackers/2009-September/027425.html).

-   See also: [Trackback](#trackback)
-   Related articles: [Introduction to Blogging: Pingbacks](glossary.md#pingback)

## Plugin

A **Plugin** is a group of PHP functions that can extend the
functionality present in a standard WordPress weblog. These functions
may all be defined in one php file, or may be spread among more than one
file. Usually, a plugin is a PHP file that can be uploaded to the
“wp-content/plugins” directory on your webserver, where you have
installed WordPress. Once you have uploaded the plugin file, you should
be able to “turn it on” or Enable it from the “Plugins” page in the
administration interface of your weblog. The WordPress source code
contains hooks that can be used by plugins.

-   See also: [Hack](#hack), [Hacking](#hacking)
-   Related articles: [Plugins](../manage/plugins.md)

## Port

Within the context of the WordPress community, a **port** is a bit
of code that has been rewritten to be compatible with WordPress. For
example, if someone wrote a plugin for MoveableType, WordPress users may
want to find a port of that plugin for WordPress. Port can also be
used as a verb: to rewrite a piece of software for a different
platform/language.

-   External links: [Porting at Wikipedia](http://en.wikipedia.org/wiki/Porting)

## Post

Also known as “articles” and sometimes incorrectly referred to as
“blogs”. In WordPress, “posts” are articles that you write to populate
your blog.

## Post settings

A sidebar region containing metadata fields for the post, including scheduling, visibility, terms, and featured image.

## Post slug

A few lowercase words separated by dashes, describing a post and
usually derived from the post title to create a user-friendly (that is,
readable and without confusing characters) [permalink](../manage/settings/permalinks.md). Post slug substitutes the “%posttitle%” placeholder in a [custom permalink structure](../manage/settings/permalinks.md). Post slug should not be changed and is especially useful if the post title tends to be long or changes frequently.

## Post status

The status of a post, as set in the [Administration Panel](../manage/dashboard/README.md), [Write Post SubPanel](https://codex.wordpress.org/Write_Post_SubPanel) is either: **Published** (viewable by everyone), **Draft** (incomplete post viewable by anyone with proper [user level](https://codex.wordpress.org/User_Levels)), or **Private** (viewable only to WordPress users at Administrator level).

-   Related articles: [Post Status](https://codex.wordpress.org/Post_Status)

## Post type

Post type refers to the various structured data that is maintained in
the WordPress posts table. Native (or built-in) registered post types
are **post**, **page**, **attachment**, **revision**, and **nav-menu-item**. Custom post types are also supported in WordPress and can be defined with [register_post_type()](https://developer.wordpress.org/reference/functions/register_post_type/).
Custom post types allow users to easily create and manage such things
as portfolios, projects, video libraries, podcasts, quotes, chats, and
whatever a user or developer can imagine.

-   Related articles: [Post Types](https://codex.wordpress.org/Post_Types)

## Query

The process behind the scenes. See below. 🙂

-   Related articles: *[Query Overview](https://codex.wordpress.org/Query_Overview)*, *[Custom Queries](https://codex.wordpress.org/Custom_Queries)*, *[WP Query](https://codex.wordpress.org/Class_Reference/WP_Query)*, *[WP User Query](https://codex.wordpress.org/Class_Reference/WP_User_Query)*
-   See also: *[query string](#query-string)*, *[query variable](#query-variable)*

## Query block

A block that replicates the classic [WP_Query](https://developer.wordpress.org/reference/classes/wp_query/) and allows for further customization with additional functionality.

## Query string

A sequence of codes in a [Uniform Resource Identifier (URI)](http://en.wikipedia.org/wiki/Uniform_Resource_Identifier) that a web page uses to determine what dynamic data to display. The query string in a [URI](http://en.wikipedia.org/wiki/Uniform_Resource_Identifier)
comes after an initial question mark, and may contain several
parameters separated by ampersands. WordPress uses query strings to
indicate criteria to search for specific posts or sets of posts in the
database. The use of query strings is generally believed to impede the
indexing of dynamic pages by search engines. For this reason, it is
often desirable to use a method such as [mod_rewrite](#mod_rewrite) to reduce exposure of query strings to search engines and other site visitors.

## Query variable

A variable passed through the [query string](#query-string). For example, in the query string *?category_name=tech&feed=atom*, there are two query variables: *category_name* with a value of “tech”, and *feed* with a value of “atom”.

## QuickTag

A **Quicktag** is a shortcut, or one-click button, that inserts HTML code into your posts. The &lt;em> (emphasis) and &lt;/em> (stop emphasis) HTML tags are example of Quicktags. Some Quicktags, such as &lt;!–contactform–>, insert HTML comment code that is used by plugins to replace text or perform certain actions.

## RDF

Resource Description Framework. A language used to describe the locations of resources on the web. WordPress can produce output in RDF format that describes the locations of posts. Like [RSS](#rss), RDF is used for content syndication.

## Recordset

**Recordset** refers to the group of records or result returned from a database query.

-   See also [MySQL](#mysql), [wpdb](https://codex.wordpress.org/Class_Reference/wpdb) database class

## Relative path

A **relative path** is the location of a file in relation to the
current working directory and does not begin with a slash (/). This is
different from an [absolute path](#absolute-path) which gives an exact location.

-   See also: [Absolute Path](#absolute-path)
-   External links: [Path_Computing at Wikipedia](http://en.wikipedia.org/wiki/Path_(computing))

## Relative URI

A relative URI (sometimes called a **relative link**) is a partial URI that is interpreted (resolved) relative to a **base URI**.

On the World Wide Web, relative URIs come in two forms:

A **relative URI with an absolute path** is interpreted relative to the domain root:

```text
 /images/icecream.jpg → http://domain.example/images/icecream.jpg
```

A **relative URI with a relative path** is interpreted relative to the URL of the current document. E.g., on the web page *http://domain.example/icecream/chocolate.html*,

```text
 strawberry.html → http://domain.example/icecream/strawberry.html
```

[Wikipedia: URI Resolution](http://en.wikipedia.org/wiki/Uniform_Resource_Identifier#URI_resolution)

## RichText

A common component enabling rich content editing including bold, italics, hyperlinks, etc.

## RSS

“*Really Simple Syndication*“: a format for syndicating many
types of content, including blog entries, torrent files, video clips on
news-like sites; specifically frequently updated content on a Web site,
and is also known as a type of “feed” or “aggregator”. An RSS feed can
contain a summary of content or the full text, and makes it easier for
people to keep up to date with sites they like in an automated manner
(much like e-mail).

The content of the feed can be read by using software called an [RSS or Feed reader](#news-reader).
Feed readers display hyperlinks, and include other metadata (information
about information) that helps people decide whether they want to read
more, follow a link, or move on.

The original intent of RSS is to make information come to you
(via the feed reader) instead of you going out to look for it (via the
Web).

Programs called news aggregators permit users to view many feeds at once, providing ‘push’ content constantly. See [Category:Feeds](https://codex.wordpress.org/Category:Feeds) for Codex resources about bringing RSS feeds into WordPress. See also [RDF](#rdf) Site Summary.

## RTL

A written language is [Right-to-left](http://en.wikipedia.org/wiki/Right-to-left) when its script flows from the right side of the page to the left.

-   Related articles: [Right-to-Left Language Support](https://codex.wordpress.org/Right-to-Left_Language_Support)

## Robots.txt

Web Robots are programs which traverse the Web automatically. They
are also called Web Wanderers, Web Crawlers, and Spiders. Search Engines
are the main Web Robots. Some Web Robots look for a file named **robots.txt** on your [web server](#web-server) to see what and where they should look for content and files on your web server. Some Web Robots ignore this file.

-   Related articles: [Search Engine Optimization for WordPress](https://codex.wordpress.org/Search_Engine_Optimization_for_WordPress)
-   External links: [Google information about robots.txt](http://www.google.com/support/webmasters/bin/answer.py?answer=40361), [The Web Robots Page](http://www.robotstxt.org/wc/robots.html)

## Role

A **role** gives users permission to perform a group of tasks. When a user logs in and is authenticated, the user’s role determines which [capabilities](#capabilities)
the user has, and each capability is permission to perform one or more
types of task. All users with the same role normally have the same
capabilities. For example, users who have the Author role usually have
permission to edit their own posts, but not permission to edit other
users’ posts. WordPress comes with six roles and over fifty capabilities
in its role-based access system. Plugins can modify the system.

-   Related article: [Roles and Capabilities](https://codex.wordpress.org/Roles_and_Capabilities)
-   External link: [Role-based access control](http://en.wikipedia.org/wiki/Role-based_access_control) (Wikipedia)

## Screen

In WordPress a **screen** is a web page used for managing part of a weblog ([site](#site)) or [network](#network). The term ‘screen’ is used to avoid confusion with ‘[page](#page-post-type)‘, which has a specific and different meaning in WordPress. For example, the web page used to manage posts is known as the [Posts Screen](https://codex.wordpress.org/Posts_Screen).

-   Related article: [Class_Reference/WP_Screen](https://codex.wordpress.org/Class_Reference/WP_Screen)

## Serialization

The process of converting a block’s attributes object into HTML markup, which occurs each time a block is edited.

## Settings sidebar

The panel on the right that contains the document and block settings. The sidebar is toggled using the Settings gear icon. Block settings are shown when a block is selected, otherwise document settings are shown.

## Shell

A **shell** is a program which interacts directly with an operating system such as MS-DOS, [Unix](#unix)/[Linux](#linux), [Mac OS X](#mac-os-x), or others, but it is most commonly associated with [Unices](#unix).
It is often referred to as a ‘console’ or ‘command line’, because it is
controlled using typed commands rather than mouse or graphical
interface input.

Most often, when interacting with a remote computer (as one would
when configuring WordPress), an additional “faux” shell is involved
called [SSH](#ssh).

Some popular shell programs are:

-   [Bash](http://www.gnu.org/software/bash/bash.html) (Bourne Again Shell)
-   [Tcsh](http://tcsh.org/) (an expanded C Shell)
-   [Zsh](http://www.zsh.org/)

## Shortcode

A [Shortcode](https://codex.wordpress.org/Shortcode) is a technique for embedding a snippet of [PHP](#php) code into the body of a page or other content item.

## Sidebar

A **sidebar** is a vertical column provided by a [theme](#theme) for displaying information other than the main [content](#content) of the web page. Themes usually provide at least one sidebar at the left or right of the content. Sidebars usually contain [widgets](#widget) that an administrator of the site can customize.

In a theme, sidebars are generated by a [template](#template) file, typically named *sidebar.php*.

-   See also: [Footer area](#footer-area)
-   Related articles: [Sidebars](https://codex.wordpress.org/Sidebars), [Templates](https://developer.wordpress.org/themes/basics/template-files/), [Customizing Your Sidebar](https://codex.wordpress.org/Customizing_Your_Sidebar), [Stepping Into Templates](https://developer.wordpress.org/themes/basics/template-files/), [Template Hierarchy](https://developer.wordpress.org/themes/basics/template-hierarchy/)

## Site

In the WordPress user interface, a **site** can simply be the website created by WordPress, or it can be a virtual website created as part of a [network](#network) by the [multisite](#multisite)
feature. A site in a network is virtual in the sense that it does not
have its own directory on the server, although it has its own URL and it
might have its own domain name.

In WordPress code the site is the website created by WordPress.
If multisite is in use, then the site is the network website and each
virtual website is known as a *blog*.

-   Related article: [Create A Network](https://developer.wordpress.org/advanced-administration/multisite/create-network/)

## Site Editor

The cohesive experience that allows you to directly edit and navigate between various templates, template parts, styling options, and more.

## Slug

A **slug** is a few words that describe a post or a page. Slugs
are usually a URL friendly version of the post title (which has been
automatically generated by WordPress), but a slug can be anything you
like. Slugs are meant to be used with [permalinks](#permalink) as they help describe what the content at the URL is.

Example post permalink: *<https://wordpress.org/development/2006/06/wordpress-203/>*

The slug for that post is “wordpress-203”.

Slugs are also used for post types, categories, tags, etc. Like
post and page slugs, this is usually for creating URL friendly versions
of these items.

## Smileys

![Wink Icon](https://codex.wordpress.org/images/4/4b/icon_wink.gif)

Smileys (also called Smilies or Emoticons) are stylized
representations of a human face, usually displayed as yellow buttons
with two dots for the eyes, and a half mouth. Smileys are often used in
WordPress Plugins. By default, WordPress automatically converts text
smileys to graphic images. When you type 😉 in your post you see when you preview or publish your post.

Related article: [Using Smilies](https://codex.wordpress.org/Using_Smilies)

## Spam

Once upon a time, [SPAM](http://www.hormel.com)
was an animal by-product that came in a can and was fodder for many
Monty Python sketches, but since the world-wide adoption of the internet
as an integral part of daily life, Spam has become synonymous with what
is wrong with the internet. Spam, in general terms, is an email or
other forms of unsolicited advertising. Spam is very easy to spread
throughout the internet, and works on the principle that if you send out
thousands, or hundreds of thousands of unsolicited advertisements,
scams, or other questionable methods of making money, that you only need
a very small percentage of people to be fooled and you will make lots
of money.

Common spam these days comes from online gambling sites and those
trying to sell drugs for “male enhancement.” Lately, web logs, or
blogs, as we call them, have been targeted by spammers to try to
increase their site ratings in the search engines. Spammers use various
methods to distribute their electronic junk mail, and employ bots, or
computer programs to quickly and easily send email or comments to
millions of addresses and [IPs](#ip-address) all over the world.

Spammers can be difficult to track down as they often hijack peoples’ email and [IP](#ip-address) addresses. When this happens, it may appear a friend sent you the spam, but in fact, the spammer’s [bot](http://en.wikipedia.org/wiki/Internet_bot) grabbed your friend’s email address and used it to hide the true source of the spam. WordPress [developers](#developer) and community members are constantly working on more and better ways to combat these annoying **spammers**
as they clog the internet with their garbage. You can help by offering
your talents, ideas, suggestions, or just by being vigilant and
installing any of the [currently-available spam combating tools](../write/comments/comment-spam.md).

-   External links: [SPAM at Wikipedia](http://en.wikipedia.org/wiki/SPAM)

## SSH

**SSH** stands for Secure Shell. It is a communication protocol
for connecting to remote computers over TCP/IP. Various authentication
methods can be used which make SSH more secure than [Telnet](#telnet).

## SSL

**SSL** stands for Secure Sockets Layer and is the predecessor to
Transport Layer Security. These are cryptographic protocols for secure
communications across an unsecured network like the Internet.

-   External links: [SSL at Wikipedia](http://en.wikipedia.org/wiki/Secure_Sockets_Layer)

## Static block

A type of block where the content of which is known at the time of saving a post. A static block will be saved with HTML markup directly in post content.

## Stats

**Stats** are a record showing how many views and visitors a
WordPress blog or website gets during a set period of time. Stats also
show where in the world your viewers are.

## String

In computer science a string is any finite sequence of characters
(i.e., letters, numerals, symbols and punctuation marks).
Typically, programmers must enclose strings in quotation marks for the
data to be recognized as a string and not a number or variable name.

-   External links: [String at Wikipedia](http://en.wikipedia.org/wiki/String_(computer_science))

## Structure tags

These tags are used to customize WordPress permalinks. Structure tags are:
%year%, %day%, %hour%, %minute%, %second%, %post_id%, %postname%, %category% and %author%.
End permalink structure with either %post_id% or %postname%, so that each permalink points to an individual post.

-   Related articles: [Permalinks](../manage/settings/permalinks.md)

## Subversion

[Subversion](http://subversion.tigris.org/) is an [open-source](#open-source) [version control](http://en.wikipedia.org/wiki/Revision_control) software tool used by the [WordPress Developers](https://codex.wordpress.org/Copyright_Holders) to maintain and track the changes and updates to the various WordPress versions.

-   Related articles: [Using Subversion](https://codex.wordpress.org/Using_Subversion)
-   External links: [Subversion access at WordPress.org](https://wordpress.org/download/svn/), [Subversion book at red-bean.com](http://svnbook.red-bean.com/)

## SVC

**SVC** stands for Switched Virtual Circuit. An SVC is a virtual
circuit that is temporary turned on during a session of data transfer.

-   External links: [Virtual circuit at Wikipedia](http://en.wikipedia.org/wiki/Virtual_circuit)

## Syndication

See RSS: [Really Simple Syndication](#rss)

## Tag

A Tag is a keyword which describes all or part of a Post. Think of it like a [Category](#category),
but smaller in scope. A Post may have several tags, many of which
relate to it only peripherally. Like Categories, Tags are usually linked
to a page which shows all Posts having the same Tag. Tags can be
created on-the-fly by simply typing them into the [Tag field](https://codex.wordpress.org/Writing_Posts#Post_Tags). By default, tags can be assigned only to the *Post* and custom [post types](https://codex.wordpress.org/Post_types).

Tags can also be displayed in [clouds](http://en.wikipedia.org/wiki/Tag_Cloud)
which show large numbers of Tags in various sizes, colors, etc. This
allows for a sort of total perspective on the blog, allowing people to
see the sort of things your blog is about most.

Many people confuse Tags and Categories, but the difference is
easy: Categories generally don’t change often, while your Tags usually
change with every Post and are closer to the topic of the Post.

## Tagline

A tagline is a catchy phrase that describes the character or the
attributes of the blog in a brief, concise manner. Think of it as the
slogan, or catchline for a weblog.

## Task based documentation

Task based, or task oriented documentation is writing that takes you
through a process/task step-by-step; it is succinct, lacks jargon, is
easily understood, and structured entirely around performing specific
tasks.
In order to get to Z, you need to:

1.  Step x
2.  Step y
3.  Step z

Keep in mind that people who need to know how to perform a task usually need answers quick!

## Taxonomy

A **taxonomy** allows for the classification of things. In
WordPress, there are two built-in taxonomies, categories and tags.
These taxonomies help further classify posts and custom post types.
Also, custom taxonomies can be defined.

-   See also: [Category](#category), [Tag](#tag)
-   External links: [Taxonomy at Wikipedia](http://en.wikipedia.org/wiki/Taxonomy), [register_taxonomy()](https://developer.wordpress.org/reference/functions/register_taxonomy/)

## Telnet

Telnet is a [communications protocol](http://en.wikipedia.org/wiki/Internet_protocol_suite) used to establish a connection to another computer. *Telnet* runs on top of [TCP](http://en.wikipedia.org/wiki/Transmission_Control_Protocol)/[IP](http://en.wikipedia.org/wiki/Internet_Protocol)
and is typically used in conjuction with terminal emulation software to
login to remote computers. Telnet is inherently insecure and has
largely been replaced by [SSH](#ssh)

-   External links: [Telnet at Wikipedia](http://en.wikipedia.org/wiki/Telnet)

## Template

In WordPress a **template** is a file that defines an area of the web pages generated by a [theme](#theme). For example, there is typically a template for the header area at the top of the web pages, a template for the [content](#content), a template for the [sidebars](#sidebar), and so on. The templates are like building blocks that make up the complete web page.

-   Related articles: [Templates](https://developer.wordpress.org/themes/basics/template-files/), [Stepping Into Templates](https://developer.wordpress.org/themes/basics/template-files/), [Template Hierarchy](https://developer.wordpress.org/themes/basics/template-hierarchy/)

## Template editing mode

A scaled down direct editing experience allowing you to edit/change/create the template a post/page uses.

## Template tag

In a WordPress Theme, [template tags](https://developer.wordpress.org/themes/basics/template-tags/)
are used in template files to generate specific programming
instructions. They are used to display generated content and information
on a WordPress site. Template tags are short programming words, also
known as functions, that tap into the WordPress core for instructions.
For example, the HTML title tag of a WordPress site may hold the [bloginfo()](https://developer.wordpress.org/reference/functions/bloginfo/)
template tag that requests the site title, site tagline, and other site
information set by the template tag parameters. Using this in the title HTML tag allows the Theme to be used on multiple sites and the information displayed will change easily with each site.

Other template tags are more sophisticated, generating post content, queries, and site data.

-   Related articles: [Stepping Into Template Tags](https://codex.wordpress.org/Stepping_Into_Template_Tags), [Anatomy of a Template Tag](https://codex.wordpress.org/Anatomy_of_a_Template_Tag), [How to Pass Tag Parameters](https://codex.wordpress.org/How_to_Pass_Tag_Parameters), [Include Tags](https://codex.wordpress.org/Include_Tags), [Conditional Tags](https://codex.wordpress.org/Conditional_Tags), [Function Reference](https://codex.wordpress.org/Function_Reference), [Templates](https://developer.wordpress.org/themes/basics/template-files/)

## Term

In WordPress, a **term** is a classification, group or subset of a [Taxonomy](#taxonomy), where the latter can be a [Category](#category), [Tag](#tag)
or Custom Taxonomy. By default, terms have a title, a slug and a
description. Hierarchical taxonomies like categories can define a parent
term.

-   Related articles: [Taxonomies](https://codex.wordpress.org/Taxonomies), [the_terms()](https://developer.wordpress.org/reference/functions/the_terms/)

## Text editor

A **text editor** is a program which edits files in *plain text* format, as compared to *binary* format. Using a non-text based word processing program (e.g. using Microsoft Word to edit [PHP](#php)
scripts) can cause major problems in your code. This is because
non-text based word processing programs insert extra formatting into
text files, and can corrupt the files when they need to be interpreted
by the interpreter. An editor like Notepad does not insert any extra
formatting.

**Edit WordPress Files with a text only editor.**

Some examples of file formats which need to be edited as plain text:

-   [HTML](#html) documents
-   [PHP](#php) scripts
-   [Perl](#perl) scripts
-   Rich Text Format documents
-   [JavaScript](#javascript) scripts

For our recommended Text Editors, please see [Editing Files](https://github.com/WordPress/Advanced-administration-handbook/blob/main/wordpress/edit-files.md#text-editors).

Some examples of non-plain text formats that require special software for editing:

-   Microsoft Word documents
-   Microsoft Excel spreadsheets
-   Images, such as JPEG, PNG, or GIF

Some examples of software which can edit text, but which are **NOT** regarded as basic text editors and **NOT recommended** for use on WordPress files:

-   Microsoft Word
-   Microsoft Excel
-   Adobe Photoshop
-   Adobe Illustrator
-   Adobe Dreamweaver

## Theme

A Theme is a collection of files that work together to produce a
graphical front-end interface with an underlying unifying design for a
site. A WordPress Theme modifies the way the site is displayed and
designed, without modifying the underlying core programming of
WordPress. While some associate a WordPress Theme with “skinning” your
site with a design, a WordPress Theme contains programming code that
influences the design, changing it with each generated page view based
upon the programming with PHP, WordPress template tags, WordPress
conditional tags, and CSS.

-   Related articles: [Theme Development](https://codex.wordpress.org/Theme_Development), [Using Themes](../design/themes/README.md)

## Theme blocks

Blocks that accomplish everything possible in traditional templates using template tags (ex: Post Author Block). A full list can be found [here](https://github.com/WordPress/gutenberg/issues/22724).

## TinyMCE

[TinyMCE](https://www.tinymce.com/) is a web-based JavaScript WYSIWYG (What You See Is What You Get) editor.

## Toolbar

The **Toolbar** is an area of the screen just above that site that
lists useful admininstration screen links such as add a new post or
edit your profile. The Toolbar was added in [Version 3.1](https://wordpress.org/documentation/wordpress-version/version-3-1/) as [Admin Bar](#admin-bar) and in [Version 3.3](https://wordpress.org/documentation/wordpress-version/version-3-3/) it was replaced by the [Toolbar](#toolbar). The toolbar can be turned on/off from the [User Profile Screen](https://codex.wordpress.org/Users_Your_Profile_SubPanel).

-   Related articles: [Toolbar](https://codex.wordpress.org/Toolbar)
-   See also: [Admin Bar](#admin-bar), [Your Profile Screen](https://codex.wordpress.org/Users_Your_Profile_SubPanel)

## Toolbar (in FSE)

A set of button controls. In the context of a block, usually referring to the toolbar of block controls shown above the selected block.

## Trackback

Trackback helps you to notify another author that you wrote something
related to what he had written on his blog, even if you don’t have an
explicit link to his article. This improves the chances of the other
author sitting up and noticing that you gave him credit for something,
or that you improved upon something he wrote, or something similar. With
pingback and trackback, blogs are interconnected. Think of them as the
equivalents of acknowledgements and references at the end of an academic
paper, or a chapter in a textbook.

-   See also: [Pingback](#pingback)
-   Related articles: [Introduction to Blogging: Trackbacks](glossary.md#trackback)

## Transient

A **Transient** is temporal data identified by a custom name, stored in the [web server](#web-server) database or memory for fast access. This temporal nature and use of fast memory caching is their primary distinction from [Options](#options).

-   Related articles: [Transients API](https://codex.wordpress.org/Transients_API), [Options API](https://developer.wordpress.org/apis/options/)

## Unicode

A widely supported and preferred character encoding system.

For a computer to display letters (or any text characters), it
needs to enumerate them – create an index of characters it knows how to
display. These indexes are known as character sets. This is invaluable
for users hosting [WordPress in a non-English language](https://codex.wordpress.org/Localization).

The most widely used collections of these character sets are the [iso-8859](https://en.wikipedia.org/wiki/ISO/IEC_8859) with [iso-8859-1](http://en.wikipedia.org/wiki/ISO_8859-1) and [iso-8859-15](http://en.wikipedia.org/wiki/ISO_8859-15) (which contains the euro sign) being the most common; they are also known as Latin1 and Latin9. These character sets use 8 bits (a single byte) for each character, allowing for 255 different characters (256, counting null). However, when considering that Latin-based languages aren’t the only ones in the world (think Japanese or Hebrew), 255 characters aren’t nearly enough.

There is a wide index of characters known as [Unicode](http://en.wikipedia.org/wiki/Unicode).
Unicode has so many characters that sometimes more than 16 bits (2
bytes!) are required to represent them. Furthermore, the first 127
characters of Unicode are the same as the first 127 of the most widely
used character set – iso-8859-1. For this purpose, UTF, the Unicode
Translation Format, was created. UTF uses different numbers of bits for
characters, and allows for the entire range of Unicode to be used. What
you should probably know is:

-   UTF-8 is an 8-bit-minimum type of UTF. There are also UTF-16 and UTF-32.
-   If your document is in a Latin-based encoding, you probably don’t need to change anything about it for it to be UTF.
-   A single UTF document can be in various languages with no need to switch encodings halfway through.
-   External links: [Joel Spolsky on Unicode](http://www.joelonsoftware.com/articles/Unicode.html)

## Unix

**Unix**, or **UNIX**, is a computer operating system developed
at AT&T’s Bell Laboratories starting back in 1969. Initially
designed with the objective of creating an OS written in a high level
language rather than assembly, a majority of [web servers](#web-server) currently run on different “flavors” of this high-performance OS, or on [Linux](#linux), developed as a Unix-like operating system.

-   See also: [UNIX Shell Skills](https://codex.wordpress.org/UNIX_Shell_Skills), [Mac OS X](#mac-os-x)

## Unix time

**Unix Time**, or a **timestamp**, is a method of tracking time
by determining the approximate number of seconds from a particular
event. That event is called an Epoch. Since this time format is only off
by a few seconds each century, it is usually considered good enough for
most applications.

Unix time is (currently) a ten digit number, and looks like this: 1229362315.
WordPress often uses a Unix timestamp internally to track time. The
human readable times and dates you see are converted from Unix Time or
from a MySQL/MariaDB DATETIME field.

-   External Links: [Unix Time at Wikipedia](http://en.wikipedia.org/wiki/Unix_time), [DATETIME](http://dev.mysql.com/doc/refman/en/datetime.htmllMySQL), [MariaDB DATETIME](https://mariadb.com/kb/en/mariadb/datetime/)

## URL

An address of a specific Web site or file on the Internet.

```text
 http://www.example.com/
 http://www.example.com/reports/index.html
```

## UTC

**UTC** (“Universal Time, Coordinated”) is the basis of
international time standards from which time zones around the world are
calculated. For most purposes it is the same as the older [GMT](#gmt) standard.

-   External link: [UTC](http://en.wikipedia.org/wiki/Coordinated_Universal_Time) (Wikipedia)

## Web server

A **web server** is a computer containing software for, and connected to infrastructure for, *hosting*, or serving, web sites written in [HTML](#html). The most common web server software on the internet is [Apache](#apache), which is frequently used in conjunction with [PHP](#php), [Perl](#perl), and other scripting languages.

It is possible to create one’s own web server, hosted on any
speed of internet connection, but many people choose to purchase
packages from [hosting providers](#hosting-provider),
who have the capacity and facilities to provide adequate bandwidth,
uptime, hardware, and maintenance for frequently-visited web sites.

-   Related articles: [Hosting WordPress](https://codex.wordpress.org/Hosting_WordPress)

## Widget

In WordPress a **widget** is a self-contained area of a web page
that performs a specific function, or the code that generates such a
self-contained area. For example, WordPress has a built-in widget that
displays a list of pages in a weblog’s [sidebar](#sidebar), and it has another built-in widget that displays a list of recent comments in the [Dashboard](#dashboard). Plugins and themes can provide additional widgets.

-   Related articles: [WordPress Widgets](https://codex.wordpress.org/WordPress_Widgets), [Widgets API](https://codex.wordpress.org/Widgets_API), [Dashboard Widgets API](https://codex.wordpress.org/Dashboard_Widgets_API)

### Widget area

Furthermore, a “Widget Area” is a pre-defined location, in the code
of your WordPress Theme, that allows users to place Widgets into.

## XFN

[The XHTML Friends Network](http://gmpg.org/xfn). A decentralised project to have inter-blog links that represent relationships between bloggers. XFN links resemble `<a href="http://www.photomatt.net/" rel="friend met">Photo Matt</a>`.

## XHTML

**XHTML**, or **Extensible HyperText Markup Language**, is the successor to [HTML](#html) as the [W3C](http://www.w3.org) standard language with which all web pages are created. It is often used in conjunction with [CSS](#css) and [JavaScript](#javascript).

WordPress strives to conform to the XHTML 1.0 Transitional standard.

-   External links: [XHTML 1.0 Specification (Second Edition)](http://www.w3.org/TR/xhtml1/), [XHTML 1.1 Specification](http://www.w3.org/TR/xhtml11/)

## XML

**XML**, or **Extensible Markup Language**, is written in
Standard Generalized Markup Language (SGML) and essentially allows you
to define your own markup language. XML is extremely useful in
describing, sharing, and transmitting data across the Internet.
Typically used in conjunction with [HTML](#html), XML defines data and [HTML](#html) displays that data.

-   External links: [Extensible Markup Language (XML) Resources at W3C org](http://www.w3.org/XML) [The XML FAQ](https://xml.silmaril.ie/), [Overview of SGML Resources at W3C org](http://www.w3.org/MarkUp/SGML/)

## XML-RPC

**XML-RPC** is **Extensible Markup Language-Remote Procedure Call**.
A Remote Procedure Call (RPC) allows you to call (or request) another
application and expect that application to honor the request (answer the
call). So, **XML-RPC** allows a user (or [developer](#developer)) to send a request, formatted in [XML](#xml), to an external application.

-   Related articles: [XML-RPC Support](https://codex.wordpress.org/XML-RPC_Support)
-   External links: [Dave Winer’s XML-RPC for Newbies](http://davenet.scripting.com/1998/07/14/xmlRpcForNewbies), [XML-RPC Home Page](http://www.xmlrpc.com), [Apache XML-RPC](http://ws.apache.org/xmlrpc/), [XML-RPC for PHP Homepage](http://phpxmlrpc.sourceforge.net), [XML-RPC at Wikipedia](http://en.wikipedia.org/wiki/XML-RPC)

## More resources

More glossaries with collection of blogging terms, acronyms and abbreviations.

-   [Giant Blogging Terms Glossary](http://www.quickonlinetips.com/archives/2006/06/the-giant-blogging-terms-glossary/)
-   [Blogging Terms at Wikipedia](http://en.wikipedia.org/wiki/List_of_blogging_terms)
-   [External WordPress glossary with additional terms](https://www.wpglossary.net)
