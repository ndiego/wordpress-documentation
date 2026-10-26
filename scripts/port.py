#!/usr/bin/env python3
"""One-shot migration of the hub's user documentation into docs/.

Reads wporg-docs/content/{get-started,content,blocks,design,administration,classic} (read-only) and writes the
pages under docs/ following the map in STRUCTURE.md ("The map from the hub" and the tables).

What it does to each page:

- moves it to its new path (MAP below, rules first, then the explicit table);
- rewrites the front matter to this repository's schema: title, description, type, order, slug, redirect_from
  (id, section, path, audience and applies_to are dropped);
- sets the H1 to the new title, normalizes title-case headings to sentence case and closes skipped heading levels;
- rewrites relative links to the new paths, and links into hub sections that do not exist here (the theme and
  plugin handbooks, reference, ...) to the matching page on developer.wordpress.org;
- drops boilerplate: the documentation edit logs ("Changelog" with "Updated <date>" entries; git history
  replaces them) and default theme self-links to "the theme's changelog";
- fills empty image alt text from the italic caption that follows the image;
- converts any remaining notice markup ([info], [tip], [alert], [warning], <div class="callout">) to alerts.

Retired pages are not written; their redirect_from entries move to the page they redirect to. Pages owned by
another author (OTHER below) are not written either; their redirects are printed so they can be added there.

Usage: python3 -I scripts/port.py [--src PATH] [--dry-run]
"""
import argparse
import os
import re
import sys
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DOCS = os.path.join(REPO, "docs")
DEFAULT_SRC = "/Users/nickdiego/Developer/wporg-docs/content"
SECTIONS = ("get-started", "content", "blocks", "design", "administration", "classic")
DEV = "https://developer.wordpress.org"

# Pages written by someone else in this repository. The port links to them but never writes them.
OTHER = {
    "README.md", "get-started/README.md", "get-started/what-is-wordpress.md",
    "get-started/choose-where-to-run-wordpress.md", "get-started/install-wordpress.md",
    "get-started/your-first-site.md", "get-started/how-wordpress-works.md", "write/README.md",
    "write/create-a-post.md", "write/publish/README.md", "design/README.md", "manage/README.md",
    "manage/security/README.md",
}

# Explicit moves. A value of ("retire", target) means the page is not written and its redirects go to target.
EXPLICIT = {
    "get-started/README.md": "get-started/README.md",
    "get-started/glossary/README.md": "get-started/glossary.md",
    "get-started/glossary/wordpress-semantics.md": ("retire", "get-started/glossary.md"),
    "get-started/install-wordpress/README.md": "get-started/install-wordpress.md",
    "get-started/install-wordpress/hosting-wordpress.md": "get-started/choose-where-to-run-wordpress.md",
    "get-started/what-wordpress-is/README.md": "get-started/the-wordpress-project.md",
    "get-started/what-wordpress-is/where-to-find-help.md": "get-started/where-to-find-help.md",
    "get-started/what-wordpress-is/wordpress-org-and-wordpress-com.md": "get-started/wordpress-org-and-wordpress-com.md",
    "get-started/your-first-site/README.md": "get-started/your-first-site.md",
    "get-started/your-first-site/get-started-with-wordpress.md": ("retire", "get-started/your-first-site.md"),
    "get-started/your-first-site/introduction-to-blogging.md": ("retire", "get-started/what-is-wordpress.md"),
    "content/README.md": "write/README.md",
    "content/seo.md": "write/seo.md",
    "content/posts-and-pages/README.md": ("retire", "write/README.md"),
    "content/posts-and-pages/create-pages.md": "write/create-a-page.md",
    "content/posts-and-pages/password-protected-posts.md": "write/publish/password-protected.md",
    "content/comments/README.md": ("retire", "write/comments/README.md"),
    "content/comments/comments-in-wordpress.md": "write/comments/README.md",
    "content/custom-fields/README.md": "write/organize/custom-fields.md",
    "content/the-editor/editor-notes.md": "write/editor/notes.md",
    "content/the-editor/editor-preview.md": "write/editor/preview.md",
    "content/the-editor/editor-preferences.md": "write/editor/preferences.md",
    "blocks/README.md": ("retire", "blocks/README.md"),
    "blocks/all-blocks/README.md": ("retire", "blocks/README.md"),
    "blocks/all-blocks/all-blocks-overview.md": "blocks/README.md",
    "blocks/embeds.md": "blocks/embeds.md",
    "blocks/working-with-blocks/README.md": ("retire", "write/blocks/README.md"),
    "blocks/working-with-blocks/work-with-blocks.md": "write/blocks/README.md",
    "blocks/working-with-blocks/adding-a-block.md": "write/blocks/add-a-block.md",
    "blocks/working-with-blocks/moving-blocks.md": "write/blocks/move-blocks.md",
    "design/README.md": "design/README.md",
    "design/fonts.md": "design/site-editor/fonts.md",
    "design/navigation.md": "design/site-editor/navigation.md",
    "design/styles/README.md": "design/site-editor/styles.md",
    "design/templates/README.md": "design/site-editor/templates.md",
    "design/patterns/pattern-directory/README.md": "design/patterns/pattern-directory.md",
    "design/patterns/pattern-directory/submit-a-pattern.md": "design/patterns/submit-a-pattern.md",
    "administration/README.md": "manage/README.md",
    "administration/manage-plugins.md": "manage/plugins.md",
    "administration/privacy/README.md": "manage/privacy.md",
    "administration/server-configuration/wp-config-basics.md": "manage/wp-config.md",
    "administration/performance/changes-not-showing.md": "manage/troubleshooting/changes-not-showing.md",
    "administration/users-roles/add-new-user.md": "manage/users/add-a-user.md",
}

# (prefix in the hub, prefix here, function applied to the remaining file name)
RULES = [
    ("content/the-editor/", "write/editor/", None),
    ("content/posts-and-pages/formatting/", "write/formatting/", None),
    ("content/posts-and-pages/", "write/publish/", None),
    ("content/organize-your-content/", "write/organize/", lambda n: n.replace("-screen.md", ".md")),
    ("content/media-library/", "write/media/", None),
    ("content/comments/", "write/comments/", None),
    ("blocks/working-with-blocks/", "write/blocks/", None),
    ("blocks/block-settings/", "write/block-settings/", lambda n: n.replace("block-settings-", "")),
    ("design/choose-and-install-a-theme/", "design/themes/", None),
    ("design/default-themes/", "design/themes/default-themes/", lambda n: n.replace("default-theme-", "")),
    ("design/site-editor/", "design/site-editor/", None),
    ("design/patterns/", "design/patterns/", None),
    ("administration/admin-screens/", "manage/dashboard/", None),
    ("administration/settings/", "manage/settings/", lambda n: n.replace("settings-", "", 1) if n.startswith("settings-") else n),
    ("administration/users-roles/", "manage/users/", None),
    ("administration/site-health/", "manage/troubleshooting/", None),
    ("administration/updates/", "manage/updates/", None),
    ("administration/security/", "manage/security/", None),
    ("classic/", "classic/", None),
]

# Hub sections that are not part of this repository, and where their pages live on developer.wordpress.org.
EXTERNAL = {
    "reference/wp-cli-commands.md": f"{DEV}/cli/commands/",
}
EXTERNAL_ROOTS = {
    "themes": f"{DEV}/themes/",
    "plugins": f"{DEV}/plugins/",
    "block-editor": f"{DEV}/block-editor/",
    "apis": f"{DEV}/apis/",
    "reference": f"{DEV}/reference/",
    "build": f"{DEV}/",
    "contribute": "https://make.wordpress.org/",
    "contribute-code": f"{DEV}/coding-standards/",
}

