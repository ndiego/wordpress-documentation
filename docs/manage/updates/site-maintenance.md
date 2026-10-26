---
title: Site maintenance
description: "A checklist of regular tasks that keep a WordPress site healthy: backups, updates, spam and broken links."
type: guide
order: 20
redirect_from:
  - /documentation/article/administer-your-blog/
  - /documentation/article/wordpress-housekeeping/
  - /documentation/article/wordpress-site-maintenance/
  - /documentation/category/maintenance/
---

# Site maintenance

> [!CAUTION]
> Please note that this is not a support page. If you seek help with your specific problem, please refer to the [Support forums](https://wordpress.org/support/welcome/).

## Getting a WordPress tune up

To keep WordPress working healthy, there is some site maintenance we recommend you do frequently.

Begin by creating a calendar of WordPress Maintenance procedures to remind yourself to get a maintenance job on your WordPress site on a regular basis.

In the article on [WordPress Housekeeping](site-maintenance.md), tips and resources are given to clean house in WordPress. These include cleaning out old plugins, upgrading WordPress, and other helpful tips for cleaning up and optimizing your WordPress Site.

To ensure you keep your WordPress site up-to-date and working in prime condition, consider adding these Housekeeping steps to your calendar, typically every three to six months.

## Update WordPress

WordPress is quickly growing and expanding as more features and functions are included and perfected. It is recommended that you check in with WordPress for updates and upgrades at least every three months, six months at the most. Check [WordPress org](https://wordpress.org/) and [Download WordPress](https://wordpress.org/download/) for information on the latest version available.

**Note:** For WordPress 3.7+, minor and security updates are automatically applied in the background process.

## Check for dead links

One of the most complained about aspect of using the Internet is the *dead link*. This is a link on a page or search engine that goes nowhere. It results in the 4**04 Page Error – Page Not Found**. These can come from links to external sites that have changed their address or closed, or it can come from internal links. When you [link between posts](https://codex.wordpress.org/Linking_Posts_Pages_and_Categories) in your post articles, you might have misspelled a [permalink address](../settings/permalinks.md) or put in the wrong post-ID, resulting in a **page not found** on your site. If you’ve recently made a change in your permalink structure, you might have some **404 page errors** that might need cleaning up.

Add to your WordPress maintenance list regularly scheduled visits to your site’s statistic logs to check on reports of **404 errors** on your site, and take time to run a links check on your external, and internal, links to make sure everything is still connected. Dependent upon the site and number of links on your site, you should check your site for dead links every six months to a year.

-   [W3C free check link free utility](http://validator.w3.org/checklink)
-   [AnyBrowser’s Link Checker](http://www.anybrowser.com/linkchecker.html)
-   [HTMLHelp Valet Link Checker](http://www.htmlhelp.com/tools/valet/)
-   [Squarefree’s Bookmarklets – javascripts for checking links](http://www.squarefree.com/bookmarklets/pagelinks.html)
-   [KeepNI’s link check (14 day evaluation, $299.00 US)](http://tools.keepni.com/)

## Check in with WordPress

The WordPress [Dashboard](../dashboard/README.md#dashboard--information-central), part of the [Administration Screens](../dashboard/README.md), help to keep you up-to-date on the WordPress Community and activities, but check the [WordPress](https://wordpress.org/) website to find out if there have been any upgrades, news, events, or information you may need to know as a WordPress user.

If you aren’t an active participant in the [WordPress Forums](https://wordpress.org/support/forums), check in once in a while to see what is going on and what topics are being discussed. There might be a topic that might interest you or news you should know.

Also visit the [WordPress Documentation](https://wordpress.org/support) here to find out if there is new documentation, events, information, or resources that will help you better run and manage your WordPress site.

## Delete spam comments

If you are using one of the many different Comment Spam WordPress Plugins with your WordPress blog, spam can collect in your database. Comment spam is stored in the database as a “just in case” so you can restore a comment incorrectly marked at comment spam. It also serves as a resource to track down recurrent comment spammers, if you need to.

In general, while some plugins will delete comment spam from your database after a specific period of time, not all do. These entries are dead-weight and unnecessary, and they can accumulate. To delete all current comment spam entries run this query on your WordPress database with [phpMyAdmin](https://github.com/WordPress/Advanced-administration-handbook/blob/main/upgrade/phpmyadmin.md) in the SQL page:

```text
DELETE FROM wp_comments WHERE comment_approved = 'spam'
```

## Back it up

Make it a part of your regularly scheduled maintenance to backup your WordPress site, both on the website host server and on your computer. For detailed information see [WordPress Backups](https://developer.wordpress.org/advanced-administration/security/backup/). Consider scheduling this, depending upon the volume of new posts or articles you add to your site, three to twelve times a year.

[Backing Up Your Database](https://github.com/WordPress/Advanced-administration-handbook/blob/main/security/backup-database.md) describes how to save a backup copy of your database tables that contain all your blog data, and [Restoring Your Database From Backup](https://developer.wordpress.org/advanced-administration/security/backup/) guides you through the process of restoring data using one of your backups should you ever have to do so.

## Update your site

If you haven’t been adding posts or articles lately, make a schedule to remind you to add new material on a regular basis. If you have, then take a look at what you’ve posted in the past and maybe do a little checking for proper grammar, bad spelling, information that needs updating, rewriting and editing a little, checking for any adjustments that should be made to make the information you’ve released to the public better.

Website looks change with time and maybe you are tired of your old look. It might need a little tweaking to improve its presentation and performance, or maybe it’s time for a new [WordPress Theme](../../design/themes/README.md).

Schedule site updates, depending upon how frequently you post new posts and articles, about every six months so your site will stay fresh and alive.

## Validate again

Make it a website maintenance policy to [validate your site](https://codex.wordpress.org/Validation) after making any code or style sheet changes. This way, you can keep on top of guaranteeing users won’t run into problems and trouble that might be brewing under the surface.

You can also regularly schedule validation tests on your site to keep it in top working condition and keep up with any changes or deprecations of the [CSS](https://codex.wordpress.org/CSS) and HTML standards. Typically, this should be done about once a year or when you make significant modifications to your site.

## Other maintenance tasks

For the serious blogger or website administrator, there are some site maintenance tasks you should do to keep up with your site based on site statistics data so that it improves hit ratio from search engine. Here are some suggestions to keep your site in top shape.

-   Check Your Website Statistics : Who is visiting, where they are visiting from, which pages are the most visited…check in regularly with your website statistics to find out where the action is on your site, where the dead links are, and where users are coming from. This information can help you better fine tune your site to meet the needs of your users and increase your web visibility. You should check site statistics at least monthly if you have an active site.
-   Check Your Linkability : There are many *link popularity* tools on the Internet that will check to see who is linking to you. This is part of the puzzle that search engines use to rank your site. Dependent upon your site’s activity and need to grow in search engine rankings, this should be done monthly, or at least three times a year.
-   Site Submissions : If you have a desire to make your site rise in search engine rankings, regularly schedule activity surrounding your site’s submissions to search engines and attracting new users. Take care to limit your submissions to the same search engine too frequently, as that can penalize you, but check in with your site submissions once or twice a year at a minimum.
-   Update Advertising : If you have included advertising in your site, check with your advertisers on a regular basis to make sure they haven’t changed their techniques, pricing, and process. Dependent upon site activity, this could be as often as once a month or several times a year.

### Site maintenance calendar

We’ve put together a sample calendar for your site maintenance to help you schedule time to keep your WordPress site tuned up and running smoothly.

|  |  |
| --- | --- |
| January | Upgrade or Update WordPress Check in with WordPress Add New Content |
| February | Add New Content Check for new Plugins Clean out Plugins Backup Database and Site Check Site Statistics Check Site’s Link Popularity and Search Engine Ranking |
| March | Clean up and/or Try New Theme Check in with WordPress Add New Content |
| April | Clean Out Graphics and Photographs Add New Content Backup Database and Site Check Site Statistics Submit Site to Search Engines |
| May | Check for Dead Links Check in with WordPress Add New Content |
| June | Backup Database and Site Add New Content Check Site Statistics Check Site’s Link Popularity and Search Engine Ranking Check Advertising |
| July | Upgrade or Update WordPress Check in with WordPress Add New Content |
| August | Check for New Plugins Clean Out Old Plugins Backup Database and Site Add New Content Check Site Statistics |
| September | Clean or Renew Themes Check in with WordPress Add New Content Submit Site to Search Engines Check Advertising |
| October | Backup Database and Site Validate Web Pages and CSS Optimize Web Pages and CSS Add New Content Check Site Statistics |
| November | Check in with WordPress Add New Content Check Site’s Link Popularity and Search Engine Ranking |
| December | Backup Database and Site Check Site Statistics Add New Content Check Advertising |

> [!CAUTION]
> Please note that this is not a support page. If you seek help with your specific problem, please refer to the [Support forums](https://wordpress.org/support/welcome/).

## Maintenance & security

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/category/maintenance/; edit it into the page. -->

Keeping a WordPress site healthy and safe: routine administration and housekeeping, updating
WordPress, plugins and themes, recovering from fatal errors, and protecting your site and your
visitors' privacy.

## Administer your blog

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/administer-your-blog/; edit it into the page. -->

Generally, the daily tasks associated with administering your WordPress site are quick and easy to do, freeing you to concentrate on the content, editorials, and stories you want to share with the world, and allowing you to get back to other activities.

Here is a quick look at the various activities involved in administering your WordPress site. Some of these may need to be done daily, while others can be done weekly, monthly, or less frequently. It depends upon your blogging activity level and the intent of your WordPress site.

### Daily tasks

#### Login and write

Most people begin by logging into their WordPress site because they have news, information, or a story to tell. So they head straight for the [Administration Screens](../dashboard/README.md) > [Posts](../dashboard/README.md#add-new-post) > [Add New](../../classic/classic-editor/write-posts-classic.md). There, the title is set, the information is entered, categories and tags chosen, and any other minor details noted, and with a click is published.

If you have any new images, movies, or music, to upload to your site, you can easily do that when writing the post or switch to the [Administration Screens](../dashboard/README.md) > [Media](../dashboard/README.md#media--add-pictures-and-movies-to-your-posts) > [Add New Screen](../../write/media/README.md) and add any other images to your WordPress site. Then, you can either add these to your new posts, or visit the [Administration Screens](../dashboard/README.md) > [Posts](../dashboard/README.md#add-new-post) > [Posts screen](../dashboard/posts-screen.md) and click Edit to edit the post in which you now wish to add an image. Again, click SAVE and it is released to the world.

Also, there are those [Drafts](../../write/publish/post-status.md#draft) sitting up at the top of the Write Post screen, which you can publish or move to the trash, if you’d like.

Luckily with WordPress, you have some options for dealing with all those posts. They don’t all have to be released today. Many people work ahead with their blog content, setting the dates into the future. When the day and time arrives, WordPress will automatically release the post, without any additional effort from you.

#### Checking comments

After you have cleaned up the content on your site, it is time to find out what they have been saying about what you say. On the [Administration Screens](../dashboard/README.md) > [Comments Screen](https://codex.wordpress.org/Comments_Screen), you can inspect the comments posted to your site. If a comment has been marked for [moderation approval](https://codex.wordpress.org/Comment_Moderation), it will look lighter colored than the rest of the comments. Click [Edit Comment](https://codex.wordpress.org/Manage_Comments_SubPanel#View_Mode) to access the comment and set it to be approved. Click **Delete Comment** if you want it removed.

The [Moderation Screen](https://codex.wordpress.org/Awaiting_Moderation_SubPanel) will segregate the comments awaiting moderation from the rest of the comments if you have set your [Administration Screens](../dashboard/README.md) > [Settings](../dashboard/README.md#settings--configuration-settings) > [Discussion](../settings/discussion.md) to moderate all comments. This allows for quick and easy comment moderation.

Determining which comments to keep and delete is a challenge. Be aware that often nice comments like *“I really like your site. Keep up the great work.”* and *“It shows you put a lot of time and effort in this. Thanks.”* might be benign comments, or more likely comment [spam](../../get-started/glossary.md#spam). To help you determine and check on what might be comment spam, and how to increase your protection against comment spammers, check out the following documents:

-   [Introduction to Dealing with Comment Spam](https://codex.wordpress.org/Comment_Spam)
-   [Moderating Comments](https://codex.wordpress.org/Comment_Moderation)
-   [Combating Comment Spam](https://codex.wordpress.org/Combating_Comment_Spam)
-   [Denying Access to Comment Spammers with .htaccess](https://codex.wordpress.org/Combating_Comment_Spam/Denying_Access)

#### Users and authors

If you have set your site set up to [allow users to register](https://codex.wordpress.org/Registered_User_Features) and submit articles, stop by your [Users Screen](../dashboard/README.md#users--your-blogging-family) to check on those who have registered and make any adjustments to their [User Roles and Capabilities](../users/roles-and-capabilities.md) as needed.

If you do allow users to post articles, be sure to check the [Administration Screens](../dashboard/README.md) > [Posts](../dashboard/README.md#add-new-post) > [Posts screen](../dashboard/posts-screen.md) for any newly posted articles in the **Drafts** or **Pending** status awaiting your review and release.

#### Check the dashboard

At this point, your daily tasks are almost complete. Your site is up-to-date and on its way to entertaining and educating the world. But, there is one last task you might want to check. Stop by your WordPress [Administration Screens](../dashboard/README.md) > [Dashboard](../dashboard/README.md#dashboard--information-central) > [Dashboard](../dashboard/dashboard-screen.md) screen and check to see if there are any new activities going on in the WordPress Community, especially any announcements about upgrades.

While there, take advantage of your handy “To Do List” featured on the Dashboard. This lists your most recently released posts, the next batch of scheduled entries, recent comments, blog stats, and incoming links (referrers). This helpful information lets you know what has been released to the public from your site, what is next on the list, and shows you, at a glance, to view the most recent comments.

The blog stats and incoming links give you different information. The Stats give you information about how many posts, comments, and categories are on your site. While this may not be critical information, you can use it as a general scoreboard or counter. The incoming links information tells you who has [pinged](../../get-started/glossary.md#pingback) or [trackbacked](../../get-started/glossary.md#trackback) your site. This helps your link popularity for your site and gives you an idea of who thought your site’s material was worthy of praise.

At the bottom of the page, you will see a list of your Drafts, waiting to be done.

### Administration tasks

As the administrator or site owner, there are a few more tasks you should add to your schedule. These do not have to be done daily, but they still need to be done on a regular basis. Many of these are outlined in the articles [WordPress Housekeeping](https://codex.wordpress.org/WordPress_Housekeeping) and [WordPress Site Maintenance](https://codex.wordpress.org/WordPress_Site_Maintenance). In general they are:

-   [Updating WordPress](README.md)
-   Check for Dead Links Throughout Your Site
-   [Check in with WordPress for Changes and Information](https://www.wordpress.org/)
-   [Backup Your WordPress Site and Database](https://github.com/WordPress/Advanced-administration-handbook/blob/main/security/backup-database.md)
-   [Update Your Site’s Content and/or Look](../../design/themes/README.md)
-   Update [Plugins](https://wordpress.org/plugins/managing-plugins/) and [Themes](../../design/themes/README.md)
-   [Check for Validation Errors](https://codex.wordpress.org/Validating_a_Website)
-   [Optimize Your WordPress Site](https://github.com/WordPress/Advanced-administration-handbook/blob/main/performance/optimization.md)

### More administration resources

-   [Administration Screens](../dashboard/README.md)
-   [What Registered Users Can Do](https://codex.wordpress.org/Registered_User_Features)
-   [Manage Categories](../dashboard/README.md#categories)
-   [Roles and Capabilities](../users/roles-and-capabilities.md)
-   [Manage WordPress Settings](../dashboard/README.md#settings--configuration-settings)
-   [Manage Discussion Options](../settings/discussion.md)
-   [Using Permalinks](../settings/permalinks.md)
-   [Moderate Comments](https://codex.wordpress.org/Comment_Moderation)
-   [Manage Plugins](../plugins.md)
-   [Manage Themes](../../design/themes/README.md)

## WordPress housekeeping

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/wordpress-housekeeping/; edit it into the page. -->

### Cleaning your WordPress house

Just as with your house, WordPress requires a little housekeeping once in a while to keep it working right. Here is a list of things you should do on a [regularly scheduled basis](site-maintenance.md) to keep your WordPress site running smoothly.

### Upgrade WordPress

If a new release of WordPress is out, we recommend that you [upgrade](README.md). These new releases often include [new and improved features](https://wordpress.org/about/features/) and fixes. It is recommended to check in with WordPress for updates and upgrades at least every three months, six months at the most. Check [WordPress.org](https://www.wordpress.org/) or [WordPress Downloads](https://wordpress.org/download/) for latest version available.

### Plugins

[Plugins](../plugins.md) are an exciting feature of WordPress. They add functions and features to your WordPress site such as adding customized post listings to featuring a local weather forecast on your site.

With the hundreds of plugins available, it’s fun to test drive them, trying out different ones to see what they will do, if you need them, and if they really add to your site or clutter things up. Once in a while, you should do a little housekeeping on your plugins.

#### Upgrade plugins

Every three to six months, check for the latest plugin version. This is easy to do from the [Administration](../dashboard/README.md) > [Plugin](../dashboard/README.md#plugins--add-functionality-to-your-blog) Screen. If an update is available, WordPress will notify you with a banner below the plugin. Just click the “upgrade automatically” link, or click the “Download” link if you would prefer to upgrade manually.

![Administration Plugins Screen.](https://wordpress.org/documentation/files/2019/03/plugins-screen.png)

*Administration Plugins Screen*

#### Delete old or unwanted plugins

To uninstall a WordPress Plugin:

1.  Go to **[Plugins](../dashboard/README.md#plugins--add-functionality-to-your-blog)** screen.
2.  Find the Plugin you wish to deactivate and uninstall.
3.  Click Deactivate.
4.  Click Delete.

The Plugin will initiate the deactivation and deletion.

Most WordPress Plugins have an option to completely uninstall themselves, though not all. If you wish to remove a WordPress Plugin permanently:

1.  Check the WordPress Plugin instructions in the **Details** readme file on how to properly uninstall the Plugin.
2.  If the WordPress Plugin required the addition of code to the WordPress Theme, manually edit the Theme files to remove it.
3.  Deactivate the Plugin and remove it manually through your FTP program.
    1.  Login to the site via your FTP Program.
    2.  Go to the Plugin directory and find where the Plugin is installed.
    3.  Delete the WordPress Plugin folder and/or files from your server.

#### New plugins

WordPress plugins are being added constantly. Every three to six months search the Internet or visit the [WordPress plugins repository](https://wordpress.org/plugins/) to see if there are any new plugins available that will improve your site. There might be a new plugin that will do what one of your older plugins do.

### Theme housekeeping

Just like plugins, many users love test driving all the different [WordPress Themes](../../design/themes/README.md) available. Some users might have twenty or more Themes in their theme list. If you aren’t using them, why not do a little housekeeping on your themes?

![Appearance Themes Screen.](https://wordpress.org/documentation/files/2019/03/800px-themes.png)

*Appearance Themes Screen*

To remove a theme from your WordPress site:

1.  Log in to the WordPress [Administration Screen](../dashboard/README.md).
2.  Select the [Appearance screen,](../dashboard/README.md#appearance--change-the-look-of-your-blog) then [Themes](../dashboard/README.md#themes).
3.  Select Theme Details for the theme you want to remove.
4.  Select Delete near the bottom-right corner.

#### Get a new theme

Tired of your old theme’s look? Maybe it’s time to do a little presentation housekeeping and change the look of your WordPress site. Thanks to WordPress’s support for [themes](../../design/themes/README.md), changing your site’s look is easy.

Check out the various resources for [WordPress Themes](../../design/themes/README.md). If you find one you like, install it and then activate it.

Don’t worry, your old theme will still be there. Test drive the new one for a while. You can always go back to the old one. If you are really determined to turn your theme housekeeping efforts into some serious work, check out the article on [Theme Development](https://developer.wordpress.org/themes/getting-started/what-is-a-theme/) to create your own unique theme.

### Unwanted images

Many users upload a lot of graphics to their site that they end up never using. If you find yourself with a lot of unused graphics and images, consider going through them and cleaning house by deleting them.

If you aren’t sure you will never need them again, but you aren’t using them now and want to remove them from your site if server site space is limited, move them to a folder in your hard drive WordPress folder called *backupimages* or something similar and store them there, *just in case*.

### Database optimization

Over time, your WordPress database can generate what’s called “overhead.” This condition is similar to a defragmented hard drive. There are some plugins that optimize your database (e.g. [WP-Sweep](https://wordpress.org/plugins/wp-sweep/))

### Maintenance schedule

In the article, [Lessons: WordPress Site Maintenance](site-maintenance.md), we cover website maintenance, but take a moment now to go through this list of WordPress housekeeping chores and add them to your calendar so you can clean up your site on a regular basis, keeping your WordPress site a lean and clean site to visit.
