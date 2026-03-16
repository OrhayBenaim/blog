---
title: "Running Claude on Autopilot"
description: "Use a devcontainer to run Claude Code with --dangerously-skip-permissions safely. Full autopilot autonomy without exposing your host machine."
pubDate: 2026-03-16
tags: ["claude-code", "security", "devcontainers", "workflow"]
---

I want Claude Code to just do the work. I don't want to approve every file write, confirm every test run, or click through permission prompts for git commits. I want to describe what I need, walk away, and come back to a finished result.

The `--dangerously-skip-permissions` flag gives you exactly that. Full autonomy. Claude reads, writes, executes, and iterates without stopping to ask. It's the difference between pair programming and delegation.

But the flag has that name for a reason. This post is about getting the freedom without the risk.

![A secure developer workspace floating inside a protective dome](/blog/blog/running-claude-on-autopilot-hero.webp)

## What --dangerously-skip-permissions Actually Does

When you pass `--dangerously-skip-permissions`, Claude can execute any shell command, write to any file, and make network requests, all without asking. On your bare metal machine, that means Claude has the same access you do. Your SSH keys, your cloud credentials, your other projects, your entire filesystem. The risk is low for trusted repos and well-scoped tasks, but there's a smarter way to work.

## The Devcontainer: A Sandbox Built for Claude Code

A devcontainer is a Docker container configured to be your full development environment. You code inside it. Your tools, extensions, and runtimes all live there. And Anthropic provides a <a href="https://github.com/anthropics/claude-code/tree/main/.devcontainer" target="_blank" rel="noopener noreferrer">reference devcontainer</a> built specifically for Claude Code. You don't have to figure this out yourself.

## Setting Up Claude Code in a Devcontainer

Getting Claude Code running inside a devcontainer works with VS Code, JetBrains, the CLI (`devcontainer up`), and GitHub Codespaces. Basically anything that supports the devcontainer spec. Four steps.

**1. Install devcontainer tooling** for your editor or CLI. For VS Code, install the <a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers" target="_blank" rel="noopener noreferrer">Dev Containers extension</a>.

**2. Clone <a href="https://github.com/anthropics/claude-code/tree/main/.devcontainer" target="_blank" rel="noopener noreferrer">Anthropic's reference configs</a>** into your project's `.devcontainer/` directory. There are three files that matter.

**3. Open your project.**

**4. Reopen in container.** Your editor will build the container and drop you inside it.

That's it. Now let me show you what those three config files actually do.

### devcontainer.json

This is the container's entry point. Here are the key parts:

```json
{
  "name": "Claude Code Sandbox",
  "build": { "dockerfile": "Dockerfile" },
  "runArgs": ["--cap-add=NET_ADMIN", "--cap-add=NET_RAW"],
  "mounts": [
    "source=claude-code-bashhistory-${devcontainerId},target=/commandhistory,type=volume",
    "source=claude-code-config-${devcontainerId},target=/home/node/.claude,type=volume"
  ],
  "workspaceMount": "source=${localWorkspaceFolder},target=/workspace,type=bind,consistency=delegated",
  "postStartCommand": "sudo /usr/local/bin/init-firewall.sh",
  "waitFor": "postStartCommand"
}
```

- `NET_ADMIN` and `NET_RAW` capabilities let the firewall script configure iptables rules inside the container
- Volume mounts keep your bash history and Claude config persistent across container rebuilds
- Your project files are bind-mounted into `/workspace`, so you're working on your actual code
- The firewall initializes automatically every time the container starts, and the container waits for it to finish before you can do anything

### Dockerfile

The Dockerfile is based on Node 20 and installs everything the sandbox needs:

```dockerfile
# Network security tools
RUN apt-get update && apt-get install -y \
    iptables ipset iproute2 dnsutils sudo

# Claude Code itself
RUN npm install -g @anthropic-ai/claude-code

# Firewall script with passwordless sudo
COPY init-firewall.sh /usr/local/bin/init-firewall.sh
RUN chmod +x /usr/local/bin/init-firewall.sh
```

- `iptables`, `ipset`, `iproute2`, and `dnsutils` are there for firewall management
- Claude Code is installed globally so it's ready to go
- The firewall script gets passwordless sudo so the non-root container user can run it on startup

### init-firewall.sh

This is where the real security lives. It starts with a default-deny policy:

```bash
# Default-deny everything
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT DROP
```

Nothing gets in or out. Then it whitelists only what Claude needs to function:

- **DNS** (port 53) and **SSH** (port 22) for basic operations
- **Localhost** traffic for local dev servers
- **Host network** so the container can reach your machine
- **GitHub IP ranges**, fetched dynamically from GitHub's meta API
- **Specific domains** resolved via DNS: `registry.npmjs.org`, `api.anthropic.com`, `sentry.io`, `statsig.anthropic.com`, `statsig.com`, `marketplace.visualstudio.com`, `vscode.blob.core.windows.net`, `update.code.visualstudio.com`

Claude can pull npm packages, talk to the Anthropic API, and push to GitHub. Everything else is blocked. If Claude tries to call some random endpoint or exfiltrate data to a server you've never heard of, the packet gets dropped.

When you combine `--dangerously-skip-permissions` with a devcontainer, the risk equation changes entirely.

## Isolation Is the Point

The container is the sandbox. That's the whole idea.

Your host machine's filesystem, your SSH keys, your AWS credentials, your other projects? None of that exists inside the container. Claude can `rm -rf /` and the worst thing that happens is you rebuild the container in thirty seconds. Your actual machine is untouched.

The default-deny firewall is a second layer, but honestly, the isolation is the main event. You're not limiting what Claude can do. You're limiting where it can do it. Full permissions inside a box that can't touch anything important. That's what makes the "dangerous" flag safe.

I've been running this setup for my own projects and it's the best of both worlds. Full autonomy for Claude, zero risk for me. The container rebuilds fast, the volume mounts keep my config persistent, and I never have to click "approve" on a file write again.

## Get Started

Grab the reference configs from <a href="https://github.com/anthropics/claude-code/tree/main/.devcontainer" target="_blank" rel="noopener noreferrer">Anthropic's repo</a>, drop them in your project, and reopen in a container. The <a href="https://docs.anthropic.com/en/docs/claude-code" target="_blank" rel="noopener noreferrer">official docs</a> cover the details if you want to customize further.