# STRUCTURE.md tables: type, title and order for every page here. Block pages and default themes are added below.
PAGES = {
    # get-started
    "get-started/wordpress-org-and-wordpress-com.md": ("concept", "WordPress.org and WordPress.com", 20),
    "get-started/the-wordpress-project.md": ("concept", "The WordPress project", 70),
    "get-started/where-to-find-help.md": ("guide", "Where to find help", 80),
    "get-started/glossary.md": ("reference", "Glossary", 90),
    # write
    "write/create-a-page.md": ("guide", "Create a page", 20),
    "write/editor/README.md": ("concept", "The editor", 30),
    "write/editor/settings-sidebar.md": ("reference", "Page and post settings sidebar", 10),
    "write/editor/preview.md": ("guide", "Preview", 20),
    "write/editor/notes.md": ("guide", "Notes", 30),
    "write/editor/preferences.md": ("reference", "Preferences", 40),
    "write/editor/distraction-free-mode.md": ("guide", "Distraction free mode", 50),
    "write/editor/keyboard-shortcuts.md": ("reference", "Keyboard shortcuts", 60),
    "write/blocks/README.md": ("guide", "Working with blocks", 40),
    "write/blocks/add-a-block.md": ("guide", "Add a block", 10),
    "write/blocks/move-blocks.md": ("guide", "Move blocks", 20),
    "write/blocks/list-view.md": ("guide", "List View", 30),
    "write/blocks/more-options.md": ("reference", "More options", 40),
    "write/blocks/rich-text-options.md": ("reference", "Rich text options", 50),
    "write/blocks/link-control.md": ("guide", "Links", 60),
    "write/blocks/page-jumps.md": ("guide", "Page jumps", 70),
    "write/blocks/block-directory.md": ("guide", "Block Directory", 80),
    "write/blocks/block-error.md": ("guide", "Block errors", 90),
    "write/block-settings/README.md": ("reference", "Block settings and design tools", 50),
    "write/block-settings/color.md": ("reference", "Color", 10),
    "write/block-settings/typography.md": ("reference", "Typography", 20),
    "write/block-settings/dimensions.md": ("reference", "Dimensions", 30),
    "write/block-settings/border.md": ("reference", "Border and shadow", 40),
    "write/block-settings/background.md": ("reference", "Background", 50),
    "write/block-settings/layout.md": ("reference", "Layout", 60),
    "write/block-settings/position.md": ("reference", "Position", 70),
    "write/block-settings/filters.md": ("reference", "Filters and duotone", 80),
    "write/block-settings/responsive.md": ("reference", "Responsive styles", 90),
    "write/block-settings/advanced.md": ("reference", "Advanced", 100),
    "write/media/README.md": ("guide", "Media", 60),
    "write/media/add-media.md": ("guide", "Add media", 10),
    "write/media/edit-media.md": ("guide", "Edit media", 20),
    "write/media/image-sizes.md": ("concept", "Image sizes and quality", 30),
    "write/publish/post-status.md": ("reference", "Post status", 10),
    "write/publish/content-visibility.md": ("guide", "Content visibility", 20),
    "write/publish/password-protected.md": ("guide", "Password-protected content", 30),
    "write/publish/sticky-posts.md": ("guide", "Sticky posts", 40),
    "write/publish/excerpts.md": ("guide", "Excerpts", 50),
    "write/publish/revisions.md": ("guide", "Revisions", 60),
    "write/organize/README.md": ("concept", "Organize your content", 80),
    "write/organize/categories.md": ("guide", "Categories", 10),
    "write/organize/tags.md": ("guide", "Tags", 20),
    "write/organize/taxonomies.md": ("concept", "Taxonomies", 30),
    "write/organize/post-types.md": ("concept", "Post types", 40),
    "write/organize/custom-fields.md": ("guide", "Custom fields", 50),
    "write/organize/static-front-page.md": ("guide", "Set a static front page", 60),
    "write/organize/search-page.md": ("guide", "Create a search page", 70),
    "write/comments/README.md": ("guide", "Comments", 90),
    "write/comments/comments-screen.md": ("reference", "Comments screen", 10),
    "write/comments/comment-moderation.md": ("guide", "Comment moderation", 20),
    "write/comments/comment-spam.md": ("guide", "Comment spam", 30),
    "write/comments/trackbacks-and-pingbacks.md": ("concept", "Trackbacks and pingbacks", 40),
    "write/formatting/README.md": ("reference", "Formatting", 100),
    "write/formatting/character-entities.md": ("reference", "Character entities", 10),
    "write/formatting/emoji.md": ("reference", "Emoji", 20),
    "write/formatting/smilies.md": ("reference", "Smilies", 30),
    "write/formatting/post-content-processing.md": ("reference", "How WordPress processes post content", 40),
    "write/seo.md": ("guide", "Search engine optimization", 110),
    # blocks
    "blocks/README.md": ("reference", "Blocks", 30),
    "blocks/text/README.md": ("reference", "Text blocks", 10),
    "blocks/media/README.md": ("reference", "Media blocks", 20),
    "blocks/design/README.md": ("reference", "Design blocks", 30),
    "blocks/widgets/README.md": ("reference", "Widget blocks", 40),
    "blocks/theme/README.md": ("reference", "Theme blocks", 50),
    "blocks/embeds.md": ("reference", "Embeds", 60),
    # design
    "design/themes/README.md": ("guide", "Themes", 10),
    "design/themes/block-themes.md": ("concept", "Block themes", 10),
    "design/themes/themes-screen.md": ("reference", "Themes screen", 20),
    "design/themes/default-themes/README.md": ("reference", "Default themes", 30),
    "design/site-editor/README.md": ("guide", "The Site Editor", 20),
    "design/site-editor/templates.md": ("concept", "Templates and template parts", 10),
    "design/site-editor/styles.md": ("guide", "Styles", 20),
    "design/site-editor/fonts.md": ("guide", "Fonts", 30),
    "design/site-editor/navigation.md": ("guide", "Navigation", 40),
    "design/site-editor/site-icon.md": ("guide", "Site icon", 50),
    "design/site-editor/command-palette.md": ("guide", "Command Palette", 60),
    "design/patterns/README.md": ("concept", "Patterns", 30),
    "design/patterns/pattern-directory.md": ("guide", "Pattern Directory", 10),
    "design/patterns/submit-a-pattern.md": ("guide", "Submit a pattern", 20),
    # manage
    "manage/dashboard/README.md": ("reference", "Dashboard and admin screens", 10),
    "manage/dashboard/dashboard-screen.md": ("reference", "Dashboard screen", 10),
    "manage/dashboard/posts-screen.md": ("reference", "Posts screen", 20),
    "manage/dashboard/pages-screen.md": ("reference", "Pages screen", 30),
    "manage/dashboard/tools-screen.md": ("reference", "Tools screen", 40),
    "manage/settings/README.md": ("reference", "Settings", 20),
    "manage/settings/general.md": ("reference", "General settings", 10),
    "manage/settings/writing.md": ("reference", "Writing settings", 20),
    "manage/settings/reading.md": ("reference", "Reading settings", 30),
    "manage/settings/discussion.md": ("reference", "Discussion settings", 40),
    "manage/settings/media.md": ("reference", "Media settings", 50),
    "manage/settings/permalinks.md": ("reference", "Permalink settings", 60),
    "manage/settings/connectors.md": ("reference", "Connectors settings", 70),
    "manage/settings/date-and-time-format.md": ("reference", "Date and time format", 80),
    "manage/users/README.md": ("guide", "Users and roles", 30),
    "manage/users/roles-and-capabilities.md": ("reference", "Roles and capabilities", 10),
    "manage/users/add-a-user.md": ("guide", "Add a user", 20),
    "manage/users/users-screen.md": ("reference", "Users screen", 30),
    "manage/users/your-profile.md": ("reference", "Your profile", 40),
    "manage/users/gravatars.md": ("guide", "Gravatars", 50),
    "manage/plugins.md": ("guide", "Plugins", 40),
    "manage/updates/README.md": ("guide", "Updates", 50),
    "manage/updates/auto-updates.md": ("guide", "Auto-updates", 10),
    "manage/updates/site-maintenance.md": ("guide", "Site maintenance", 20),
    "manage/updates/update-php.md": ("guide", "Update PHP", 30),
    "manage/security/password-best-practices.md": ("guide", "Password best practices", 10),
    "manage/security/site-was-hacked.md": ("guide", "My site was hacked", 20),
    "manage/privacy.md": ("guide", "Privacy", 70),
    "manage/troubleshooting/README.md": ("guide", "Site Health and troubleshooting", 80),
    "manage/troubleshooting/faq-troubleshooting.md": ("guide", "Troubleshooting FAQ", 10),
    "manage/troubleshooting/recovery-mode.md": ("guide", "Recovery mode", 20),
    "manage/troubleshooting/changes-not-showing.md": ("guide", "Changes not showing", 30),
    "manage/wp-config.md": ("reference", "wp-config.php for site owners", 90),
    # classic
    "classic/README.md": ("guide", "Classic WordPress", 70),
    "classic/classic-editor/README.md": ("guide", "Classic Editor", 10),
    "classic/classic-editor/write-posts-classic.md": ("guide", None, 10),
    "classic/classic-editor/write-code-in-posts.md": ("guide", None, 20),
    "classic/classic-editor/audio-video-shortcodes.md": ("reference", None, 30),
    "classic/widgets-menus-customizer/README.md": ("guide", None, 20),
    "classic/widgets-menus-customizer/customizer.md": ("guide", None, 10),
    "classic/widgets-menus-customizer/widgets-screen.md": ("reference", None, 20),
    "classic/widgets-menus-customizer/block-widgets-editor.md": ("guide", None, 30),
    "classic/widgets-menus-customizer/menus-screen.md": ("reference", None, 40),
}

