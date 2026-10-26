---
title: How a WordPress site is put together
description: The mental model of WordPress. Content, blocks, themes, templates, plugins and users, and how they combine into the pages visitors see.
type: concept
order: 60
---

# How a WordPress site is put together

After reading this page you can name the parts of a WordPress site, say what each one is for, and know where to go to change any part of it. The rest of this documentation uses these words without explaining them again.

![A diagram of how a WordPress page is built. Content such as posts, pages, media and comments is made of blocks; a template places the blocks along with the header and footer parts; the theme styles them with colors, fonts, spacing and layout; the result is the page a visitor sees. Below, plugins can add to every step, and the site is stored in a database and in files.](images/how-wordpress-works.svg)

## Content

Content is what you write and upload. WordPress has four main kinds.

- **Posts** are dated entries, shown newest first on your blog page, in archives and in feeds. News, articles and updates are posts.
- **Pages** are standalone and not dated: About, Contact, Services. Pages can have parent pages, so you can build a hierarchy such as Services > Design.
- **Media** is every file you upload: images, video, audio and documents. They live in the **Media Library** and you can use each one in many places.
- **Comments** are what visitors write in reply to posts (and to pages, if you allow it). You approve, answer or delete them.

Plugins can add more kinds of content, such as products or events. WordPress calls each kind a [post type](../write/organize/post-types.md).

## Structure

Posts are grouped with **categories** and **tags**. Categories are the broad sections of your site, and can have subcategories. Tags are optional keywords that cross categories. Visitors can browse each category and tag as its own list of posts. See [Organize your content](../write/organize/README.md).

## Blocks

Blocks are the unit of everything you edit. A paragraph is a block, and so is a heading, an image, a button, a list of your latest posts, the site title and the navigation menu. You add, move and style blocks the same way wherever they are, in a post, a page or the site's header.

Some blocks hold other blocks. A Columns block holds a Column block for each column, and each Column holds whatever you put in it. This is how you build layouts without code. See [Working with blocks](../write/blocks/README.md) and the [block reference](../blocks/README.md).

## Appearance

How your site looks comes from its **theme**. You can change themes at any time; your content stays the same, and only its presentation changes.

Most current themes are **block themes**, and their look is made of the same blocks as your content:

- **Templates** define the layout of each kind of view: a single post, a page, the blog, a category archive, the search results, the 404 page. WordPress picks the template that matches what the visitor asked for.
- **Template parts** are pieces shared by many templates, such as the header and footer. Change the header once and it changes everywhere.
- **Styles** set colors, fonts, spacing and layout for the whole site and for each type of block. A theme can offer several style variations to choose from.
- **Patterns** are ready-made groups of blocks, such as a hero section or a pricing table, that you insert and then change. Some patterns are synced, so editing one updates it everywhere it appears.

You edit all of these in the **Site Editor**, at **Appearance > Editor**. See [Design your site](../design/README.md). Older **classic themes** are built differently and use the Customizer, widgets and menus; [Classic WordPress](../classic/README.md) covers them.

## Plugins

Plugins add features to WordPress: contact forms, online stores, search engine settings, backups, new blocks. You install them from the [Plugin Directory](https://wordpress.org/plugins/) at **Plugins > Add Plugin**, and turn them on and off at any time. A plugin can add a screen to the admin menu, new blocks to the editor, or a new kind of content. Install only the plugins you need, and keep them updated. See [Plugins](../manage/plugins.md).

## Users and roles

Everyone who logs in to your site is a user, and each user has a **role** that decides what they can do:

- **Administrator**: everything, including themes, plugins, settings and other users.
- **Editor**: publish and manage all posts and pages, including other people's.
- **Author**: publish and manage their own posts.
- **Contributor**: write their own posts, but not publish them.
- **Subscriber**: manage their own profile.

Give each person the lowest role that lets them do their work. See [Users and roles](../manage/users/README.md).

## The dashboard and the front end

Your site has two sides. The **front end** is the site visitors see. The **dashboard** (also called the admin or wp-admin, at `/wp-admin/`) is where logged-in users manage it: writing in the editor, designing in the Site Editor, changing settings. When you are logged in, the toolbar at the top of the screen lets you move between the two. Changes you make in the dashboard appear on the front end when you save or publish them.

## Where everything is stored

A WordPress site is two things on the server: a **database** and **files**. The database (MySQL or MariaDB) holds your content, comments, users, settings, and the changes you make to templates and styles in the Site Editor. The files are WordPress itself, your themes and plugins, the `wp-config.php` file that tells WordPress how to reach the database, and your uploaded media in `wp-content/uploads`. A complete backup includes both. When a visitor asks for a page, WordPress reads the content from the database, finds the right template in the theme, renders the blocks, and sends the result to the browser as HTML.

## Next

You have finished the Get started path. Pick a task: [Write and edit](../write/README.md), [Design your site](../design/README.md) or [Manage your site](../manage/README.md). Keep the [Glossary](glossary.md) at hand for any word you meet.
