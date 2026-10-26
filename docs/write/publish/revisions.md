---
title: Revisions
description: The WordPress revisions system stores a record of each saved draft or published update. The revision system allows you to see what changes were made in each revision by dragging a slider.
type: guide
order: 60
redirect_from:
  - /documentation/article/revisions/
---

# Revisions

The WordPress revisions system stores a record of each saved draft or published update. The revision system allows you to see what changes were made in each revision by dragging a slider. The display indicates what has changed in each revision – what was added, what remained unchanged, and what was removed. Lines added or removed are highlighted, and individual character changes get additional highlighting. Click the **Restore**  button to restore a revision.

[Watch the video on VideoPress](https://videopress.com/v/4AXIEeKG)

https://videopress.com/v/4AXIEeKG

## View revisions

To view revisions:

1.  Open the Settings sidebar.
2.  Select the Page or Post tab.
3.  Click the number next to Revisions.

Since WordPress 7.0, clicking the revision opens a new revisions screen. If you are using WordPress 6.9 or earlier, see Classic Revisions below.

![Revision slider and revision list in the WordPress revisions screen.](https://wordpress.org/documentation/files/2019/02/view-revisions.jpg)

## Revisions screen

The revisions screen opens with a list of saved revisions in the Revision panel. Select a revision from the list to view it, or use the slider at the top of the screen to move forward or backward through revisions.

### Revisions summary

The list in the Revision panel provides another way to move between saved revisions. Select a revision to jump directly to that version.

### Top slider

The revisions screen lets you see what changed in each revision by dragging the top slider.

### Color indicators

Next to the scrollbar, you will see colored markers that indicate where changes were made and how large they are. Click a marker to jump to that location.

**Color meanings:**

-   Added blocks: solid green
-   Removed blocks: red, forward-slanting diagonal stripes
-   Modified blocks: yellow, backward-slanting diagonal stripes

### Show changes

The Show changes icon on the left side of the slider toggles the colored highlights on and off.

![Show changes icon](https://wordpress.org/documentation/files/2019/02/revisions-3-7.0.jpg)

## Restore a revision

To restore a revision:

1.  Use the top slider to find the revision you want to restore.
2.  Click Restore.

## Classic revisions

In WordPress 6.9 and earlier, clicking the revisions number in the sidebar opens the classic revisions screen. In WordPress 7.0, you can also open this screen by clicking Open classic revisions screen in the sidebar.

The classic revisions screen shows a side-by-side comparison of the HTML version of the content.

![Classic revisions screen](https://wordpress.org/documentation/files/2019/02/revisions-2-7.0.jpg)

Like the new revisions screen, you can see what changed in each revision by dragging the slider or using the Next and Previous buttons.

The revisions page also includes a Compare any two revisions mode that lets you compare any two revisions. In this mode, the slider has two handles: one for the revision you are comparing from and one for the revision you are comparing to. Drag the handles to see the changes between any two specific revisions.

## Autosaves

There is only ever a maximum of one [autosave](../../get-started/glossary.md#autosave)per user for any given post. New autosaves overwrite old autosaves. This means that no, your tables do not grow by one row every 60 seconds. In multi-user settings, one autosave is stored for each user.

Autosaves are enabled for all posts and pages but do not overwrite published content. Autosaves are stored as a special type of revision; they do not overwrite the actual post. In fact, whether your power goes out, your browser crashes, or you lose your internet connection, when you go back to edit that post, WP will toss up a warning telling you that it has a backup of your post and a link to restore the backup.

In the revisions timeline, autosaves are marked with an Autosave label.

![Autosave label on a revision post](https://wordpress.org/documentation/files/2019/02/revision-autosave.png)

## Revision options

Limit the number of posts revisions that WordPress stores in the database.

The [wp_revisions_to_keep](https://codex.wordpress.org/Plugin_API/Filter_Reference/wp_revisions_to_keep) filter allows developers to easily alter how many revisions are kept for a given post.

Alternately, the limit can be set in wp-config.php:

```text
define( 'WP_POST_REVISIONS', 3 );
```

WP_POST_REVISIONS:

-   true (default), -1: store every revision
-   false, 0: do not store any revisions (except the one autosave per post)
-   (int) > 0: store that many revisions (+1 autosave per user) per post. Old revisions are automatically deleted when the post is updated again.

## Revision storage method

Revisions are stored in the posts table.

Revisions are stored as children of their associated post (the same thing we do for attachments). They are given a post_status of ‘inherit’, a post_type of ‘revision’, and a post_name of {parent ID}- revision(-#) for regular revisions and {parent ID}-autosave for autosaves.

By default, WP keeps track of the changes to title, author, content, excerpt.

## Revision management

Deleting: There is an API function to delete revisions, but there is no UI. That can certainly change.

## Displaying rendered revisions

Currently revision comparison “diffs” are rendered in Text (or HTML) view; proposed filters would allow plugin developers to customize diff encoding/rendering. (see Trac ticket [#24908](https://core.trac.wordpress.org/ticket/24908))