# Slugs that would otherwise collide with another page's default slug.
SLUGS = {
    "write/blocks/README.md": "work-with-blocks",
    "blocks/text/README.md": "text-blocks",
    "blocks/media/README.md": "media-blocks",
    "blocks/design/README.md": "design-blocks",
    "blocks/widgets/README.md": "widget-blocks",
    "blocks/theme/README.md": "theme-blocks",
    "manage/settings/media.md": "media-settings",
}

# Descriptions that the hub got wrong (truncated, out of date or too long); the rest come from the hub.
DESCRIPTIONS = {
    "write/comments/README.md": "How comments work in WordPress, where to manage them, and the settings that control who can comment and when.",
    "blocks/README.md": "Every block that ships with WordPress, grouped the way the block inserter groups them.",
    "write/blocks/README.md": "The tools every block shares: the block toolbar, the settings sidebar, selecting, grouping and transforming blocks.",
    "get-started/the-wordpress-project.md": "Where WordPress came from, how it is released, and the community and philosophy behind it.",
    "manage/wp-config.md": "What the wp-config.php file does, where to find it, and the settings a site owner is most likely to change.",
    "classic/README.md": "The Classic Editor, widgets, menus and the Customizer, for sites that use the Classic Editor plugin or a classic theme.",
}

DESCRIPTIONS.update({
    'blocks/design/buttons.md': 'Add one or more buttons that link to other pages or sites with the Buttons block.',
    'blocks/design/columns.md': 'Lay out text, images and other blocks side by side in columns with the Columns block.',
    'blocks/design/group/README.md': 'Put blocks together in a Group block so you can style, move and lay them out as one unit.',
    'blocks/design/group/grid.md': 'Arrange blocks in a grid of rows and columns with the Grid variation of the Group block.',
    'blocks/design/group/row.md': 'Arrange blocks side by side in a single horizontal line with the Row variation of the Group block.',
    'blocks/design/group/stack.md': 'Stack blocks one above the other with the Stack variation of the Group block.',
    'blocks/design/home-link.md': "Add a link to your site's home page inside a Navigation block with the Home Link block.",
    'blocks/design/more.md': 'Show only the start of a post on your blog page, with a link to read the rest, using the More block.',
    'blocks/design/navigation-link.md': 'Add a link to a page, post, category or any URL inside a Navigation block with the Custom Link block.',
    'blocks/design/navigation-submenu.md': 'Add a dropdown list of links inside a Navigation block with the Submenu block.',
    'blocks/design/nextpage.md': 'Split a long post or page into several pages with the Page Break block.',
    'blocks/design/separator.md': 'Add a horizontal line between sections of content with the Separator block.',
    'blocks/design/spacer.md': 'Add empty space between blocks with the Spacer block.',
    'blocks/embeds.md': 'Add videos, posts, audio and other content from YouTube, Vimeo, Spotify and many other sites with the Embed block.',
    'blocks/media/audio.md': 'Add an audio file, such as music or a podcast episode, to a post or page with the Audio block.',
    'blocks/media/cover.md': 'Put text over an image, a video or a color with the Cover block, for headers, banners and calls to action.',
    'blocks/media/file.md': 'Add a link to a file that visitors can download, with an optional download button, using the File block.',
    'blocks/media/gallery.md': 'Show several images together with the Gallery block, and choose its columns, image sizes and links.',
    'blocks/media/image.md': 'Add an image to a post or page with the Image block, then crop, resize, link and caption it.',
    'blocks/media/media-text.md': 'Place an image or video side by side with text using the Media & Text block.',
    'blocks/media/video.md': 'Upload a video, or pick one from the Media Library, and show it in a post or page with the Video block.',
    'blocks/text/code.md': 'Show code examples exactly as typed, in a monospaced font, with the Code block.',
    'blocks/text/details.md': 'Hide content behind a short summary that visitors click to expand, using the Details block.',
    'blocks/text/footnotes.md': 'Add numbered notes to a post or page and list them at the end with the Footnotes block.',
    'blocks/text/freeform.md': 'Edit content with the Classic Editor toolbar inside the block editor using the Classic block.',
    'blocks/text/heading.md': 'Add headings that introduce sections and give a page a clear structure with the Heading block.',
    'blocks/text/list.md': 'Create a bulleted or numbered list, with nested items, using the List block.',
    'blocks/text/paragraph.md': 'Add and format text with the Paragraph block, the default block in the editor.',
    'blocks/text/preformatted.md': 'Show text exactly as you type it, spaces and line breaks included, with the Preformatted block.',
    'blocks/text/pullquote.md': 'Highlight a short quotation from your text in large type with the Pullquote block.',
    'blocks/text/quote.md': 'Set a quotation apart from the rest of the text, with an optional citation, using the Quote block.',
    'blocks/text/table.md': 'Add a table of rows and columns to a post or page with the Table block.',
    'blocks/text/verse.md': 'Write poetry and song lyrics with the spacing and line breaks you type, using the Poetry block.',
    'blocks/theme/comments.md': "Show a post's comments and the comment form in a template with the Comments block and its inner blocks.",
    'blocks/theme/loginout.md': 'Add a link that lets visitors log in to your site, or log out when they are logged in, with the Login/out block.',
    'blocks/theme/post-author-name.md': "Show the name of a post's author with the Author Name block, usually in a template or a Query Loop.",
    'blocks/theme/post-comments-form.md': 'Show the form visitors use to leave a comment with the Comments Form block.',
    'blocks/theme/post-content.md': 'Show the content of a post or page in a template or a Query Loop with the Content block.',
    'blocks/theme/post-date.md': 'Show the date a post was published or last updated with the Date block.',
    'blocks/theme/post-excerpt.md': "Show a post's excerpt in a template or a Query Loop with the Excerpt block.",
    'blocks/theme/post-featured-image.md': "Show a post's featured image in a template or a Query Loop with the Featured Image block.",
    'blocks/theme/post-navigation-link.md': 'Link to the previous or next post with the Previous Post and Next Post blocks.',
    'blocks/theme/post-template.md': 'Set the layout of each post in a Query Loop with the Post Template block.',
    'blocks/theme/post-terms.md': "Show a post's categories, tags or other terms with the Categories, Tags and other post terms blocks.",
    'blocks/theme/post-title.md': 'Show the title of a post or page with the Title block.',
    'blocks/theme/query-pagination.md': 'Add links to the next and previous pages of results in a Query Loop with the Pagination block.',
    'blocks/theme/query-title.md': 'Show a heading that matches the archive or search results being viewed with the Query Title block.',
    'blocks/theme/query-total.md': 'Show how many posts a Query Loop found, or which ones are on the current page, with the Query Total block.',
    'blocks/theme/query.md': 'Show a list of posts chosen by type, category, author and other filters with the Query Loop block.',
    'blocks/theme/read-more.md': 'Add a link to the full post inside a Query Loop with the Read More block.',
    'blocks/theme/site-logo.md': "Show your site's logo with the Site Logo block, and set the logo for the whole site.",
    'blocks/theme/template-part.md': 'Reuse areas such as the header and footer across templates with the Template Part block.',
    'blocks/theme/term-description.md': 'Show the description of a category, tag or other term on its archive page with the Term Description block.',
    'blocks/theme/terms-query.md': 'Show a list or grid of categories, tags or other taxonomy terms with the Terms Query block.',
    'blocks/widgets/README.md': 'Blocks that show content WordPress keeps up to date, such as archives, latest posts and comments, a search form and social icons.',
    'blocks/widgets/archives.md': 'Show links to your posts grouped by month or year with the Archives block.',
    'blocks/widgets/calendar.md': 'Show a monthly calendar that links to the days you published posts with the Calendar block.',
    'blocks/widgets/categories.md': 'Show a list or dropdown of your post categories with the Categories List block.',
    'blocks/widgets/html.md': 'Add your own HTML code to a post, page or template with the Custom HTML block.',
    'blocks/widgets/latest-comments.md': 'Show the most recent comments on your site with the Latest Comments block.',
    'blocks/widgets/latest-posts.md': 'Show a list of your most recent posts with the Latest Posts block.',
    'blocks/widgets/page-list.md': "Show a list of your site's published pages with the Page List block.",
    'blocks/widgets/rss.md': 'Show the latest items from any RSS feed with the RSS block.',
    'blocks/widgets/search.md': 'Add a search form to a post, page or template with the Search block.',
    'blocks/widgets/shortcode.md': 'Add a shortcode from a plugin or theme to a post or page with the Shortcode block.',
    'blocks/widgets/social-links.md': 'Add icons that link to your social media profiles with the Social Icons block.',
    'blocks/widgets/tag-cloud.md': 'Show your most used tags or categories as a cloud of links with the Tag Cloud block.',
    'classic/classic-editor/audio-video-shortcodes.md': 'Embed audio and video files in Classic Editor content with the audio and video shortcodes.',
    'classic/classic-editor/write-code-in-posts.md': 'Show code in a post written with the Classic Editor without WordPress changing or running it.',
    'classic/classic-editor/write-posts-classic.md': 'Write, format and publish a post with the Classic Editor.',
    'classic/widgets-menus-customizer/README.md': 'Customize a classic theme with the Customizer, widgets and menus.',
    'classic/widgets-menus-customizer/block-widgets-editor.md': 'Add blocks to the widget areas of a classic theme with the block-based widgets editor.',
    'classic/widgets-menus-customizer/customizer.md': "Preview and change a classic theme's settings, such as the site identity, colors, menus and widgets, in the Customizer.",
    'classic/widgets-menus-customizer/menus-screen.md': 'Create and manage navigation menus for a classic theme on the Appearance > Menus screen.',
    'classic/widgets-menus-customizer/widgets-screen.md': "Add, arrange and remove widgets in a classic theme's widget areas on the Appearance > Widgets screen.",
    'design/patterns/README.md': 'Patterns are ready-made groups of blocks that you insert and then change to fit your content.',
    'design/patterns/pattern-directory.md': 'Find patterns in the WordPress.org Pattern Directory and use them on your site.',
    'design/patterns/submit-a-pattern.md': 'Share a pattern you made with every WordPress site by submitting it to the Pattern Directory.',
    'design/site-editor/README.md': 'Design your whole site with blocks in the Site Editor, from the header and footer to every template.',
    'design/site-editor/command-palette.md': 'Jump to any part of your site or run an action from the keyboard with the Command Palette.',
    'design/site-editor/fonts.md': 'Install, upload and manage the fonts on your site with the Font Library.',
    'design/site-editor/navigation.md': "Create and edit your site's navigation menus in the Site Editor.",
    'design/site-editor/site-icon.md': 'Set the small icon that browsers show in tabs and bookmarks for your site.',
    'design/site-editor/styles.md': 'Change the colors, fonts and spacing of your whole site at once with Styles in the Site Editor.',
    'design/site-editor/templates.md': 'Templates set the layout of each kind of page on your site; template parts are the pieces they share, such as the header.',
    'design/themes/README.md': 'Find, install, preview and switch themes, the designs that control how your site looks.',
    'design/themes/default-themes/README.md': 'Every default theme WordPress has shipped, from Twenty Ten to Twenty Twenty-Five: what each one offers and how to customize it.',
    'design/themes/default-themes/twenty-eleven.md': 'Twenty Eleven, the default theme introduced in WordPress 3.2: what it offers and how to customize it.',
    'design/themes/default-themes/twenty-fifteen.md': 'Twenty Fifteen, the default theme introduced in WordPress 4.1: what it offers and how to customize it.',
    'design/themes/default-themes/twenty-fourteen.md': 'Twenty Fourteen, the default theme introduced in WordPress 3.8: what it offers and how to customize it.',
    'design/themes/default-themes/twenty-nineteen.md': 'Twenty Nineteen, the default theme introduced in WordPress 5.0: what it offers and how to customize it.',
    'design/themes/default-themes/twenty-seventeen.md': 'Twenty Seventeen, the default theme introduced in WordPress 4.7: what it offers and how to customize it.',
    'design/themes/default-themes/twenty-sixteen.md': 'Twenty Sixteen, the default theme introduced in WordPress 4.4: what it offers and how to customize it.',
    'design/themes/default-themes/twenty-ten.md': 'Twenty Ten, the default theme introduced in WordPress 3.0: what it offers and how to customize it.',
    'design/themes/default-themes/twenty-thirteen.md': 'Twenty Thirteen, the default theme introduced in WordPress 3.6: what it offers and how to customize it.',
    'design/themes/default-themes/twenty-twelve.md': 'Twenty Twelve, the default theme introduced in WordPress 3.5: what it offers and how to customize it.',
    'design/themes/default-themes/twenty-twenty-five.md': 'Twenty Twenty-Five, the default theme introduced in WordPress 6.7: what it offers and how to customize it.',
    'design/themes/default-themes/twenty-twenty-four.md': 'Twenty Twenty-Four, the default theme introduced in WordPress 6.4: what it offers and how to customize it.',
    'design/themes/default-themes/twenty-twenty-one.md': 'Twenty Twenty-One, the default theme introduced in WordPress 5.6: what it offers and how to customize it.',
    'design/themes/default-themes/twenty-twenty-three.md': 'Twenty Twenty-Three, the default theme introduced in WordPress 6.1: what it offers and how to customize it.',
    'design/themes/default-themes/twenty-twenty-two.md': 'Twenty Twenty-Two, the default theme introduced in WordPress 5.9: what it offers and how to customize it.',
    'design/themes/default-themes/twenty-twenty.md': 'Twenty Twenty, the default theme introduced in WordPress 5.3: what it offers and how to customize it.',
    'design/themes/themes-screen.md': 'Install, preview, activate, update and delete themes on the Appearance > Themes screen.',
    'get-started/glossary.md': 'Definitions of the terms used in WordPress and in this documentation.',
    'get-started/where-to-find-help.md': 'Where to look when you are stuck: this documentation, the support forums, and how to search for an answer.',
    'get-started/wordpress-org-and-wordpress-com.md': 'The difference between WordPress.org, the free software you can install anywhere, and WordPress.com, a hosting service built on it.',
    'manage/dashboard/README.md': 'A tour of the WordPress admin: the toolbar, the menu, and the screens you reach from it.',
    'manage/dashboard/dashboard-screen.md': 'The Dashboard screen you see after you log in: its widgets and how to arrange them.',
    'manage/dashboard/pages-screen.md': 'List, search, filter and edit your pages, one at a time or in bulk, on the Pages screen.',
    'manage/dashboard/posts-screen.md': 'List, search, filter and edit your posts, one at a time or in bulk, on the Posts screen.',
    'manage/plugins.md': 'Find, install, update, deactivate and delete plugins, which add features to your site.',
    'manage/privacy.md': "The privacy tools in WordPress: the privacy policy page, and exporting or erasing a person's personal data.",
    'manage/security/password-best-practices.md': 'How to choose a strong password for your WordPress account and keep it safe.',
    'manage/security/site-was-hacked.md': 'What to do, step by step, when your WordPress site has been hacked.',
    'manage/settings/connectors.md': 'Connect your site to external services, such as AI providers, on the Settings > Connectors screen.',
    'manage/settings/date-and-time-format.md': 'The format characters WordPress uses to show dates and times, and how to write your own format.',
    'manage/settings/discussion.md': 'Choose who can comment, how comments are moderated and which avatars appear on the Settings > Discussion screen.',
    'manage/settings/general.md': "Set your site's title, tagline, address, admin email, language, time zone and date format on the Settings > General screen.",
    'manage/settings/media.md': 'Set the sizes WordPress creates for uploaded images and how uploads are organized on the Settings > Media screen.',
    'manage/settings/permalinks.md': 'Choose the structure of the URLs of your posts and archives on the Settings > Permalinks screen.',
    'manage/settings/reading.md': 'Choose what your front page shows and how many posts appear on the Settings > Reading screen.',
    'manage/settings/writing.md': 'Set the default post category and format, and other writing options, on the Settings > Writing screen.',
    'manage/troubleshooting/README.md': "Check your site's health on the Site Health screen, and find what to do when something goes wrong.",
    'manage/troubleshooting/changes-not-showing.md': 'Why a change you made may not show on your site yet, and how to clear the caches that cause it.',
    'manage/troubleshooting/faq-troubleshooting.md': 'Answers to common WordPress problems, from login trouble to errors after an update.',
    'manage/troubleshooting/recovery-mode.md': 'How recovery mode lets you back into your site after a fatal error, without FTP.',
    'manage/updates/README.md': 'Update WordPress, plugins, themes and translations, and what to do when an update fails.',
    'manage/updates/auto-updates.md': 'Turn automatic updates on or off for WordPress, plugins and themes.',
    'manage/updates/site-maintenance.md': 'A checklist of regular tasks that keep a WordPress site healthy: backups, updates, spam and broken links.',
    'manage/updates/update-php.md': 'Why the PHP version your site runs on matters, and how to update it.',
    'manage/users/README.md': 'Who can do what on your site: user roles, adding users and managing profiles.',
    'manage/users/add-a-user.md': 'Add a new user to your site and choose their role.',
    'manage/users/gravatars.md': 'How WordPress uses Gravatar to show profile pictures, and how to set up your own.',
    'manage/users/roles-and-capabilities.md': 'The roles a WordPress user can have, from Subscriber to Administrator, and what each one can do.',
    'manage/users/users-screen.md': 'List, search, edit and delete users, and change their roles, on the Users screen.',
    'manage/users/your-profile.md': 'Change your name, email, password, color scheme and other personal options on your profile screen.',
    'write/block-settings/advanced.md': 'Add an HTML anchor or extra CSS classes to a block in its Advanced settings.',
    'write/block-settings/border.md': 'Add a border, rounded corners or a shadow to a block.',
    'write/block-settings/dimensions.md': 'Set the padding, margin, spacing and size of a block with the dimensions settings.',
    'write/block-settings/position.md': 'Make a block stay at the top of the screen as visitors scroll with the position settings.',
    'write/block-settings/typography.md': 'Change the font, size, line height, letter case and other text settings of a block.',
    'write/blocks/add-a-block.md': 'The ways to add a block to a post or page: the block inserter, the slash command and the inserter between blocks.',
    'write/blocks/block-directory.md': 'Find and install blocks made by the community from inside the editor with the Block Directory.',
    'write/blocks/block-error.md': "What a block error message means and how to recover the block's content.",
    'write/blocks/move-blocks.md': 'Move blocks within a post or page with the move arrows, drag and drop, or List View.',
    'write/blocks/page-jumps.md': 'Link to a heading or block further down a page with an HTML anchor, so readers jump straight to it.',
    'write/comments/comment-spam.md': 'How to stop spam comments, and how to clean up the ones that get through.',
    'write/comments/comments-screen.md': 'Approve, reply to, edit, mark as spam and delete comments on the Comments screen.',
    'write/comments/trackbacks-and-pingbacks.md': 'What trackbacks and pingbacks are, how they differ, and how to turn them off.',
    'write/create-a-page.md': 'Create a page for content that sits outside your blog, such as an About or Contact page.',
    'write/editor/README.md': 'A tour of the block editor: the top toolbar, the content area, the settings sidebar and the document tools.',
    'write/editor/distraction-free-mode.md': "Hide the editor's toolbars and panels so you can focus on writing with Distraction free mode.",
    'write/editor/keyboard-shortcuts.md': 'Keyboard shortcuts for the block editor, the Classic Editor and the Comments screen, on Windows and Mac.',
    'write/editor/preferences.md': "Turn editor features and panels on or off in the editor's Preferences.",
    'write/editor/preview.md': 'Preview a post, page or template at desktop, tablet and mobile widths before you publish it.',
    'write/editor/settings-sidebar.md': 'The post and page settings in the editor sidebar, from status and publish date to categories, tags and featured image.',
    'write/formatting/character-entities.md': 'Type special characters, such as the copyright sign, accented letters and arrows, with HTML character entities.',
    'write/formatting/emoji.md': 'How emoji work in WordPress and how to add them to your content on mobile and desktop.',
    'write/formatting/post-content-processing.md': 'The changes WordPress makes to post content before showing it, such as curly quotes and paragraph tags, and how to prevent them.',
    'write/formatting/smilies.md': 'How WordPress turns text smileys such as :-) into images, and how to turn that off.',
    'write/media/README.md': 'Upload, find and manage the images, video, audio and documents on your site in the Media Library.',
    'write/media/add-media.md': 'Upload images, video, audio and other files to the Media Library.',
    'write/media/edit-media.md': "Edit a file's title, caption, alt text and description, and crop or rotate images, in the Media Library.",
    'write/media/image-sizes.md': 'How WordPress resizes the images you upload, and how to keep images sharp and quick to load.',
    'write/organize/README.md': 'How WordPress groups content so visitors can find it: categories and tags, post types, custom fields, a static front page and a search page.',
    'write/organize/categories.md': 'Create, edit and organize post categories on the Posts > Categories screen.',
    'write/organize/custom-fields.md': 'Add extra information, called metadata, to a post with custom fields.',
    'write/organize/post-types.md': 'Posts, pages, attachments and the other kinds of content WordPress stores, and how custom post types add more.',
    'write/organize/search-page.md': 'Create a page that helps visitors search your site.',
    'write/organize/static-front-page.md': "Show a page instead of your latest posts on your site's front page, and put your posts on a page of their own.",
    'write/organize/tags.md': 'Create, edit and manage post tags on the Posts > Tags screen.',
    'write/organize/taxonomies.md': 'What taxonomies are, the categories and tags WordPress includes, and how custom taxonomies add more.',
    'write/publish/content-visibility.md': 'Make a post or page public, private or password protected with the Visibility setting.',
    'write/publish/excerpts.md': 'Write a short summary of a post, called an excerpt, and control where WordPress shows it.',
    'write/publish/password-protected.md': 'Protect a post or page with a password so that only people who know it can read it.',
    'write/publish/post-status.md': 'The statuses a post can have, such as draft, pending, scheduled, private and published, and what each one means.',
    'write/publish/revisions.md': 'See every saved version of a post, compare two versions, and restore an earlier one.',
    'write/publish/sticky-posts.md': 'Keep a post at the top of your blog page by making it sticky.',
    'write/seo.md': 'What WordPress does for search engines out of the box, and the settings and habits that help people find your site.',
})

