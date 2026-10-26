---
title: Updates
description: "Update WordPress, plugins, themes and translations, and what to do when an update fails."
type: guide
order: 50
redirect_from:
  - /documentation/article/dashboard-updates-screen/
  - /documentation/article/updating-wordpress/
---

# Updates

Updates bring new features, bug fixes and security fixes to WordPress, plugins, themes and translations, so keeping a site up to date is the most important thing you can do for its security. This page explains how to update WordPress from the dashboard and what to do if an update fails; the pages in this group cover automatic updates, regular maintenance and updating PHP.

> [!WARNING]
> The upgrade process will affect all files and folders included in the main WordPress installation. This includes all the core files used to run WordPress. If you have made any modifications to those files, your changes will be lost.

You should always update WordPress to the [latest version](https://wordpress.org/download/). When a new version of WordPress is available you will receive an update message in your WordPress Admin Screens. To update WordPress, click the link in this message.

There are two methods for updating – the easiest is the one-click update, which will work for most people. If it doesn’t work, or you just prefer to be more hands-on, you can follow the manual update process.

If you are updating across multiple versions, follow the procedure at [Upgrading WordPress – Extended Instructions](https://github.com/WordPress/Advanced-administration-handbook/blob/main/upgrade/upgrading.md)

## Back up WordPress

Before you get started, it’s a good idea to back up your website. This means if there are any issues you can restore your website. Complete instructions to make a backup can be found in the [WordPress Backup](https://developer.wordpress.org/advanced-administration/security/backup/).

## Automatic background updates

For [WordPress 3.7](https://wordpress.org/documentation/wordpress-version/version-3-7/)+, you don’t have to lift a finger to apply minor and security updates. Most sites are now able to automatically apply these updates in the background. If your site is capable of one-click updates without entering FTP credentials, then your site should be able to update from 3.7 to 3.7.1, 3.7.2, etc. (You’ll still need to click “Update Now” for major feature releases.)

## One-click update

WordPress lets you update with the click of a button.  You can launch the update by clicking the link in the new version banner (if it’s there) or by going to the Dashboard > Updates screen. Once you are on the “Update WordPress” page, click the button “Update Now” to start the process off. You shouldn’t need to do anything else and, once it’s finished, you will be up-to-date.

One-click updates work on most servers. If you have any problems, it is probably related to permissions issues on the filesystem.

### File ownership

WordPress determines what method it will use to connect to the filesystem of your server based on the file ownership of your WordPress files. If the files are owned by the owner of the current process (i.e., the user under which the web server is running), *and* new files created by WordPress will also be owned by that user, WordPress will directly modify the files all by itself, without asking you for credentials.

WordPress won’t attempt to create the new files directly if they won’t have the correct ownership. Instead, you will be shown a dialog box asking for connection credentials. It is typical for the files to be owned by the FTP account that originally uploaded them. To perform the update, you just need to fill in the connection credentials for that FTP account.

Whether your files are owned by the web server user, or not, will depend on how you installed WordPress and how your server is configured. On some shared hosting platforms, it is a security risk for the files to be owned by the web server user and not a FTP user. See the tutorial on [Changing File Permissions](https://github.com/WordPress/Advanced-administration-handbook/blob/main/server/file-permissions.md)for more information, including how to configure file permissions so that multiple FTP users are able to edit the files.

### Failed updates

If you see a “failed update” nag message, delete the file **.maintenance** from your WordPress directory using FTP. This will remove the “failed update” nag message.

If the one-click upgrade doesn’t work for you, don’t panic! Just try a manual update.

## Manual update

These are the short instructions, if you want more check out the [extended upgrade](https://github.com/WordPress/Advanced-administration-handbook/blob/main/upgrade/upgrading.md) instructions. If you experience problems with the Three Step Update, you may want to review the [more detailed upgrade instructions](https://github.com/WordPress/Advanced-administration-handbook/blob/main/upgrade/upgrading.md).

For these instructions, it is assumed that your blog’s URL is `http://example.com/wordpress/`.

### Step 1: Replace WordPress files

1.  Get the [latest WordPress](https://wordpress.org/download/) zip (or tar.gz) file.
2.  Unpack the zip file that you downloaded.
3.  Deactivate plugins.
4.  Delete the old `wp-includes` and `wp-admin` directories on your web host (through your [FTP](https://github.com/WordPress/Advanced-administration-handbook/blob/main/upgrade/ftp.md)or shell access).
5.  Using [FTP](https://github.com/WordPress/Advanced-administration-handbook/blob/main/upgrade/ftp.md)or your shell access, upload the new `wp-includes` and `wp-admin` directories to your web host, in place of the previously deleted directories.
6.  Upload the individual files from the new `wp-content` folder to your existing `wp-content` folder, overwriting existing files. Do NOT delete your existing `wp-content` folder. Do NOT delete any files or folders in your existing `wp-content` directory (except for the one being overwritten by new files).
7.  Upload all new loose files from the root directory of the new version to your existing WordPress root directory.

NOTE – you should replace all the old WordPress files with the new ones in the `wp-includes` and `wp-admin` directories and sub-directories, and in the root directory (such as `index.php`, `wp-login.php` and so on). Don’t worry – your `wp-config.php` will be safe.

Be careful when you come to copying the `wp-content` directory. You should make sure that you only copy the files from inside this directory, rather than replacing your entire `wp-content` directory. This is where your themes and plugins live, so you will want to keep them. If you have customized the default or classic themes without renaming them, make sure not to overwrite those files, otherwise you will lose your changes. (Though you might want to compare them for new features or fixes..)

Lastly you should take a look at the `wp-config-sample.php` file, to see if any new settings have been introduced that you might want to add to your own `wp-config.php`.

### Step 1.5: Remove .maintenance file

If you’re upgrading manually after a failed auto-upgrade, delete the file .maintenance from your WordPress directory using FTP. This will remove the “failed update” nag message.

### Step 2: Update your installation

Visit your main WordPress admin page at /wp-admin. You may be asked to login again. If a database upgrade is necessary at this point, WordPress will detect it and give you a link to a URL like `http://example.com/wordpress/wp-admin/upgrade.php`. Follow that link and follow the instructions. This will update your database to be compatible with the latest code. You should do this as soon as possible after step 1.

Don’t forget to reactivate plugins!

### Step 3: Do something nice for yourself

If you have caching enabled, clear the cache at this point so the changes will go live immediately. Otherwise, visitors to your site (including you) will continue to see the old version (until the cache updates).

Your WordPress installation is successfully updated. That’s as simple as we can make it without [Updating WordPress Using Subversion](https://codex.wordpress.org/Installing/Updating_WordPress_with_Subversion).

Consider rewarding yourself with a blog post about the update, reading that book or article you’ve been putting off, or simply sitting back for a few moments and letting the world pass you by.

## Final steps

Your update is now complete, so you can go in and enable your Plugins again.

If you have issues with logging in, try clearing cookies in your browser.

## Troubleshooting

If anything has gone wrong, then the first thing to do is go through all the steps in our [extended upgrade instructions](https://github.com/WordPress/Advanced-administration-handbook/blob/main/upgrade/upgrading.md). That page also has information about some of the most common problems we see.

If you run into a request for FTP credentials with trying to update WP on a IIS server automatically, it may well be a matter of rights. Go into the IIS Management Console, and there to the application pool of your blog. In its advanced settings, change the Process Model Id into LocalSystem. Then on Sites, choose your blog, right click, click on Edit permissions and on security tab add authenticated users. That should do it.

If you experience problems after the upgrade, you can always [restore your backup](https://developer.wordpress.org/advanced-administration/security/backup/)and replace the files with ones from your previous version from the [release archive](https://wordpress.org/download/release-archive/).

### Other options

If you have some knowledge of unix shells you should check out [wp-cli](https://developer.wordpress.org/cli/commands/).

## Dashboard Updates screen

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/dashboard-updates-screen/; edit it into the page. -->

The **Dashboard Updates Screen**
provides the links necessary to install a ‘core’ WordPress upgrade
automatically, or to download the file necessary to complete a manual
upgrade.

In addition to the ‘core’ update process, this Screen provides
the ability to upgrade all plugins and themes, active or inactive, that
have available updates. For installs that have set the language to a
language different from English (United States), you can also install
translation updates.

[![](https://wordpress.org/documentation/files/2019/01/dashboard-updates.png)](https://wordpress.org/support/?attachment_id=11102166)

*Dashboard > Updates when everything is up to date.*

### WordPress updates

#### No upgrade is available

When visiting the **Dashboard Updates Screen**, if you are running the latest version of WordPress, you should see messages like this:

> [!NOTE]
> **Y**o**u have the latest version of WordPress. Future security updates will be applied automatically.**

> *If you need to re-install version x.x, you can do so here or download the package and re-install manually:*

**Re-install now** – Click to to reinstall the current version. You should receive the following messages if the upgrade proceeds successfully:

> [!NOTE]
> *Downloading update from <https://wordpress.org/wordpress-x.x.zip>*

> *Unpacking the core update*

> *Verifying the unpacked files*

> *Installing the latest version*

> *Upgrading database*

> *WordPress upgraded successfully*

**Download x.x** – Click this to download the zip file contain the latest version.

##### An upgrade is available

When visiting the **Dashboard Updates Screen**, and there is an WordPress upgrade available, you should see messages like this:

> [!CAUTION]
> *before upgrading, please backup your database and files.*

**Upgrade Automatically** – Press this button to begin the automatic upgrade process. The following messages will display during and upon completion of the upgrade:

> [!NOTE]
> *Downloading update from <https://wordpress.org/nightly-builds/wordpress-latest.zip>*

> *Unpacking the core update*

> *Verifying the unpacked files*

> *Installing the latest version*

> *Upgrading database*

> *WordPress upgraded successfully*

**Download x.x** – Click this to download the zip file contain the latest version.

##### Once an update is completed

After a successful upgrade is achieved, it is a good time to review any new features about the new Version just installed.

### Plugins

#### No plugins to update

When visiting the **Dashboard Updates Screen**, if your plugins (active and inactive) are at the latest versions, you should see this message:

> [!NOTE]
> *Your plugins are all up to date.*

##### Update plugins

When visiting the **Dashboard Updates Screen**, if there are updates available for one or more plugins (active and inactive), this message displays:

> [!NOTE]
> *The following plugins have new versions available. Check the ones you want to update and then click “Update Plugins”.*

**Update Plugins** – After checking Select All or one or more plugins, click this button to begin the automatic upgrade process. The following messages will display during and upon completion of the upgrade. Messages for each plugin being updated will display. This example shows Akismet being updated:

> [!NOTE]
> *The update process is starting. This process may take awhile on some hosts, so please be patient.*

> *Enabling Maintenance mode…*

> **Updating Plugin Akismet**

> *Downloading update from [plugins](https://wordpress.org/plugins/akismet/).*

> *Unpacking the update…*

> *Installing the latest version.*

> *Removing the old version of the plugin…*

> *Plugin upgraded successfully.*

> *Akismet updated successfully. Show/Hide Details.*

> *Disabling Maintenance mode. All updates have been completed.*

> **Actions:** *Return to Plugins page | Return to WordPress Updates.*

### Themes

#### No themes to update

When visiting the **Dashboard Updates Screen**, if your themes (active and inactive) are at the latest versions, you should see this message:

> [!NOTE]
> *Your themes are all up to date.*

##### Update themes

When visiting the **Dashboard Updates Screen**, if there are updates available for one or more themes (active and inactive), this message displays:

> [!NOTE]
> *The following themes have new versions available. Check the ones you want to update and then click “Update Themes”.*

>  **Please Note:** *Any customization you have made to the Themes files will be lost. Please consider using child themes for modifications.*

**Update Themes** – After checking Themes (to Select All), or one or more themes, click this button to begin the automatic upgrade process. The following messages will display during and upon completion of the upgrade. Messages for each theme being updated will display. This example shows the WordPress Classic theme being updated:

> [!NOTE]
> *The update process is starting. This process may take awhile on some hosts, so please be patient.*

> *Enabling Maintenance mode.*

> **Updating WordPress.**

> *Downloading update.*

> *Unpacking the update…*

> *Installing the latest version…*

> *Removing the old version of the theme…*

> *Theme upgraded successfully.*

> *WordPress updated successfully. Show/Hide Details.*

> *Disabling Maintenance mode.*

> *All updates have been completed.*

> **Actions**:*Return to Themes page | Return to WordPress Updates*

### Translations

#### No translations to update

When visiting the **Dashboard Updates Screen** on a WordPress install that is set to a different language then English (United States), you should see this message if translations are all up to date:

> [!NOTE]
> *Your translations are all up to date.*

##### Update translations

If there are new translations available, this message is displayed:

> [!NOTE]
> *New translations are available.*

Below this text will be a button with the text “Update translations”.

When you click the update button, it will tell you which plugins are downloaded and installed. Plugins for WordPress Core will be installed in */wp-content/languages*, while the translations for plugins and themes will be installed in their subfolder under */wp-content/languages*. This example shows the translations for Twenty Fifteen anf Twenty Sixteen being updated for Dutch (nl_NL):

> [!NOTE]
> *Updating translations*

> *Updating translation for Twenty Fifteen (nl_NL)…*

> *Translation was successfully updated.*

> *Updating translation for Twenty Sixteen (nl_NL)…*

> *Translation was successfully updated.*

> **Actions**:*Return to WordPress Updates*

> **Actions**:*Return to WordPress Updates*

### Troubleshooting

**Problem:** If one of the following messages is received after electing to do the Automatic Upgrade:

> [!NOTE]
> *Downloading update .*

> *Download failed.: Could not open handle for fopen() to latest wordpress.*

> *I*n*stallation Failed*

or

> [!NOTE]
> *Download failed.: name lookup timed out*

> *Installation Failed*

**Solution:** Confirm you are properly connected to the internet then do the Automatic Upgrade again.

**Problem:** After doing the upgrade, and received *WordPress upgraded successfully* message, but the following message still displays:

> [!NOTE]
> *An automated WordPress update has failed to complete – please attempt the update again now.*

**Solution:** Delete the **.maintenance** file found in the WordPress root/base folder, then do the Upgrade again.

**Problem:** After clicking on “automatic upgrade” you get a dialog box asking for “Connection Information.” And, no matter what you enter, you continue to get errors.

**Solution:**  Make sure that your entire wordpress directory is owned by the username under which your Apache server runs. For example, if your server runs as https, and your files live in /var/wordpress do a “chown -R apache.apache /var/wordpress.” Note that you might want to edit some permissions for security purposes, in particular a chmod 640 on wp-config.php, to protect access information to your database.

### Related articles

-   [FAQ Installation](https://github.com/WordPress/Advanced-administration-handbook/blob/main/before-install/howto-install.md)
-   [Troubleshooting about upgrading](https://github.com/WordPress/Advanced-administration-handbook/blob/main/upgrade/upgrading.md#troubleshooting)
