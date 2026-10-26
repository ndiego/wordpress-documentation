---
title: General settings
description: "Set your site's title, tagline, address, admin email, language, time zone and date format on the Settings > General screen."
type: reference
order: 10
redirect_from:
  - /documentation/article/settings-general-screen/
---

# General settings

The **Settings > General** screen holds the most basic settings for your site: its title and address, who may register an account, the language of the dashboard, and how dates and times are calculated and shown. It is the screen that opens when you select **Settings** in the dashboard.

![The Settings > General screen with the site title, tagline and address fields.](https://wordpress.org/documentation/files/2018/11/general-settings.jpg)

## The settings on this screen

### Site title

Enter the name of your site (or blog) here. Most themes show this title at the top of every page, and browsers show it in the tab. WordPress also uses this title as the identifying name for your [Syndication](../../get-started/glossary.md#syndication) feeds.

### Tagline

In a few words, say what your site is about. A tagline is a short phrase or sentence that sums up the site; many themes show it next to the site title. It is empty by default.

### WordPress address (URL)

Enter the full URL of the directory containing your WordPress core application files (for example `wp-config.php`, `wp-admin`, `wp-content` and `wp-includes`). For example, if you installed WordPress into a directory called “blog”, then the WordPress address would be `http://example.net/blog` (where example.net is your domain). If you installed WordPress into your web root, this address will be the root URL `http://example.net`. WordPress will trim a slash (`/`) from the end. If you defined the **WP_SITEURL** constant in your [`wp-config.php`](../wp-config.md) file, that value will appear in this field and you will not be able to make changes to it from the WordPress administration screen.

### Site address (URL)

Enter the address you want people to type in their browser to reach your WordPress site. This is the directory where WordPress’s main `index.php` file is installed. The *Site address (URL)* is identical to the *WordPress address (URL)* (above) unless you are [giving WordPress its own directory](https://github.com/WordPress/Advanced-administration-handbook/blob/main/server/wordpress-in-directory.md). WordPress will trim a slash (`/`) from the end. If you defined the **WP_HOME** constant in your [`wp-config.php`](../wp-config.md) file, that value will appear in this field and you will not be able to make changes to it from the WordPress administration screen.

### Administration email address

Enter the email address WordPress should use for site administration notifications.

This address may receive notifications about:

-   comment moderation,
-   user registration,
-   site updates and maintenance,
-   recovery mode and fatal errors,
-   plugin or theme issues,
-   and other administrative events.

The Administration Email Address is different from the email address associated with an individual user account.

Changing this setting does not change the email address used to log in to WordPress. User account email addresses can be managed under Users → Profile.

When you change the Administration Email Address, WordPress sends a confirmation email to the new address. The new address does not become active until the confirmation link in that email is clicked. Until then, the existing administration email address remains active.

After saving changes, WordPress displays a notice indicating that the new email address is pending confirmation.

If you do not receive the confirmation email:

-   Check your spam or junk folder.
-   Allow a few minutes for delivery.
-   Verify that your hosting provider or email service is configured to send WordPress emails correctly.
-   Test whether your site can send email successfully.
-   Consider using an SMTP plugin or transactional email service if emails from your site are not being delivered reliably.

If your site was originally set up by a developer or agency, verify that the Administration Email Address points to an address your organization can access. Recovery mode and critical error notifications are sent to this address.

If email delivery problems continue, contact your hosting provider or system administrator.

### Membership

Select **Anyone can register** if you want anyone to be able to create an account on your site.

### New user default role

Select the default [Role](../users/roles-and-capabilities.md) that is assigned to new users. This Default [Role](../users/roles-and-capabilities.md) will be assigned to newly registered members or users added on the [Users screen](../users/users-screen.md). Valid choices are [Administrator](../users/roles-and-capabilities.md#administrator), [Editor](../users/roles-and-capabilities.md#editor), [Author](../users/roles-and-capabilities.md#author), [Contributor](../users/roles-and-capabilities.md#contributor), or [Subscriber](../users/roles-and-capabilities.md#subscriber).

### Site language

The WordPress dashboard language.

### Timezone

From the drop-down box, choose a city in the same timezone as you. For example, under America, select New York if you reside in the Eastern Timezone of the United States that observes daylight saving time. If you can’t identify a city in your timezone, select one of the **Etc GMT** settings that represents the number of hours by which your time differs from [Greenwich Mean Time](https://en.wikipedia.org/wiki/Greenwich_Mean_Time). Click the **Save Changes** button and the [UTC time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) and “Local time” will display to confirm the correct Timezone was selected.

### Date format

The format in which to display dates on your site. The Date Format setting is intended to be used by theme designers in displaying dates on your site, but does not control how the date is displayed in the Administrative Screens (such as the Posts screen). Click the **Save Changes** button and the “Output” example below will show the current date in the format entered. See [Formatting Date and Time](date-and-time-format.md) for some of the formats available.

### Time format

The format in which to display times on your site. The Time Format setting is intended to be used by theme designers in displaying time on your site, but does not control how the time is displayed in the Administrative Screens (such as the publish date in the editor). Click the **Save Changes** button and the “Output” example below will show the current time in the format entered. See [Formatting Date and Time](date-and-time-format.md) for some of the formats available.

### Week starts on

Select the day WordPress calendars start on. Monday is the default setting for this drop-down, meaning a monthly calendar will show Monday in the first column. If you want your calendar to show Sunday as the first column, then select Sunday from the drop-down.

### Save changes

Click the **Save Changes** button to ensure any changes you have made to your Settings are saved to your database. Once you click the button, a confirmation text box will appear at the top of the page telling you your settings have been saved.
