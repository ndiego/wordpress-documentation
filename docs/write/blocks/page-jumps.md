---
title: Page jumps
description: "Page jumping, also sometimes referred to as anchor links, is where you click a link and instantly get moved somewhere further up or down a page. This can be particularly useful with a long page."
type: guide
order: 70
redirect_from:
  - /documentation/article/page-jumps/
---

# Page jumps

Page jumping, also sometimes referred to as anchor links, is where you click a link and instantly get moved somewhere further up or down a page. This can be particularly useful with a long page.

One way to enable this is by setting an HTML Anchor to a Heading block on your page and creating a link that jumps to the anchor. [You can even jump to another page’s anchor](#jumping-to-an-anchor-on-another-page).

This can also be accomplished with any other block that allows for an HTML Anchor to be set under “Advanced”. You can review which blocks have the HTML anchor field by reviewing the **[Core Blocks Reference](../../blocks/README.md)** and looking for blocks with the `anchor` attribute.

[Watch the video](https://wordpress.org/documentation/files/2022/10/Page-Jumps-HelpHub-Oct-2022.mp4)

## Create an HTML anchor

![Where to add an HTML anchor for a block (Heading block) under Block settings.](https://wordpress.org/documentation/files/2022/10/190138307-c7915fea-353c-44a1-9056-a07a3af12790.png)

1.  Use the Plus Icon to add a new block.
2.  Select Heading as the block type, or start typing `/heading` as a shortcut (slash command) to the heading block.
3.  Enter your heading text. You may leave blank in heading text if you do not want to display any text.
4.  On the right side under Block Settings, click on Advanced.
5.  Type a word that will become your link into the HTML Anchor field.

### HTML anchor syntax

-   HTML Anchor must be unique within a document.
-   HTML Anchor is case-sensitive.
-   HTML Anchor can include following symbols: hyphen(-), underscore(_), colon(:), period(.). It cannot include space.
-   HTML Anchor must start in the alphabet.

## Link to your HTML anchor

1.  Type some text, or add an image or button that will become what you want your visitors to click on to go to another section.
2.  Highlight the text, image or button, and select the link option from the block’s toolbar.
3.  Type in the HTML Anchor you created, starting with the pound (#) symbol. For example, if you created an Anchor named important-notice you would link to #important-notice.

![How to add a link that jumps internally on the page to an HTML anchor.](https://wordpress.org/documentation/files/2022/10/190138761-276173ca-c970-4834-90fd-d4ee23a90218.png)

### Jumping to an anchor on another page

If you want to jump to another page’s anchor, then specify URL with HTML Anchor. For example, `example.com/anotherpage#important-notice`
