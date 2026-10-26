---
title: Security
description: Keep your WordPress site secure with updates, strong logins, the right roles, backups and HTTPS, and know what to do if it is hacked.
type: guide
order: 60
---

# Security

After reading this page you can protect your WordPress site against the most common attacks, and you know what to do if something goes wrong. None of it needs code, and most of it you set up once.

## Keep everything updated

Most hacked WordPress sites were running outdated software with a known security hole. Updates close those holes.

- WordPress installs minor releases, which carry security fixes, automatically by default. Leave that on.
- Turn on auto-updates for plugins and themes: on **Plugins > Installed Plugins** and **Appearance > Themes**, select **Enable auto-updates** for each one you trust to update without you.
- Check **Dashboard > Updates** regularly for anything that is not automatic, and update to each new major release of WordPress.
- Ask your host to keep PHP on a supported version. **Tools > Site Health** tells you when it is out of date.

See [Updates](../updates/README.md) and [Auto-updates](../updates/auto-updates.md).

## Protect every login

- Give every account a long, unique password, stored in a password manager. WordPress suggests a strong password when you create a user or change a password. See [Password best practices](password-best-practices.md).
- Do not use `admin` as a username.
- Add two-factor authentication, so a stolen password is not enough to log in. WordPress does not include it, but plugins from the [Plugin Directory](https://wordpress.org/plugins/tags/two-factor-authentication/) add it.
- Remove accounts that are no longer used.

## Give each person the role they need

Every user has a role, and the Administrator role can change everything, including installing code. Give administrator access to as few people as possible, and give everyone else the lowest role that lets them do their work: an Editor to manage content, an Author to publish their own posts, a Contributor to write without publishing. See [Roles and capabilities](../users/roles-and-capabilities.md).

## Back up your site

A backup lets you recover from a hack, a bad update or a mistake. A complete backup has both the database and the files (`wp-content` holds your themes, plugins and uploads). Many hosts back up automatically; check how often, how long they keep backups, and how you restore one. If your host does not, use a backup plugin, and store copies somewhere other than your hosting account.

## Use HTTPS

HTTPS encrypts the connection between your visitors and your site, including your password when you log in. Most hosts include a free certificate. Once it is active, make sure both addresses under **Settings > General** start with `https://`. Site Health warns you when the site is not using HTTPS.

## Choose plugins and themes with care

Every plugin and theme you install runs with full access to your site. Before you install one, check in its directory listing when it was last updated, whether it is tested with your version of WordPress, how many sites use it, its reviews, and whether support questions get answers. Install from the [Plugin Directory](https://wordpress.org/plugins/) and [Theme Directory](https://wordpress.org/themes/) or from developers you trust, never from sites that offer paid products for free. Delete plugins and themes you do not use; a deactivated plugin can still be attacked.

## If your site is hacked

Signs include pages you did not create, redirects to other sites, unknown administrator accounts, or a warning from your host or a search engine. Act quickly: change every password, contact your host, and restore a clean backup or clean the site. [My site was hacked](site-was-hacked.md) walks you through it step by step.

> [!TIP]
> For server-level hardening, such as file permissions and `wp-config.php` settings, see [Hardening WordPress](https://developer.wordpress.org/advanced-administration/security/hardening/) in the Advanced Administration Handbook.