# New bodies for group landings whose hub page was a stub (replace everything after the H1).
INTROS = {
    "blocks/text/README.md": (
        "Text blocks hold the words on a page: paragraphs and headings, lists and quotes, tables, code and "
        "poetry. Most posts are built mainly from these blocks.\n\n"
        "Start with the [Paragraph](paragraph.md) and [Heading](heading.md) blocks; the others work the same way, "
        "with a few settings of their own.\n"),
    "blocks/media/README.md": (
        "Media blocks put images, audio, video and files on a page, or combine media with text, as the "
        "[Cover](cover.md) and [Media & Text](media-text.md) blocks do.\n\n"
        "Files you add through these blocks go into the Media Library, where you can reuse and edit them. See "
        "[Media](../../write/media/README.md) for how the library works.\n"),
    "blocks/design/README.md": (
        "Design blocks arrange other blocks. Use them to lay out a page in columns, rows, stacks and grids, to "
        "add buttons, separators and space, and to hide content in accordions and tabs.\n\n"
        "The [Group](group/README.md) block is the one to learn first: most layouts are groups of blocks with a "
        "layout and a few design settings applied.\n"),
    "blocks/widgets/README.md": (
        "Widget blocks show content that WordPress keeps up to date for you: your latest posts and comments, "
        "archives, a calendar, a tag cloud, a search form and links to your social profiles.\n\n"
        "You can use them anywhere in a post, a page or a template, and in the widget areas of a classic theme.\n"),
    "blocks/theme/README.md": (
        "Theme blocks build the templates of a block theme in the Site Editor. They display parts of your site "
        "that change from page to page, such as the site title, the navigation menu, a post's title, date and "
        "content, or a list of posts from a query.\n\n"
        "You mostly meet them while editing templates; see [Templates and template parts]"
        "(../../design/site-editor/templates.md) for how templates fit together.\n"),
    "write/formatting/README.md": (
        "WordPress changes some of the text you type before it shows it to visitors: it turns quotes into curly "
        "quotes, smilies into images, and some characters into HTML entities. These pages explain what it "
        "changes and how to type characters that have a special meaning.\n\n"
        "You rarely need them in the block editor; they matter most when something on the page looks different "
        "from what you typed.\n"),
    "write/organize/README.md": (
        "WordPress gives you several ways to organize content so that visitors can find it: categories and tags "
        "group posts, post types separate posts from pages and other kinds of content, and custom fields add "
        "extra details to a post.\n\n"
        "This group also covers two pages most sites need: a static front page and a search page. Start with "
        "[Categories](categories.md) if you write posts.\n"),
    "manage/settings/README.md": (
        "The **Settings** menu in the dashboard holds the options that apply to the whole site: its title and "
        "language, how posts are written and shown, comments, image sizes and the structure of your URLs.\n\n"
        "Each page here describes one settings screen, field by field. Only administrators can change settings.\n"),
    "manage/users/README.md": (
        "A WordPress site can have many users, and each user has a role that decides what they can do, from "
        "reading private posts to changing every setting. Administrators add users, assign roles and remove "
        "users from the **Users** screen.\n\n"
        "Start with [Roles and capabilities](roles-and-capabilities.md) to choose the right role, then "
        "[Add a user](add-a-user.md).\n"),
    "write/block-settings/README.md": (
        "When you select a block, the settings sidebar shows the design tools that block supports: color, "
        "typography, dimensions, border and shadow, background, layout, position and filters. Most blocks share "
        "the same tools, so each one is described once, here, instead of on every block page.\n\n"
        "Which tools a block offers depends on the block and on your theme. If a setting described here is "
        "missing, the theme may have turned it off.\n"),
}

