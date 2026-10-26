---
title: Audio and video shortcodes
description: "The Audio feature allows you to embed audio files and play them back using a simple Shortcode. This was added as of WordPress 3.6 and is used like this:"
type: reference
order: 30
redirect_from:
  - /documentation/article/audio-shortcode/
  - /documentation/article/video-shortcode/
---

# Audio and video shortcodes

The Audio feature allows you to embed audio files and play them back using a simple Shortcode. This was added as of WordPress 3.6 and is used like this:

```json
[ audio]
```

Note: Do not put space between “[” and “audio”.

You can also use build-in embeds and simply put the media file on its own line:

```text
My cool content
http://my.mp3s.com/cool/songs/coolest.mp3
More cool content
```

## Usage

I have an old post that has an audio file in the Media Library attached to it, and I want to use the new shortcode:

```json
[ audio]
```

Note: Do Not put Space between “[” and “audio”.

I have the URL for an MP3, from the Media Library or external, that I want to play:

```json
[audio src="audio-source.mp3"]
```

I have a source URL and fallbacks for other HTML5-supported filetypes:

```json
[audio mp3="source.mp3" ogg="source.ogg" wav="source.wav"]
```

## Options

The following basic options are supported:

`src`

([string](../../get-started/glossary.md#string)) (optional) The source of your audio file. If not included it will auto-populate with the first audio file attached to the post. You can use the following options to define specific filetypes, allowing for graceful fallbacks:

-   ‘mp3’, ‘m4a’, ‘ogg’, ‘wav’, ‘wma’

Default: First audio file attached to the post

`loop`

([string](../../get-started/glossary.md#string)) (optional) Allows for the looping of media.

-   “off” – Do not loop the media.
-   “on” – Media will loop to the beginning when finished and automatically continue playing.

Default: “off”

`autoplay`

([string](../../get-started/glossary.md#string)) (optional) Causes the media to automatically play as soon as the media file is ready.

-   “off” – Do not automatically play the media.
-   “on” – Media will play as soon as it is ready.

Default: “off”

`preload`

([string](../../get-started/glossary.md#string)) (optional) Specifies if and how the audio should be loaded when the page loads. Defaults to “none”

-   “none” – The audio should not be loaded when the page loads.
-   “auto” – The audio should be loaded entirely when the page loads.
-   “metadata” – Only metadata should be loaded when the page loads.

Default: “none”

## Related

WordPress Shortcodes: [video](audio-video-shortcodes.md), [caption](https://codex.wordpress.org/Caption_Shortcode), [embed](https://codex.wordpress.org/Embed_Shortcode), [gallery](https://codex.wordpress.org/Gallery_Shortcode), [playlist](https://codex.wordpress.org/Playlist_Shortcode)

## Video shortcode

<!-- TODO: merge: this section was absorbed from https://wordpress.org/documentation/article/video-shortcode/; edit it into the page. -->

The **Video** feature allows you to embed video files and play them back using a simple shortcode. This was added as of WordPress [Version 3.6](https://wordpress.org/documentation/wordpress-version/version-3-6/) and is used like this:

```json
[video]
```

You can also use built in embeds and simply put the media file on its own line:

```text
My cool content
http://my.movies.com/cool/movie/coolest.mp4
More cool content
```

### Usage

I have an old post that has an audio file in the Media Library attached to it, and I want to use the new shortcode:

```json
[video]
```

Note: Do Not put Space between “[” and “video”.

I have the URL for an MP3, from the Media Library or external, that I want to play:

```json
[video src="video-source.mp4"]
```

I have a source URL and fallbacks for other HTML5-supported filetypes:

```json
[video mp4="source.mp4" webm="source.webm" ogv="source.ogv"]
```

### Options

The following basic options are supported:

`src`

(string) (optional) The source of your video file. If not included it will auto-populate with the first video file attached to the post. You can use the following options to define specific filetypes, allowing for graceful fallbacks:

-   mp4, m4v, webm, ogv, wmv, flv

Default: First video file attached to the post

`poster`

Defines image to show as placeholder before the media plays.

Default: none

`loop`

(string) Allows for the looping of media. Defaults to “off.”

-   “off” – (“default”) does not loop the media
-   “on” – media will loop to beginning when finished and automatically continue playing

Default: “off”

`autoplay`

(string) Causes the media to automatically play as soon as the media file is ready. Defaults to “off.”

-   “off” – (“default”) does not automatically play the media
-   “on” – Media will play as soon as the media is ready

Default: “off”

`preload`

(string) (optional) Specifies if and how the video should be loaded when the page loads. Defaults to “metadata.”

-   “metadata” – (“default”) only metadata should be loaded when the page loads
-   “none” – the video should not be loaded when the page loads
-   “auto” – the video should be loaded entirely when the page loads

Default: “metadata”

`height`

(integer) (required) Defines height of the media. Value is automatically detected on file upload.

Default: [Media file height]

`width`

(integer) (required) Defines width of the media. Value is automatically detected on file upload.

Default: [Media file width]

`muted`

 (string) Mutes the video when it starts playing. This is particularly useful for autoplay videos.

-   “off” – (“default”) the video is not muted
-   “on” – the video will be muted
-   Default: “off”

### Related

WordPress Shortcodes: [audio](audio-video-shortcodes.md), [caption](https://codex.wordpress.org/Caption_Shortcode), [embed](https://codex.wordpress.org/Embed_Shortcode), [gallery](https://codex.wordpress.org/Gallery_Shortcode), [playlist](https://codex.wordpress.org/Playlist_Shortcode)
