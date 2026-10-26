---
title: Comments
description: "How comments work in WordPress, where to manage them, and the settings that control who can comment and when."
type: guide
order: 90
redirect_from:
  - /documentation/article/comments-in-wordpress/
---

# Comments

Comments let visitors talk with you and with each other. When comments are open on a post or [page](../create-a-page.md), WordPress shows a comment form after the content; once a comment is approved, it appears below the content.

This page covers where comments are managed, the settings to review before you open comments, and how to turn comments on. The pages in this group go further into [moderation](comment-moderation.md), [spam](comment-spam.md) and [trackbacks and pingbacks](trackbacks-and-pingbacks.md).

## The Comments screen

All the comments on your site are listed on the **Comments** screen in the dashboard (see [Comments screen](comments-screen.md) for every option). It shows all comments by default.

![The 'Comments' page in the admin dashboard](https://wordpress.org/documentation/files/2020/04/comments-dashboard.png)

You can switch the view to see Pending, Approved, Spam, and Trash comments:

-   **Pending:** comments submitted by your visitors, but won’t be visible on your blog posts unless you approve them.
-   **Approved:** comments published and are publicly visible on your blog posts by all your website visitors.
-   **Spam**: comments flagged as possibly unwanted or irrelevant, and aren’t visible to your site visitors.
-   **Trash**: comments marked as unwanted and will be automatically deleted for good after 30 days.

Moving your mouse over to a comment will display the action links for it. You can approve a comment to make it visible to all your site visitors, or unapprove it to put it in pending status again.

You can also reply to comments. By replying to a specific comment, your reply will appear right under that comment. This is called “threaded” or “nested” comments.

You can also choose to edit anyone’s comments on your own site. The **Quick Edit** option opens a text area so you can edit the comment without reloading the page. **Edit**, on the other hand, gives you more options to edit the name, user email, and more.

When a visitor submits a comment, WordPress follows your settings and either holds it for your approval or publishes it right away.

If you see a comment marked as spam that’s actually a real comment, then you can mark it as **Not Spam** by hovering your mouse over it.

Comments you delete go to the trash, where you can restore them with **Restore**. WordPress deletes comments permanently after 30 days in the trash.

## Discussion settings

Before you enable comments on posts or [Pages](../create-a-page.md), reviewing the options under **Settings > Discussion** (see [Discussion settings](../../manage/settings/discussion.md)) can help make your life as a moderator easier. Use these settings to restrict comments and reduce the amount of spam you receive.

### Notification

![The 'Discussion Settings' section of the 'Settings' page in the admin dashboard](https://wordpress.org/documentation/files/2020/04/default-post-settings.png)

If you link another site post on your site, **Attempt to notify any blogs linked to from the post** will enable your site to notify the website owners that you have linked to them. They can then choose to tell their users that another site linked to them through a [trackback or pingback](trackbacks-and-pingbacks.md).

Just like the option above, you can enable your site to accept pingbacks and trackbacks from other websites by checking **Allow link notifications from other blogs (pingbacks and trackbacks) on new posts**.

### Comment rules

**Allow people to post comments on new articles** will enable you to disable comments if you don’t need comments on your websites.

![Other comments options on the 'Settings' page of the admin dashboard](https://wordpress.org/documentation/files/2020/04/other-comment-settings.png)

**Comment author must fill out name and e-mail** prevents people from leaving anonymous comments.

**Users must be registered and logged in to comment** will only allow registered users of your site to post comments.

**Automatically close comments on articles older than _____ days** will close comments on a post that have reached a set time. This is a good way to limit spam comments.

### Comment display

**Enable threaded (nested) comments _____ levels deep**: will allow your users to reply to one another. A reply to a comment is shown “nested” underneath the original comments. You can limit how many levels (a reply to a reply) of replies your site will allow by changing the number of levels.

**Break comments into Pages with _____top level comments per Page and the _____ Page displayed by default** will change how your comments are displayed. You can set how many comments you see per Page and if the oldest or newest comments are displayed first.

**Comments should be displayed with the _____ comments at the top of each Page** will place newer or older comments at the top of each page.

![Email and comment options on the 'Settings' page in the admin dashboard](https://wordpress.org/documentation/files/2020/04/comment-administration.png)

### Comment administration

**Email me whenever … Anyone posts a comment** and/or **A comment is held for moderation** will help you stay up to date on your comments. This helps if you don’t check your site often.

**Comment must be manually approved** will help you moderate the comments published on your site.

**Comment author must have a previously approved comment** will help moderate the comments published on your site.

### Comment spam

![The comment moderation and blocklist options on the 'Settings' page](https://wordpress.org/documentation/files/2020/04/comment-moderation.png)

**Hold a comment in the queue if it contains _____ links**, Spam comments are designed to get users to click on links in order to drive traffic to other sites. As a result, many spam comments contain multiple links. Setting this option to hold all comments that contain 2 or more links will help catch more spam.

You can use the **Comment Moderation** and **Disallowed Comment Keys** lists to catch spam that contains certain words or is posted from a particular IP address. Comments that match a disallowed key are not deleted but instead [moved to your spam folder](comment-moderation.md).

Because spam is pervasive on the Web, some of the comments you receive will most likely be spam. However, WordPress developers and administrators have already developed a number of [ways to prevent spam comments](comment-spam.md) from appearing on your site. Besides the options in **Settings > Discussion**, you can install a [WordPress Plugin](https://wordpress.org/plugins/) like [Akismet](http://akismet.com/) or [make other changes](comment-spam.md) to help you keep spam comments under control.

### Avatars

The settings under “Avatars” control the images your site displays next to comments. For an introduction, see [Gravatars](../../manage/users/gravatars.md).

## Turn on comments

Once you have decided on your discussion options, you are ready to enable comments. If you chose not to enable comments on all articles automatically, you can turn on comments for a specific post or Page in several ways.

### For one post or page

![WordPress block editor interface showing an empty post titled ‘Enter the article title here.’ On the right-hand side under the ‘Document’ tab, various post settings are visible. The ‘Discussion’ section is highlighted in yellow, with checkboxes for ‘Allow comments’ and ‘Allow pingbacks & trackbacks’ both checked.](https://wordpress.org/documentation/files/2020/04/enable-comment-on-page-1.png)

In the editor, open the post or page settings in the sidebar, find **Discussion**, and select **Allow comments**. Then save the post or page.

### From the Posts or Pages screen

![WordPress Quick Edit panel for a post. The panel displays fields for title, slug, date, author, categories, template, tags, and status. On the right side, the options ‘Allow Comments’ (checked) and ‘Allow Pings’ (unchecked) are highlighted in yellow, with the post status set to ‘Published.’](https://wordpress.org/documentation/files/2020/04/enable-comment-from-quick-edit.png)

Navigate to the Posts/Pages screen. In the list of pages or posts, find the one you want and hover your cursor over the title of the post. You will see several links appear underneath the title. Click “Quick Edit” and check “Allow Comments.” Click “Update” to turn comments on for that post.

### For several posts or pages at once

From the Posts/Pages screen, check the boxes next to the posts or Pages on which you want to enable comments. Select “Edit” from the “Bulk Edit” Dropdown box and click Apply. Then, select “Allow” next in the Comments dropdown box and finish by clicking “update.”
