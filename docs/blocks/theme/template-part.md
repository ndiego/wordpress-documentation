---
title: Template Part
description: Reuse areas such as the header and footer across templates with the Template Part block.
type: reference
slug: template-part-block
redirect_from:
  - /documentation/article/template-part-block/
---

# Template Part

The Template Part block is used while creating and editing templates to manage blocks in areas repeated across the website. This block is often used to create areas like your site header and site footer. When you change blocks inside a template part, the editor updates the blocks on every block template that includes the template part.

> [!NOTE]
> [Learn more about Template editing.](../../design/site-editor/templates.md)

[Watch the video on VideoPress](https://videopress.com/v/GEDQAobI)

https://videopress.com/v/GEDQAobI

## Add a template part

You can add templates when using the [Template Editor](../../design/site-editor/templates.md) or [Site Editor](../../design/site-editor/README.md) to edit templates directly. In order to add a Template Part block, click on the add block button and select the Template Part block. You can also type `/template part` and hit enter in a new paragraph block to add one quickly.

> [!NOTE]
> [Get detailed instructions on adding blocks](../../write/blocks/add-a-block.md).

![Add a template part in template editor](https://wordpress.org/documentation/files/2022/01/Screenshot-2026-09-25-at-4.21.50-PM.png)

After adding a template part, you can choose from existing parts or create a new template part.

### Choosing from existing template parts

Selecting the button **Choose** opens a modal where you can search, preview, and select existing parts. These parts will depend on what your theme has provided.

### Creating new template parts

Selecting **Start blank** will open a modal and prompt you to add a name. Pick a descriptive name so that it’s easy to find in the future.

![](https://wordpress.org/documentation/files/2022/01/Screenshot-2026-09-25-at-4.43.32-PM.png)

### Add a template part in patterns editor

![Pattern admin page with Add Pattern button selected and Add Template Part dropdown option in view.](https://wordpress.org/documentation/files/2022/01/Screenshot-2026-09-25-at-4.37.41-PM-1024x355.png)

If you are using a block theme, you can also create a new template in Administration Screen > Appearance > Editor > Patterns > All template parts. Click on the **Add Pattern** button and choose **Add Template Part** from the dropdown.

You can choose to create one of the following Template Parts:

-   **General** – General templates often perform a specific role like displaying post content, and are not tied to any particular area.
-   **Header** – The Header template defines a page area that typically contains a title, logo, and main navigation.
-   **Footer** – The Footer template defines a page area that typically contains site credits, social links, or any other combination of blocks.
-   **Navigation Overlay** – The Navigation Overlay template defines an overlay area that typically contains navigation links and can be toggled open and closed.

## Edit template parts

[Watch the video on VideoPress](https://videopress.com/v/ea2a8vn6)

https://videopress.com/v/ea2a8vn6

After adding or selecting a Template Part block, you can customize in various ways by adding additional blocks within it. To make it easier to find current template parts to edit, it’s recommended that you use [List View](../../write/blocks/list-view.md).

When you have a template part selected, choose the **Edit original** button to enter a focused mode where you can add or alter blocks. When editing is complete, press the **Save** button, then press the **Back** button next to the template part title to return to the Template Editor.

### Replacing one template part with another

If the theme has more than one pattern for the same template part area, you will see a pattern selector in the design tab of the template inspector panel. If you don’t see this selector, this is because the theme hasn’t provided multiple patterns for the same area.

![Design tab of template inspector that shows additional Header templates](https://wordpress.org/documentation/files/2022/01/template-part-design-1024x507.jpg)

## Advanced settings

The Template Part block has the following unique Advanced Settings:

![Title and area Advanced settings](https://wordpress.org/documentation/files/2022/01/Screenshot-2026-06-29-at-4.17.43-PM.png)

-   **Title:** Rename the template part.
-   **Area:** Select general, header, footer, or navigation overlay.

### Importing widget area

If you’ve switched from a classic theme to a block theme and have widgets that were created in the classic theme, you can import them from the **Import Widget Area** dropdown in the Advanced Settings.

![Import Widget Area menu in the sidebar.](https://wordpress.org/documentation/files/2024/02/importing-widget-area_6.4.jpg)

In addition to these, the following Advanced settings options are available: Additional CSS Class(es), Additional CSS, and HTML Element.

> [!NOTE]
> [Learn more about advanced settings.](../../write/block-settings/advanced.md)