TEXT_INTRO_BLOCKS = (
    "Blocks are the pieces you build every post, page and template from. Each paragraph, image, heading or "
    "list is a block, and each block has its own toolbar and settings. WordPress ships with about a hundred "
    "of them, and plugins can add more.\n\n"
    "This reference has one page per core block, grouped the way the block inserter groups them: text, media, "
    "design, widgets, theme and embeds. To learn the tools every block shares, such as adding, moving and "
    "styling blocks, start with [Working with blocks](../write/blocks/README.md).\n")

MINOR = {"a", "an", "the", "and", "or", "of", "to", "in", "on", "for", "with", "at", "by", "from", "as", "vs",
         "via", "is", "are", "your", "you", "it", "its", "into", "be", "not", "do", "how", "what"}
PROPER = {
    "WordPress", "Gutenberg", "Gravatar", "Gravatars", "Google", "Bing", "Yahoo", "Linux", "Windows", "Mac",
    "Apache", "Nginx", "Customizer", "Openverse", "Playground", "Studio", "Akismet", "Jetpack", "FTP",
    "Twenty", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Nineteen",
    "Twenty-One", "Twenty-Two", "Twenty-Three", "Twenty-Four", "Twenty-Five", "Arch", "Ubuntu", "Debian",
    "Fedora", "Microsoft", "Word", "Excel", "YouTube", "Vimeo", "Spotify", "Instagram", "Facebook", "Twitter",
    "English", "Unicode", "Markdown", "I", "OS", "X", "Quicktags", "QuickTags", "Gmail", "Chrome",
    "Firefox", "Safari", "Edge", "Ajax", "JavaScript", "Dashicons", "Abilities", "Hello", "Dolly",
}
PHRASES = [
    "Site Editor", "Block Editor Handbook", "Block Directory", "Pattern Directory", "Plugin Directory",
    "Theme Directory", "Font Library", "Media Library", "List View", "Command Palette", "Classic Editor",
    "Query Loop", "Site Health", "Global Styles", "Code Reference", "Media & Text", "Social Icons",
    "Quick Edit", "Bulk Edit", "Screen Options", "Help Tab", "Application Passwords", "Abilities API",
    "REST API", "Block Inserter", "Twenty Twenty", "Hello Dolly", "Learn WordPress",
    "Support Forums", "Theme Handbook", "Plugin Handbook", "Common APIs Handbook",
]


