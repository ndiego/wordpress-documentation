---
title: Smilies
description: "How WordPress turns text smileys such as :-) into images, and how to turn that off."
type: reference
order: 30
redirect_from:
  - /documentation/article/what-are-smilies/
---

# Smilies

## What are smileys?

Smileys, also known as “emoticons”, are *glyphs* used to convey emotions in your writing. They are a great way to brighten up posts. 🙂

Text smileys are created by typing two or more punctuation marks. Some examples are:

`;-)` is equivalent to 😉

`:-)` is equivalent to 🙂

`:-(` is equivalent to 🙁

`:-?` is equivalent to 😕

To learn more about emoticons and their history, see the [Wikipedia entry on Emoticons](http://en.wikipedia.org/wiki/Emoticons).

### Smileys are not emoji

Although smileys and emoji can both display smiley faces and such, emoji are a newer development and have a much wider range of images that can be displayed. (They are also created differently.) For more information on emoji and how to use them, see the [Emoji](https://codex.wordpress.org/Emoji) page.

## How does WordPress handle smileys?

By default, WordPress automatically converts text smileys to graphic images. When you type `;-)` in your post you see 😉 when you preview or publish your post.

## To turn off graphic smileys

As of WordPress 4.3, the option to disable graphic smileys was removed from new installs. There is [a plugin](https://wordpress.org/plugins/keep-emoticons-as-text/) if you want to retain the option.

## What text do I type to make smileys?

Smiley images and the text used to produce them\*:

| icon | text | text | full text | icon | full text |
| --- | --- | --- | --- | --- | --- |
| 🙂 | `:)` | `:-)` | `:smile:` | 😆 | `:lol:` |
| 😀 | `:D` | `:-D` | `:grin:` | 😳 | `:oops:` |
| 🙁 | `:(` | `:-(` | `:sad:` | 😥 | `:cry:` |
| 😮 | `:o` | `:-o` | `:eek:` | 👿 | `:evil:` |
| 😯 | `8O` | `8-O` | `:shock:` | 😈 | `:twisted:` |
| 😕 | `:?` | `:-?` | `:???:` | 🙄 | `:roll:` |
| 😎 | `8)` | `8-)` | `:cool:` | ❗ | `:!:` |
| 😡 | `:x` | `:-x` | `:mad:` | ❓ | `:?:` |
| 😛 | `:P` | `:-P` | `:razz:` | 💡 | `:idea:` |
| 😐 | `:\|` | `:-\|` | `:neutral:` | ➡ | `:arrow:` |
| 😉 | `;)` | `;-)` | `:wink:` | ![:mrgreen:](https://wordpress.org/documentation/wp-includes/images/smilies/mrgreen.png) | `:mrgreen:` |

*\* In some instances, multiple text options are available to display the same smiley.*

Category:Getting Started

## Troubleshooting smileys

### Why doesn’t it work?

Smileys may have been disabled by your WordPress admin. Another possibility is the smiley image files have been deleted from `/wp-includes/images/smilies`.

### Why doesn’t it work for me?

*If smileys work for others at your site but not for you:*

Type a space before and after your smiley text. That prevents the smiley being accidentally included in the text around it. 😳

Make sure not to use quotes or other punctuation marks before and after the smiley text. 🙄

### Where are my smiley images kept?

The smiley or emoticon image graphics are found in the `/wp-includes/images/smilies` directory.

Note that smileys is spelled ‘eys’ in this documentation and the directory name for the smiley images is *‘smilies*, spelled ‘ies’. 😯

### How can I have different smiley images appear?

The easiest way is to filter the smilies.

Upload the images you want with the same name to your server (say in wp-content/images/smilies) and put this in your theme’s function.php:

```php
add_filter( 'smilies_src', 'my_custom_smilies_src', 10, 3 );
function my_custom_smilies_src( $img_src, $img, $siteurl )
{
        return $siteurl.'/wp-content/images/smilies/'.$img;
}
```

That will replace http://example.com/wp-includes/images/smilies/icon_question.gif with http://example.com/wp-content/images/smilies/icon_question.gif

### Why are my smiley images blank?

If you recently uploaded the images, it could be that the images have been uploaded in ***ASCII*** format by your FTP program. Re-upload the smileys ensuring that they are transferred in ***BINARY*** format.

Some FTP programs have an **auto-detect** setting which will upload files in the correct format without user intervention. If you have such a setting, turn it on.

## Smiley CSS

The smiley images in WordPress are automatically given a [CSS](../../get-started/glossary.md#css) class of **wp-smiley** when they are displayed in a post. You can use this class to style your smileys differently from other post images.

For example, it’s not uncommon to set up images in a post to appear on the left-hand side of the content with text flowing around the image. The CSS for that might look like this:

```php
.post img {
        float: left;
}
```

This would typically affect all images in a post, **including** your smiley images. To *override* this so that smileys stay inline, you could add this to your CSS:

```php
img.wp-smiley {
        float: none;
}
```

For more on CSS in WordPress, you might want to [start here](https://codex.wordpress.org/CSS).

## More information on smileys

-   [Wikipedia – Emoticon](http://en.wikipedia.org/wiki/Emoticon)
