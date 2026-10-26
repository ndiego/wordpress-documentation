---
title: Install WordPress
description: Install WordPress with your host's one-click installer, or by hand in about five minutes, or on your own computer.
type: guide
order: 40
redirect_from:
  - /documentation/category/installation/
---

# Install WordPress

After reading this page you can install WordPress on a hosting account, either with the host's installer or by hand, and log in to your new site.

Before you start, choose where WordPress will run: [Choose where to run WordPress](choose-where-to-run-wordpress.md).

## Use your host's installer

Most hosting providers install WordPress for you. Some plans come with WordPress already installed; others have a one-click installer in the hosting control panel, often labeled with the WordPress logo or under a heading such as "Applications" or "Website builder". The names differ from host to host, so check your host's help pages for the exact steps.

A one-click installer usually asks for:

- The domain (and, optionally, a folder) where the site should live.
- A site title, which you can change later.
- An administrator username, password and email address.

When it finishes, it gives you the address of your site and of its login page. Keep the username and password somewhere safe, such as a password manager, then go to [Log in](#log-in).

## Install WordPress by hand

If your host has no installer, or you want to know what one does, install WordPress yourself. This is the famous five-minute install. You need access to your hosting control panel and a way to upload files (an SFTP client or the host's file manager).

1. **Download WordPress.** Get the latest version from [WordPress.org/download](https://wordpress.org/download/) and unzip it on your computer.
2. **Create a database.** In your hosting control panel, create a MySQL or MariaDB database and a database user with all privileges on it. Write down four things: the database name, the database username, its password, and the database host (often `localhost`; your host tells you if it is something else).
3. **Upload the files.** Upload the contents of the `wordpress` folder to your site's web root (often `public_html` or `www`) to put the site at your domain, or into a subfolder to put it at an address such as `example.com/blog`.
4. **Run the setup.** Visit your site's address in a browser. WordPress asks for a language, then lists what it needs. Select **Let's go!**, enter the **Database Name**, **Username**, **Password**, **Database Host** and **Table Prefix** (leave the default `wp_` unless you have a reason to change it), and select **Submit**. WordPress writes its configuration file, `wp-config.php`. Select **Run the installation**.
5. **Fill in the site details.** The installer at `/wp-admin/install.php` asks for a **Site Title**, a **Username** and **Password** for your administrator account, and **Your Email**. The **Search engine visibility** checkbox asks search engines not to index the site while you build it; you can change it later under **Settings > Reading**. Select **Install WordPress**.
6. When you see **Success!**, select **Log In**.

> [!IMPORTANT]
> The administrator account can change everything on the site. Choose a username that is not `admin` and a long, unique password. See [Password best practices](../manage/security/password-best-practices.md).

If WordPress cannot write `wp-config.php` itself, it shows you the contents to paste into the file by hand. For server details, file permissions, a manual `wp-config.php`, and installs in other languages, follow the [detailed installation guide](https://developer.wordpress.org/advanced-administration/before-install/howto-install/) in the Advanced Administration Handbook.

## Install WordPress on your own computer

To build or test a site that only you can see, use a desktop app instead: [Studio by WordPress.com](https://developer.wordpress.com/studio/) or [Local](https://localwp.com/) create a WordPress site in a few clicks, and developers can use [wp-env](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-env/). [WordPress Playground](https://playground.wordpress.net/) runs WordPress in your browser with no install at all. See [Choose where to run WordPress](choose-where-to-run-wordpress.md#on-your-own-computer).

## Log in

Your login page is your site's address followed by `/wp-admin/`, for example `https://example.com/wp-admin/`. WordPress sends you to the login form; enter the username and password you chose. After you log in, you see the dashboard.

## Next

Take a guided first session: [Your first site: a guided tour](your-first-site.md).
