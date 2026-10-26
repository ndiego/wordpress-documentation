---
title: Add a user
description: Add a new user to your site and choose their role.
type: guide
order: 20
redirect_from:
  - /documentation/article/users-add-new-screen/
---

# Add a user

Administrators can add people to a site from the dashboard, without waiting for them to register. You choose each person's role when you add them, which decides what they can do on the site (see [Roles and capabilities](roles-and-capabilities.md)).

![The Add New User screen.](https://wordpress.org/documentation/files/2019/01/add-user.png)

## Add a new user

1.  In the dashboard, go to **Users > Add New User**.
2.  Fill in the fields described below. Only the username and email are required.
3.  Select **Add New User**. A message at the top of the screen confirms that the user was added.

If **Anyone can register** is selected in **Settings > General** (see [General settings](../settings/general.md)), people can also create an account themselves from the login screen. Either way, you can add users here.

## The fields

-   **Username**: the name the user logs in with. It cannot be changed later.
-   **Email**: a valid email address, unique to this user. WordPress sends account emails here, and notifications about comments on the user's posts.
-   **First Name** and **Last Name**: optional; the display name defaults to them.
-   **Website**: optional; the user's website.
-   **Language**: the language of the dashboard for this user. **Site Default** uses the language set in **Settings > General**.
-   **Password**: WordPress suggests a strong password. You can replace it with your own; the strength indicator shows how strong it is.
-   **Send User Notification**: select it to email the new user a link to set their password and log in.
-   **Role**: what the user can do on the site. The default comes from **New User Default Role** in **Settings > General**.