def lower_word(w):
    """Lowercase one word unless it is a name, an acronym, CamelCase or has digits."""
    if not w or w in PROPER or re.sub(r"[’'](s)?$", "", w) in PROPER or re.search(r"\d", w) \
            or re.search(r"[a-z][A-Z]", w) or (len(w) > 1 and w.rstrip("s").isupper()) or w[0].islower():
        return w
    return w[0].lower() + w[1:]


def sentence_case(text):
    """Title Case heading to sentence case, keeping product names, block names and acronyms."""
    # Protect code, links (keep only their text to judge), bold, phrases.
    words = re.findall(r"[A-Za-z][\w'’.-]*", re.sub(r"`[^`]*`|\]\([^)]*\)", " ", text))
    if len(words) < 2:
        return text
    rest = [w for w in words[1:] if w.lower() not in MINOR]
    caps = [w for w in rest if w[0].isupper()]
    if not rest or not caps or len(caps) < 0.6 * len(rest):
        return text
    keep = set()
    for ph in PHRASES:
        for m in re.finditer(re.escape(ph), text):
            keep.update(range(m.start(), m.end()))
    # Words that name a block: Capitalized words right before "block" or "blocks".
    for m in re.finditer(r"([A-Z][\w&’'-]*\s+(?:(?:to|of|and|&|[A-Z][\w&’'-]*)\s+)*)(?=[Bb]locks?\b)", text):
        if not re.match(r"(Most|Other|Embed|Theme|Hidden|Locked|Parent|Synced)\b", m.group(1)):
            keep.update(range(m.start(), m.end()))
    for m in re.finditer(r"`[^`]*`|\]\([^)]*\)|\*\*[^*]+\*\*|“[^”]*”|\"[^\"]*\"", text):
        keep.update(range(m.start(), m.end()))
    out, first = [], True
    pos = 0
    for m in re.finditer(r"[A-Za-z][\w'’.-]*", text):
        out.append(text[pos:m.start()])
        w = m.group(0)
        before = text[:m.start()].rstrip()
        after_break = before.endswith((":", "?", "!", "→", "→︎")) or \
            (before.endswith(".") and not before.endswith("..") and not before.lower().endswith("vs."))
        if first or after_break or m.start() in keep:
            out.append(w)
        else:
            out.append("-".join(lower_word(p) for p in w.split("-")))
        if re.match(r"[A-Za-z]", w):
            first = False
        pos = m.end()
    out.append(text[pos:])
    s = "".join(out)
    # "Step 2 – Click..." style: keep the capital after a dash used as a separator.
    s = re.sub(r"( [–-] )([a-z])", lambda mm: mm.group(1) + mm.group(2).upper(), s) if re.match(r"(Step|Option) ", s) else s
    return s


def target_of(src):
    """('page', dst) | ('retire', dst) | ('other', dst) | (None, None)."""
    v = EXPLICIT.get(src)
    if isinstance(v, tuple):
        return "retire", v[1]
    if v:
        return ("other" if v in OTHER else "page"), v
    m = re.match(r"blocks/all-blocks/blocks-category-([a-z]+)/(.*)$", src)
    if m:
        g, rest = m.groups()
        if rest == "README.md":
            return "page", f"blocks/{g}/README.md"
        parts = rest.split("/")
        name = parts[0][len("block-"):].removesuffix(".md")
        if len(parts) == 1:
            return "page", f"blocks/{g}/{name}.md"
        folder = os.path.join(SRC, "blocks/all-blocks", f"blocks-category-{g}", parts[0])
        if not os.path.isdir(folder):
            return None, None
        has_children = any(f.endswith(".md") and f != "README.md" for f in os.listdir(folder))
        if parts[1] == "README.md":
            return "page", (f"blocks/{g}/{name}/README.md" if has_children else f"blocks/{g}/{name}.md")
        child = parts[1].removesuffix(".md").removeprefix(f"block-{name}-").removeprefix("block-")
        return "page", f"blocks/{g}/{name}/{child}.md"
    for pre, new, fn in RULES:
        if src.startswith(pre):
            rest = src[len(pre):]
            if fn:
                d, b = os.path.split(rest)
                rest = os.path.join(d, fn(b)) if d else fn(b)
            dst = new + rest
            return ("other" if dst in OTHER else "page"), dst
    return None, None


# ---------------------------------------------------------------------------------------------- front matter


def parse_front_matter(text):
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    fm, key = {}, None
    for line in m.group(1).split("\n"):
        if not line.strip():
            continue
        li = re.match(r"^\s+-\s+(.*)$", line)
        if li and key:
            fm.setdefault(key, []).append(unquote(li.group(1)))
            continue
        kv = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if kv:
            key, val = kv.group(1), kv.group(2).strip()
            if val.startswith("[") and val.endswith("]"):
                fm[key] = [unquote(x.strip()) for x in val[1:-1].split(",") if x.strip()]
            elif val:
                fm[key] = unquote(val)
            else:
                fm[key] = []
    return fm, text[m.end():]


def unquote(v):
    if len(v) >= 2 and v[0] == v[-1] == '"':
        return v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    if len(v) >= 2 and v[0] == v[-1] == "'":
        return v[1:-1].replace("''", "'")
    return v


