---
title: WordPress and AI
description: How to use AI assistants with this documentation and with a WordPress site, what works today, and what is still being built.
type: concept
order: 60
---

# WordPress and AI

After reading this page you know what this section covers, which parts describe things you can do today, and which parts describe work in progress. Edited locally.

## What this section covers

People increasingly ask an AI assistant before they open the documentation, and some let an agent do the work for them. This section covers two different things:

- **Using AI assistants with this documentation**, so the answers you get about WordPress come from current, accurate pages instead of from whatever a model remembers.
- **Using AI with your WordPress site**: connecting an agent to the site, building a site with one, writing with AI in the editor, and keeping control of what an agent is allowed to do.

## What is real today

This documentation is built to be read by assistants as well as people. Every page is available as clean Markdown at a stable address, the whole set has a machine-readable index, and each page has buttons to copy it or open it in an assistant. You can use all of that now, with any assistant that can read a web page. [Use this documentation with an AI assistant](use-the-docs-with-ai.md) explains how.

WordPress also already has the building blocks that agents use to work with a site: the REST API, which lets other software read and change content, and application passwords, which give that software its own revocable credentials instead of your password. Developers and tools use them today.

## What is being built

WordPress 6.9 and later include the Abilities API, which lets WordPress, plugins and themes describe what a site can do in a form that software can discover, and WordPress 7.1 has a **Settings > Connectors** screen for connecting the site to external services such as AI providers. The WordPress project is building on them: an adapter that lets AI agents use a site's abilities through the Model Context Protocol (MCP), and AI features for the editor. Those are not documented here yet, because their final shape is still changing.

The pages for them exist now as **placeholders**: each one says so at the top, outlines what it will cover, and makes no claims about features that are not released. They are:

- [Connect an AI agent to your site](connect-an-agent.md)
- [Build a site with an agent](build-a-site-with-an-agent.md)
- [Write and edit with AI](write-with-ai.md)
- [Permissions and safety for agents](agent-permissions-and-safety.md)

Until the last page is written, one principle applies today, whatever tool you use: give each tool its own application password and only the role it needs.

## A note on accuracy

An AI assistant can be wrong, including about WordPress. It may describe a screen from an older version, invent a setting, or recommend a plugin that no longer exists. When an answer matters, ask the assistant to cite the page it used, and check the step against your own site before you rely on it.
