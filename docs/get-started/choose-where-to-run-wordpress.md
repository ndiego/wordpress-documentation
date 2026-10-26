---
title: Choose where to run WordPress
description: Compare a hosting provider, your own computer and your browser as places to run WordPress, and pick the one that fits.
type: guide
order: 30
redirect_from:
  - /documentation/article/hosting-wordpress/
---

# Choose where to run WordPress

After reading this page you can choose where your WordPress site runs: on a hosting provider for a public site, on your own computer for building and testing, or in your browser to try WordPress in a minute with nothing to install.

WordPress is software that needs a web server, a database and PHP. All three options below provide them; they differ in who can see the site, how long it lasts and how much you manage yourself.

## At a glance

| | Hosting provider | Your own computer | In the browser (Playground) |
|---|---|---|---|
| Who can visit the site | Anyone on the internet | Only you, on that computer | Only you, in that browser tab |
| Cost | A monthly or yearly fee | Free | Free |
| Setup | One-click install, or WordPress is already installed | Install a desktop app | Open a web page |
| How long the site lasts | As long as you keep the hosting | Until you delete it | Until you close the tab, unless you save or export it |
| Good for | A real site with real visitors | Building, testing, learning, working offline | Trying WordPress, testing a theme or plugin, demos |
| You need a domain name | Yes, usually bought with the hosting or separately | No | No |

You can combine them. Many people build a site on their own computer and then move it to a host when it is ready.

## On a hosting provider

A hosting provider rents you space on a web server that is connected to the internet all the time. This is where a public site lives.

Hosts offer two kinds of plans:

- **Generic hosting**, for many kinds of web software, including WordPress.
- **WordPress hosting**, set up for WordPress. WordPress is often installed for you, and the plan may include backups, automatic updates, caching and staging sites.

If you are new to WordPress, a host with WordPress experience saves you work.

### What to look for in a host

- **It meets the WordPress requirements.** The [requirements page on WordPress.org](https://wordpress.org/about/requirements/) lists the recommended versions of PHP and MySQL or MariaDB, and HTTPS support. It also has a letter you can send to a host to ask whether it meets them.
- **HTTPS is included**, with a free certificate, so your site loads over a secure connection.
- **Backups** run automatically, and you can restore one yourself.
- **Updates.** The host keeps PHP current, and lets WordPress update itself.
- **Support** that knows WordPress and answers when you need it.
- **A one-click installer** or WordPress already installed.

### Where to find hosts

- [WordPress hosting](https://wordpress.org/hosting/) on WordPress.org lists hosts that support WordPress.
- The [WordPress support forums](https://wordpress.org/support/forums/) have threads where people share their experience.
- Local WordPress meetups and the [Make WordPress Slack](https://make.wordpress.org/chat/) are good places to ask what people use.

## On your own computer

A local site runs on your computer only. Nobody else can see it, it costs nothing, and it works without an internet connection. It is the right place to learn, to build a site before launch, or to test changes before you make them on a live site.

- **[Studio by WordPress.com](https://developer.wordpress.com/studio/)** is a free desktop app for macOS and Windows. It creates a local WordPress site in a few clicks.
- **[Local](https://localwp.com/)** is a free desktop app for macOS, Windows and Linux that creates and manages local WordPress sites.
- **[wp-env](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-env/)** is a command-line tool for developers. It sets up WordPress in Docker with one command and is used for theme and plugin development.

When your site is ready, you move it to a host. Some tools, and many hosts, have a migration feature, and migration plugins do the same job.

## In the browser, with nothing to install

[WordPress Playground](https://playground.wordpress.net/) runs a complete WordPress site inside your web browser, using WebAssembly. Open the page and you have a working site with the dashboard and the editor, in a few seconds, with no account and no server.

A Playground site is temporary. When you close the tab or reload the page, the site and everything you did in it are gone unless you save it in the browser or export it as a file first. Use Playground to try WordPress, follow this documentation, or test a theme or plugin. Do not use it for a site you want to keep.

## Which one to choose

- **You want a public site.** Choose a hosting provider.
- **You want to learn WordPress or build a site before anyone sees it.** Start on your own computer.
- **You want to look around for five minutes.** Open Playground.

## Next

[Install WordPress](install-wordpress.md) on the host or computer you chose. If you picked Playground, WordPress is already running: go to [Your first site: a guided tour](your-first-site.md).