def yaml_str(v):
    if re.search(r"[:#\[\]{},&*!|>'\"%@`]|^[-?\s]|\s$", v) or v.lower() in ("yes", "no", "true", "false", "null", "~") \
            or re.fullmatch(r"[\d.]+", v):
        return '"' + v.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return v


def render_front_matter(fm):
    out = ["---"]
    for k in ("title", "description", "type", "order", "slug", "status", "redirect_from"):
        if k not in fm or fm[k] in (None, "", []):
            continue
        v = fm[k]
        if isinstance(v, list):
            out.append(f"{k}:")
            out += [f"  - {yaml_str(x)}" for x in v]
        elif isinstance(v, int):
            out.append(f"{k}: {v}")
        else:
            out.append(f"{k}: {yaml_str(v)}")
    out.append("---")
    return "\n".join(out) + "\n\n"


# ---------------------------------------------------------------------------------------------- body


FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
LINK = re.compile(r"(!?)\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(\s*(<[^>]*>|[^()\s]*(?:\([^()\s]*\)[^()\s]*)*)((?:\s+\"[^\"]*\")?)\s*\)")


def split_fences(body):
    """[(is_code, text_lines)] chunks."""
    chunks, cur, code, fence = [], [], False, None
    for line in body.split("\n"):
        m = FENCE.match(line)
        if not code and m:
            if cur:
                chunks.append((False, cur))
            cur, code, fence = [line], True, m.group(1)
            continue
        if code:
            cur.append(line)
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) and not line.strip()[len(m.group(1)):].strip():
                chunks.append((True, cur))
                cur, code = [], False
            continue
        cur.append(line)
    if cur:
        chunks.append((code, cur))
    return chunks


def external_for(rel):
    if rel in EXTERNAL:
        return EXTERNAL[rel]
    top = rel.split("/")[0]
    if top in ("themes", "plugins"):
        p = rel.removesuffix(".md").removesuffix("README").rstrip("/")
        return f"{DEV}/{p}/"
    return EXTERNAL_ROOTS.get(top, f"{DEV}/")


def rewrite_links(line, src, dst, problems):
    def repl(m):
        bang, label, url, title = m.group(1), m.group(2), m.group(3), m.group(4)
        u = url.strip("<>")
        if not u or u.startswith("#") or re.match(r"^[a-z][a-z0-9+.-]*:", u):
            return m.group(0)
        path, _, frag = u.partition("#")
        if bang:
            return m.group(0)
        if path.startswith("/"):
            problems.append(f"{src}: root-relative link {u}")
            return m.group(0)
        rel = os.path.normpath(os.path.join(os.path.dirname(src), path))
        if os.path.isdir(os.path.join(SRC, rel)):
            rel = os.path.join(rel, "README.md")
        kind, new = target_of(rel) if rel.split("/")[0] in SECTIONS else (None, None)
        if new is None:
            if rel.split("/")[0] in SECTIONS:
                problems.append(f"{src}: link to {u} has no target here")
                return m.group(0)
            ext = external_for(rel)
            return f"{bang}[{label}]({ext}{title})"
        if new == dst and frag:
            return f"{bang}[{label}](#{frag}{title})"
        newrel = os.path.relpath(new, os.path.dirname(dst) or ".")
        return f"{bang}[{label}]({newrel}{('#' + frag) if frag else ''}{title})"
    return LINK.sub(repl, line)


CALLOUTS = {"info": "NOTE", "tip": "TIP", "alert": "WARNING", "warning": "CAUTION"}


def convert_callouts(text):
    def sc(m):
        kind = CALLOUTS[m.group(1).lower()]
        inner = m.group(2).strip()
        return "> [!" + kind + "]\n" + "\n".join("> " + x if x else ">" for x in inner.split("\n"))
    text = re.sub(r"\[(info|tip|alert|warning)\](.*?)\[/\1\]", sc, text, flags=re.S | re.I)
    text = re.sub(r'<div class="callout[^"]*">(.*?)</div>',
                  lambda m: "> [!NOTE]\n" + "\n".join("> " + x for x in m.group(1).strip().split("\n")), text, flags=re.S)
    return text


def drop_changelog(lines):
    """Remove the documentation edit log: a heading or paragraph 'Changelog' and its list of Updated entries."""
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        h = re.match(r"^(#{1,6})\s*\**changelog\**:?\s*$", line, re.I) or re.match(r"^\**changelog\**:?\s*$", line, re.I)
        if h:
            lvl = len(h.group(1)) if h.re.pattern.startswith("^(#") else 7
            j = i + 1
            while j < len(lines):
                nh = re.match(r"^(#{1,6})\s", lines[j])
                if nh and len(nh.group(1)) <= min(lvl, 6):
                    break
                if lvl == 7 and nh:
                    break
                j += 1
            block = "\n".join(lines[i + 1:j])
            if re.search(r"(Updated|Update|Created)\b|^\s*-\s", block) or not block.strip():
                while out and not out[-1].strip():
                    out.pop()
                out.append("")
                i = j
                continue
        out.append(line)
        i += 1
    while out and not out[-1].strip():
        out.pop()
    return out


def sentence_heading(rest):
    s = rest.strip()
    s = re.sub(r"\s*#+\s*$", "", s)
    return " " + sentence_case(s)


def fill_alt(lines):
    """![](url) followed by an italic caption line: use the caption as alt text."""
    out = list(lines)
    for i, line in enumerate(out):
        m = re.match(r"^(\s*)!\[\]\((\S+)\)\s*$", line)
        if not m:
            continue
        j = i + 1
        while j < len(out) and not out[j].strip():
            j += 1
        if j < len(out):
            c = re.match(r"^\s*[*_]+([^*_].*?)[*_]+\s*$", out[j])
            if c:
                alt = re.sub(r"[\[\]]", "", c.group(1)).strip().rstrip(".")
                out[i] = f"{m.group(1)}![{alt}.]({m.group(2)})"
    return out


def plain(md):
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", md)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"[*_`]", "", t)
    return re.sub(r"\s+", " ", t).strip()


def derive_description(body_lines):
    para = []
    for line in body_lines[1:]:
        s = line.strip()
        if not s:
            if para:
                break
            continue
        if s.startswith(("#", ">", "!", "|", "-", "*", "1.", "```", "<")):
            if para:
                break
            continue
        para.append(s)
    text = plain(" ".join(para))
    return first_sentence(text)


def first_sentence(text):
    text = text.replace("—", ", ").replace(" , ", ", ")
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z“\"])", text)
    s = parts[0].strip() if parts else ""
    if len(s) >= 200:
        s = s[:196].rsplit(" ", 1)[0].rstrip(",;:") + "."
    return s


def clean_description(desc, body_lines):
    if desc:
        desc = re.sub(r"\s+", " ", desc).strip()
    if not desc or desc.endswith(("...", "…")) or len(desc) >= 200 or "—" in desc:
        if desc and "—" in desc and len(desc) < 200 and not desc.endswith(("...", "…")):
            return desc.replace(" — ", ", ").replace("—", ", ")
        if desc and not desc.endswith(("...", "…")):
            return first_sentence(desc)
        return derive_description(body_lines)
    return desc


def drop_boilerplate(lines, dst):
    out = []
    for line in lines:
        if re.search(r"go back to the list of blocks", line, re.I) and len(line) < 200:
            continue
        if re.match(r"^You can also read \[the theme.s changelog\]\([^)]*\)\.?\s*$", line):
            continue
        out.append(line)
    return out


def collapse_blank(lines):
    out = []
    for line in lines:
        if not line.strip() and out and not out[-1].strip():
            continue
        out.append(line.rstrip() if not line.strip() else line)
    return out


# ---------------------------------------------------------------------------------------------- anchors


def github_slug(text, seen=None):
    t = re.sub(r"<[^>]+>", "", text)
    t = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = t.replace("`", "").strip().lower()
    t = re.sub(r"[^\w\- ]", "", t, flags=re.U)
    t = t.replace(" ", "-")
    if seen is not None:
        base, i = t, 1
        while t in seen:
            t = f"{base}-{i}"
            i += 1
        seen.add(t)
    return t


def anchors_in(path, cache):
    if path not in cache:
        seen, out = set(), set()
        if os.path.isfile(path):
            for code, chunk in split_fences(open(path, encoding="utf-8").read()):
                if code:
                    continue
                for line in chunk:
                    h = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
                    if h:
                        out.add(github_slug(h.group(1), seen))
        cache[path] = out
    return cache[path]


