---
title: Permalink settings
description: "Choose the structure of the URLs of your posts and archives on the Settings > Permalinks screen."
type: reference
order: 60
redirect_from:
  - /documentation/article/customize-permalinks/
  - /documentation/article/settings-permalinks-screen/
---

# Permalink settings

Permalinks are the permanent URLs of your posts, pages, categories, and other archive pages on your website. These URLs are permanent and should never be changed, hence the name *perma*link.

Permalinks help to create a URL structure that is easy for both humans and search engines to understand and share.

-   A permalink is used when another blogger wants to link to your article.
-   You share the permalink when you want to share your content on social media.
-   When Google wants to index your article, they use the permalink of the content.
-   When you want to share a blog post with your friend, you send the permalink of your content in an email.

## Permalink types

There are three types of WordPress permalinks:

### Plain permalinks

The default Plain Permalink also called the Ugly Permalink looks like this:

http://example.com/?p=N

with p as the parameter and N is the unique ID of the post or page in the database.

WordPress comes preinstalled with this setting. It works on all server environments. It is not user-friendly and also not optimized for search engines.

### Pretty permalinks

Pretty Permalinks are SEO-friendly and attractive. They usually contain several words such as the title of the post or page, post category, tag name, etc. You can use Keywords in the URL to make your content readable by search engines.

Pretty Permalinks also help others get an understanding of what the content of the page or post is by reading the URL.

Pretty Permalinks look like this:

http://example.com/2012/post-name/

or

http://example.com/2012/12/30/post-name

### Almost pretty permalinks

WordPress provides a third option called the Almost Pretty permalinks. These permalinks have /index.php prefixed before them, like so:

http://example.com/index.php/yyyy/mm/dd/post-name/

Except for this detail, they are similar to Pretty Permalinks.

## Choosing your permalink structure

On the WordPress dashboard, go to Settings → Permalinks Screen. You can choose one of the permalink structures or enter your own in the “Custom structure” field using the *structure tags*.

