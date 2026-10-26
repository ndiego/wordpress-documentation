---
title: Permissions and safety for agents
description: "Placeholder: how to keep control of what an AI agent can do on your WordPress site, with principles that apply today."
type: concept
order: 50
status: placeholder
---

# Permissions and safety for agents

This page is a placeholder for documentation that does not exist yet. The full page will explain how agent permissions work once the features in [Connect an AI agent to your site](connect-an-agent.md) are released. The principles below already apply, whatever tool or connection you use.

## Principles

- **Least privilege.** Give an agent its own user account with the lowest role that lets it do the task, such as Author or Contributor, never your own administrator account. See [Roles and capabilities](../manage/users/roles-and-capabilities.md).
- **Review before publish.** Let an agent create drafts, and have a person read and publish them. A Contributor account enforces this: it cannot publish.
- **An audit trail.** Use a separate account and separate credentials for each agent, so posts, revisions and logs show what the agent did. Revisions let you see and undo each change.
- **Revoke access.** Use credentials you can revoke on their own, such as an application password, and revoke them when the task is finished or when something looks wrong.
- **What agents should never do without a person:** install or delete plugins and themes, change users or roles, change site settings, delete content, publish, or handle payments and personal data.

## How permissions will work

How the roles and capabilities WordPress already has will apply to agents, and any agent-specific controls.

## Credentials

How to create, scope, store and revoke the credentials an agent uses.

## Watch what an agent does

How to see an agent's activity, and how to undo it.

## When something goes wrong

What to do if an agent makes a change you did not want: revoke its access, restore from revisions or a backup, and check the rest of the site. See [Security](../manage/security/README.md).
