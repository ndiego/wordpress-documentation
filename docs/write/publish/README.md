---
title: Publish
description: What publishing does, the status and visibility of a post or page, scheduling, and how to update or unpublish what is live.
type: guide
order: 70
---

# Publish

After reading this page you can publish a post or page, schedule it for later, choose who can see it, and change or take down something that is already live.

## What publishing does

Until you publish, a post or page is a draft that only logged-in users with the right role can see. When you select **Publish** and confirm in the pre-publish panel, WordPress gives it a public address, adds it to your site's lists (the blog page, category archives, the feed and search), and records the publish date. Pages are not added to the blog or the feed, but they get their address and appear wherever your navigation lists them.

## Status

Every post and page has a status, shown in the **Post** or **Page** tab of the settings sidebar:

- **Draft**: saved but not published. WordPress also saves drafts automatically while you write.
- **Pending**: written and waiting for an editor to review it. Contributors cannot publish, so their button says **Submit for Review**.
- **Scheduled**: set to publish automatically at a future date and time.
- **Published**: live on the site.
- **Private**: published, but visible only to logged-in users who can edit it, such as administrators and editors.

[Post status](post-status.md) explains each one.

## Visibility

Visibility decides who can read a published post or page:

- **Public**: everyone. This is the default.
- **Private**: only logged-in administrators and editors (and the author).
- **Password protected**: everyone can see the title, but only people who enter the password can read the content.

See [Content visibility](content-visibility.md) and [Password-protected content](password-protected.md).

## Schedule a post

In the settings sidebar, select the publish date (it shows **Immediately** for a new post) and choose a date and time in the future. The **Publish** button changes to **Schedule**. Select it and confirm. WordPress publishes the post at that time, using the timezone set in **Settings > General**, so check that the timezone is yours.

## Update something that is published

Open the post or page, make your changes, and select **Save**. The changes go live right away. Each save creates a revision, so you can compare versions and restore an earlier one: see [Revisions](revisions.md).

## Unpublish

To take a post or page down without deleting it, open its status in the settings sidebar and choose **Draft**, then select **Save**. It disappears from your site and stays in your list of posts or pages. To remove it, choose **Move to trash**; trashed items can be restored for 30 days.

## More publishing options

- [Sticky posts](sticky-posts.md) keep a post at the top of your blog page.
- [Excerpts](excerpts.md) are the short summaries shown in lists and search results.