![Permalink settings in Admin Dashboard > Settings > Permalink](https://lh4.googleusercontent.com/Lcb0FZp6yKMbXUPN_IobSjNDSP3sl1IGphrkuwVdBzZ81rpigq04ewoiJd3drRIdEC_wrFjfV-smOvngr9enVzmff0eAdg2IeFPbMaHRT_I_AwUxNo5DfE_nyZPqqq-RHZu-BgLq)

There are six options to select from:

Plain: This is the Ugly Permalink setting.

Day and name: This uses a year/month/date format followed by your post name.

Month and name: This uses a year/month format followed by your post name.

Numeric: This option uses the ID of the post from the row in the wp_posts table of your database.

Post name: This one uses the name of your post.

Custom Structure: This field allows you to define your own custom URL structure using the structure tags available in WordPress.

The default setting is Plain, which is automatically configured when you install WordPress.

> [!NOTE]
> 

Your hosting provider should have set up the web servers with the necessary configurations for the Pretty and Almost Pretty Permalinks to work correctly. If they are not, then you need to contact your hosting provider.

### Structure tags

WordPress provides the following structure tags for creating your own custom permalinks. You can use these tags to customize your Pretty or Almost Pretty permalinks.

> [!NOTE]
> 

-   You do not put your website URL in the permalinks fields. You only use one of the structure tags or a combination of tags.
-   To use the Almost Pretty Permalinks, start your permalink structure with index.php/.
-   End your structure with either %post_id% or %postname% so that WordPress can target an individual post for every permalink. (E.g. /%year%/%monthnum%/%day%/%postname%/)

**%year%**

The year of the post in four digits, eg:  2018

**%monthnum%**

Month the post was published, in two digits, eg: 05

**%day%**

Day the post was published in two digits, eg: 28

**%hour%**

Hour of the day, the post was published, eg: 15

**%minute%**

Minute of the hour, the post was published, eg:  43

**%second%**

Second of the minute, the post was published, eg: 33

**%post_id%**

The unique ID of the post, eg: 423

**%postname%**

A sanitized version of the title of the post (*post slug* field on Edit Post/Page panel).

Eg: “This Is A Great Post!” becomes this-is-a-great-post in the URI.

**%category%**

A sanitized version of the category name (*category slug* field on New/Edit Category panel).

Nested sub-categories appear as nested directories in the URI.

**%author%**

A sanitized version of the post author’s name.

### Category base and Tag base

You also have the option of setting custom category and tag bases for your site on the same screen under the **Optional** settings section.

![Optional Category base and Tag base permalink settings in Admin Dashboard > Settings > Permalink](https://lh3.googleusercontent.com/T1ebzj_2xkBSUS9rNTXkrnIB_hB84Mc3MxCy2Sl82jesIPUO48GomcQzVfF5s-oVfABCm19HZsVvfUCBrBrUXVrDeolsyWvx1N2mFWaAeHCUy0J7ZG-OtXZuApJ8yFwZ09hr7-hV)

The *Category base* and *Tag base* are prefixes used in URLs for category and tag archives, which look like this:

example.net/category_base/category_name

example.net/tag_base/tag_name

The default values for *Category base* and *Tag base* are category and tag. You can change them, but you can’t remove them from the URLs altogether.

### Using %category% with multiple categories on a post

When you assign multiple categories to a post, only one can show up in the permalink. Which category gets displayed in the permalink is determined alphabetically.

If you want to choose which category shows up in the permalink, you can use one of the plugins from the [plugin directory](https://wordpress.org/plugins/search/taxonomy/).

## Settings Permalinks screen

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/settings-permalinks-screen/; edit it into the page. -->

**Permalinks** are the permanent URLs to your individual pages and blog posts, as well as your category and tag archives. A permalink is the web address used to link to your content. The URL to each post should be permanent and never change, hence the name permalink.

The **Settings Permalinks Screen** allows you to choose your default permalink structure. You can choose from common settings or create custom URL structures. You must click the **Save Changes** button at the bottom of the screen for the new settings to take effect.

By default, WordPress uses web URLs that have day and name in them; however, WordPress offers you the ability to create a custom URL structure for your permalinks and archives. This can improve the aesthetics, usability, and forward compatibility of your links.

For an introduction to Permalinks, read the [Pretty Permalinks](../../get-started/glossary.md#permalink) section of [Introduction to Blogging](../../get-started/what-is-wordpress.md). For a more in-depth description of the way this structure is specified, see the [Using Permalinks](permalinks.md) article.

![WordPress permalink settings screen](https://wordpress.org/documentation/files/2022/11/wordpress-permalink-settings.png)

### Customize Permalink structure

A [number of tags are available](#structure-tags), and here are some examples to get you started.

#### Common settings

Check one of the radio buttons corresponding to the correct Permalink Structure for your blog.

-   **Plain** – An example of the default structure is **http://www.sample.com/?p=123**
-   **Day and name** – An example of the day and name based structure is **http://www.sample.com/2008/03/31/sample-post/**
-   **Month and name** – An example of the month and name based structure is **http://www.sample.com/2008/03/sample-post/**
-   **Numeric** – An example of the numeric structure is **http://www.sample.com/archives/123**
-   **Post name** – An example of the post name structure is **http://www.sample.com/sample-post**
-   **Custom structure** – In the box specify the custom structure you desire to use. One example is **/archives/%year%/%monthnum%/%day%/%postname%/**. Look at the [Permalink Structure Tags](#structure-tags).

#### Optional

You may enter custom bases for your category and tag URLs here. For example, using **/topics/** as your category base would make your category links like **http://example.org/topics/uncategorized/**. If you leave these blank the defaults will be used. Again, see the [Permalink Structure Tags](#structure-tags).

-   **Category base** – Enter a custom prefix for your category URLs here.
-   **Tag base** – Enter a custom prefix for your tag URLs here.

#### Save changes

Click the **Save Changes** button to ensure any changes you have made to your Settings are saved to your database. Once you click the button, a confirmation text box will appear at the top of the page telling you your settings have been saved.

After you’ve clicked this button, you should receive one of two messages depending on whether your [.htaccess](../../get-started/glossary.md#htaccess) file is writeable.

-   If [.htaccess](../../get-started/glossary.md#htaccess) is writeable, you will get a message that says “**Permalink structure updated.**” You’re all set; WordPress has been able to do everything for you automatically.
-   If [.htaccess](../../get-started/glossary.md#htaccess) is *not* writeable, you will see a message at the top of the screen that says “**You should update your .htaccess now.**“. Near the bottom of the screen you will see “**If your .htaccess file were writable, we could do this automatically, but it isn’t so these are the mod_rewrite rules you should have in your [.htaccess](../../get-started/glossary.md#htaccess) file. Click in the field and press CTRL + a to select all.**” This means you’ll have to do one extra step yourself. In the text box at the bottom of the Screen, WordPress displays several lines of [rewrite](../../get-started/glossary.md#mod_rewrite) rules associated with the Permalink Structure you designated above. You need to manually copy everything in this text box into your [.htaccess](../../get-started/glossary.md#htaccess) file to make your new Permalinks work.

For information on how to make [.htaccess](../../get-started/glossary.md#htaccess) writeable, see [Changing File Permissions](https://developer.wordpress.org/advanced-administration/server/file-permissions/).

> [!NOTE]
> Visiting the Permalinks screen triggers a flush of rewrite rules. There is no need to save just to flush the rewrite rules.
>
> If you’re writing your [.htaccess](../../get-started/glossary.md#htaccess) file on your own local computer, remember, some operating systems do not allow the creation of a file named “`.htaccess`” because of the initial dot (“**`.`**“). You can always name the file without the initial dot or with a standard extension (e.g. “`htaccess.txt`“). Once the file is uploaded to your weblog’s directory, rename it with your [FTP](../../get-started/glossary.md#ftp) software. Most [FTP Clients](https://github.com/WordPress/Advanced-administration-handbook/blob/main/upgrade/ftp.md) should provide you a way to rename files this.

**Also Note**: Files that begin with a dot (“**`.`**“) like “`.htaccess`” are hidden on most servers by default. Consult the user guide or FAQ of the FTP software you use to find out how to have the software display these hidden files, and also how to use the software to change file permissions, rename files, etc. For more information on all of this see [Changing File Permissions](https://developer.wordpress.org/advanced-administration/server/file-permissions/).
