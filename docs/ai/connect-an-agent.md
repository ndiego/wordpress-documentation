---
title: Connect an AI agent to your site
description: "Placeholder: how an AI agent will connect to a WordPress site, what works today through the REST API, and what the project is building."
type: guide
order: 20
status: placeholder
---

# Connect an AI agent to your site

This page is a placeholder for documentation that does not exist yet. It outlines what the page will cover once the features it describes are released and documented. Nothing below is a set of instructions.

## What connecting an agent means

An agent connected to your site can read and change it on your behalf: draft a post, update a page, upload an image. To do that it needs a way in, credentials that identify it, and limits on what it may do.

## What works today: application passwords and the REST API

WordPress has a REST API that lets other software read and change content, and application passwords, which you create under **Users > Profile** to give a tool its own credentials that you can revoke at any time. This section will explain how an agent uses them, and their limits.

## The direction: the MCP adapter and the Abilities API

WordPress 6.9 and later include the Abilities API, a way for WordPress, plugins and themes to describe what a site can do in a form that software can discover. The WordPress project is working on an adapter, developed separately from WordPress itself, that exposes those abilities to AI agents through the Model Context Protocol (MCP). This section will describe them once they are ready for site owners.

## What you will be able to ask an agent to do

Examples of tasks, matched to the permissions each one needs, once the features above are documented.

## Where to go next

This page will link to the feature documentation, to [Permissions and safety for agents](agent-permissions-and-safety.md), and to the developer documentation for each API.