def norm_anchor(a):
    return re.sub(r"-+", "-", a.lower().replace("_", "-")).strip("-")


def fix_anchors(dst, problems, cache):
    """Point #fragments at headings that exist: same heading with different hyphenation, a glossary term, or
    no fragment at all (the page still opens)."""
    path = os.path.join(DOCS, dst)
    text = open(path, encoding="utf-8").read()
    glossary = os.path.join(DOCS, "get-started/glossary.md")
    out = []

    def repl(m):
        bang, label, url, title = m.group(1), m.group(2), m.group(3), m.group(4)
        if bang or "#" not in url or re.match(r"^[a-z][a-z0-9+.-]*:", url):
            return m.group(0)
        target, frag = url.split("#", 1)
        tpath = path if not target else os.path.normpath(os.path.join(os.path.dirname(path), target))
        if not tpath.endswith(".md") or not os.path.isfile(tpath):
            return m.group(0)
        names = anchors_in(tpath, cache)
        if frag in names:
            return m.group(0)
        byn = {norm_anchor(n): n for n in names}
        nf = norm_anchor(github_slug(urllib.parse.unquote(frag)))
        for cand in (nf, nf + "s", nf.removesuffix("s")):
            if cand in byn:
                return f"[{label}]({target}#{byn[cand]}{title})"
        pref = [n for n in names if n.startswith(nf + "-")]
        if len(pref) == 1:
            return f"[{label}]({target}#{pref[0]}{title})"
        g = anchors_in(glossary, cache)
        for cand in (frag, frag.rstrip("s"), frag.removeprefix("pretty-").rstrip("s")):
            if cand.lower() in g and tpath not in (glossary, path):
                rel = os.path.relpath(glossary, os.path.dirname(path))
                problems.append(f"{dst}: #{frag} pointed at {os.path.relpath(tpath, DOCS)}; now glossary#{cand.lower()}")
                return f"[{label}]({rel}#{cand.lower()}{title})"
        problems.append(f"{dst}: anchor #{frag} not in {os.path.relpath(tpath, DOCS)}; fragment dropped")
        if not target:
            return label
        return f"[{label}]({target}{title})"

    for code, chunk in split_fences(text.rstrip("\n")):
        if code:
            out += chunk
        else:
            out += [LINK.sub(repl, x) for x in chunk]
    new = "\n".join(out) + "\n"
    if new != text:
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(new)


# ---------------------------------------------------------------------------------------------- main


def port_file(src, dst, extra_redirects, problems):
    text = open(os.path.join(SRC, src), encoding="utf-8").read().replace("\r\n", "\n").lstrip("﻿")
    fm, body = parse_front_matter(text)
    lines = body.lstrip("\n").split("\n")
    if lines and lines[0].startswith("# "):
        hub_title = lines[0][2:].strip()
        lines = lines[1:]
    else:
        hub_title = fm.get("title", "")
    ptype, title, order = PAGES.get(dst, (None, None, None))
    is_block = dst.startswith("blocks/") and not dst.endswith(("blocks/README.md", "embeds.md")) and \
        not re.fullmatch(r"blocks/[a-z]+/README\.md", dst)
    is_theme = dst.startswith("design/themes/default-themes/") and not dst.endswith("README.md")
    if is_block or is_theme:
        ptype = "reference"
    if title is None:
        title = fm.get("title") or hub_title
        if not (is_block or is_theme):
            title = sentence_case(title)
    if ptype is None:
        problems.append(f"{dst}: no type in PAGES; using guide")
        ptype = "guide"

    # Body transformations, outside code fences only.
    if dst in INTROS:
        lines = [""] + INTROS[dst].rstrip("\n").split("\n")
    out_chunks = []
    for code, chunk in split_fences("\n".join(lines)):
        if code:
            out_chunks.append("\n".join(chunk))
            continue
        t = convert_callouts("\n".join(chunk))
        cl = t.split("\n")
        if dst not in INTROS:
            cl = [rewrite_links(x, src, dst, problems) for x in cl]
        cl = fill_alt(cl)
        out_chunks.append("\n".join(cl))
    lines = "\n".join(out_chunks).split("\n")
    lines = drop_changelog(lines)
    lines = drop_boilerplate(lines, dst)
    lines = fix_heading_levels_outside_code(lines)
    if dst == "blocks/README.md":
        lines = blocks_landing(lines)
    lines = collapse_blank(["# " + title, ""] + [x for x in lines])
    while len(lines) > 2 and not lines[2 - 1].strip() and not lines[2].strip():
        lines.pop(2)

    desc = DESCRIPTIONS.get(dst) or clean_description(fm.get("description"), lines)
    redirects = [r for r in (fm.get("redirect_from") or []) if r.startswith("/")]
    dropped = [r for r in (fm.get("redirect_from") or []) if not r.startswith("/")]
    for r in extra_redirects.get(dst, []):
        if r not in redirects:
            redirects.append(r)
    new_fm = {"title": title, "description": desc, "type": ptype}
    if order is not None and not is_block and not is_theme:
        new_fm["order"] = order
    if dst in SLUGS:
        new_fm["slug"] = SLUGS[dst]
    elif is_block:
        base = os.path.basename(dst).removesuffix(".md")
        if base == "README":
            base = os.path.basename(os.path.dirname(dst))
        new_fm["slug"] = f"{base}-block"
    new_fm["redirect_from"] = redirects
    content = render_front_matter(new_fm) + "\n".join(lines).rstrip("\n") + "\n"
    return content, dropped


def fix_heading_levels_outside_code(lines):
    out = []
    prev = [1]
    for code, chunk in split_fences("\n".join(lines)):
        if code:
            out += chunk
            continue
        for line in chunk:
            m = re.match(r"^(#{1,6})(\s+.*)$", line)
            if m:
                lvl = max(2, min(len(m.group(1)), prev[0] + 1))
                prev[0] = lvl
                line = "#" * lvl + sentence_heading(m.group(2))
            out.append(line)
    return out


def blocks_landing(lines):
    """all-blocks-overview: a new intro, plain group headings, and no list of hub categories."""
    i = 0
    while i < len(lines) and not lines[i].startswith("## "):
        i += 1
    rest = lines[i:]
    rest = [re.sub(r"^(##\s+)\[([^\]]+)\]\(([^)]*)\)\s*$", r"\1\2", x) for x in rest]
    return [""] + TEXT_INTRO_BLOCKS.rstrip("\n").split("\n") + [""] + rest


def main():
    global SRC
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", default=DEFAULT_SRC)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    SRC = a.src
    sources = []
    for s in SECTIONS:
        for dp, _, fs in os.walk(os.path.join(SRC, s)):
            for f in fs:
                if f.endswith(".md"):
                    sources.append(os.path.relpath(os.path.join(dp, f), SRC))
    sources.sort()
    plan, extra, other_redirects, problems = {}, {}, {}, []
    for src in sources:
        kind, dst = target_of(src)
        if kind is None:
            problems.append(f"{src}: no target in the map")
            continue
        fm, _ = parse_front_matter(open(os.path.join(SRC, src), encoding="utf-8").read())
        reds = [r for r in (fm.get("redirect_from") or []) if r.startswith("/")]
        if kind == "page":
            if dst in plan:
                problems.append(f"{src}: target {dst} already used by {plan[dst]}")
            plan[dst] = src
        elif kind == "retire":
            if dst in OTHER:
                other_redirects.setdefault(dst, []).extend(reds)
            else:
                extra.setdefault(dst, []).extend(reds)
        elif kind == "other":
            other_redirects.setdefault(dst, []).extend(reds)
    written = 0
    dropped_all = []
    for dst, src in sorted(plan.items()):
        content, dropped = port_file(src, dst, extra, problems)
        dropped_all += [(dst, d) for d in dropped]
        if not a.dry_run:
            path = os.path.join(DOCS, dst)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(content)
        written += 1
    if not a.dry_run:
        cache = {}
        for dst in sorted(plan):
            fix_anchors(dst, problems, cache)
    print(f"ported {written} pages from {len(sources)} hub files")
    if other_redirects:
        print("\nredirect_from for pages written by another author (add them there):")
        for dst, reds in sorted(other_redirects.items()):
            print(f"  {dst}:")
            for r in reds:
                print(f"    - {r}")
    if dropped_all:
        print("\nredirect_from entries dropped (not WordPress.org paths):")
        for dst, d in dropped_all:
            print(f"  {dst}: {d}")
    if problems:
        print("\nproblems:")
        for p in problems:
            print(f"  {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
