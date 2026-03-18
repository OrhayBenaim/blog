---
title: "NemoClaw: NVIDIA's Open Source Security Layer for OpenClaw"
description: "NemoClaw is NVIDIA's open-source security layer for OpenClaw AI agents. Sandboxing with Landlock, seccomp, and network namespaces in one command."
pubDate: 2026-03-18
pubTime: "14:30"
tags: ["nemoclaw", "nvidia", "openclaw", "security", "ai-agents"]
---

NVIDIA just shipped <a href="https://www.nvidia.com/en-us/ai/nemoclaw/" target="_blank" rel="noopener noreferrer">NemoClaw</a>, an open-source security layer for OpenClaw AI agents. One command to install. It wraps your OpenClaw agents in a real sandbox with Landlock, seccomp, and network namespaces. Not a wrapper script. Not a permissions popup. Actual kernel-level isolation.

If you've been running OpenClaw agents on your machine, you already know the problem. These agents have broad system access. They can read files, make network requests, execute commands. That's what makes them useful, but it's also what makes them risky. NemoClaw is NVIDIA's answer to that gap.

![Jensen Huang cartoon character with crab claws, the NemoClaw mascot](/blog/blog/nvidia-nemoclaw-hero.webp)

## What is OpenClaw (and Why AI Agent Security Matters)

OpenClaw is an open-source AI agent framework created by Peter Steinberger. It runs locally, connects to your chat apps (Telegram, Discord, WhatsApp, and more), and lets AI agents actually do things on your machine. Think file management, shell commands, web automation, over 100 preconfigured skills. It hit 60,000+ GitHub stars in 72 hours and became one of the fastest-growing open-source projects this year.

People use it because it's model-agnostic, self-hosted, and privacy-focused. You bring your own API keys or run local models. No subscription, no cloud dependency.

The catch is that running an autonomous agent with full system access on your actual machine is a security gamble. OpenClaw doesn't enforce guardrails out of the box. Your agent can reach any endpoint, read any file it has permissions for, and execute whatever it wants. If you've read my post about [running Claude on autopilot](/blog/running-claude-on-autopilot), you know why sandboxing matters for autonomous AI tools. The same principle applies here, just a different agent.

## What NemoClaw Does: NVIDIA's Security Sandbox for AI Agents

NemoClaw is an open-source stack that adds privacy and security controls to OpenClaw. It's built on <a href="https://github.com/NVIDIA/OpenShell" target="_blank" rel="noopener noreferrer">NVIDIA OpenShell</a>, a runtime designed specifically for running autonomous agents safely.

The architecture has four pieces that work together:

- **Plugin**: A TypeScript CLI that integrates with OpenClaw's existing command structure. This is what you interact with.
- **Blueprint**: A versioned Python artifact that orchestrates sandbox creation, policy application, and inference setup through the OpenShell CLI.
- **Sandbox**: An isolated OpenShell container where your agent actually runs. This is where the security enforcement happens.
- **Inference**: Routes model API calls through NVIDIA's cloud, specifically to <a href="https://build.nvidia.com/" target="_blank" rel="noopener noreferrer">Nemotron 3 Super 120B</a> on build.nvidia.com.

### The Four Protection Layers

This is where NemoClaw gets interesting. OpenShell enforces four distinct security boundaries around your agent:

**Network isolation** uses Linux network namespaces to control outbound connections. Only endpoints listed in your policy are allowed. Everything else gets blocked. When the agent tries to reach an unlisted host, OpenShell surfaces the request in a terminal UI for you to approve or deny. This layer is hot-reloadable, so you can update network policies without restarting the sandbox.

**Filesystem restrictions** use Landlock to prevent reads and writes outside `/sandbox` and `/tmp`. The agent can work in its own directory and use temp files, but it can't touch anything else on the system. This layer is locked at sandbox creation. No runtime changes.

**Process security** uses seccomp to block privilege escalation and dangerous syscalls. The agent can't break out of its container, can't gain root, can't call syscalls it doesn't need. Also locked at creation.

**Inference routing** intercepts every model API call from the agent and routes it through controlled backends. The agent never makes direct calls to model providers. This means you can monitor, audit, and control what models the agent talks to. Like the network layer, this is hot-reloadable.

NemoClaw also ships with a TUI (terminal user interface) for monitoring sandbox activity and handling operator approvals in real time. You launch it with `openshell term` and get a live, keyboard-driven dashboard showing what your agent is doing, what requests it's making, and what's been blocked.

## Installation

There are two paths to get NemoClaw running.

### Local or VM

On a Linux machine (or WSL2 on Windows), it's a one-liner:

```bash
curl -fsSL https://nvidia.com/nemoclaw.sh | bash
```

This installs Node.js if needed, sets up OpenShell, and drops you into the onboard wizard:

```bash
nemoclaw onboard
```

The wizard walks you through naming your sandbox, configuring your NVIDIA API key, and selecting a model. When it finishes, you get a summary like this:

```
Sandbox:   my-assistant
Security:  Landlock + seccomp + netns
Model:     nvidia/nemotron-3-super-120b-a12b

  nemoclaw my-assistant connect   # interactive shell
  nemoclaw my-assistant status    # health check
  nemoclaw my-assistant logs      # stream logs
```

### Cloud (one-click)

If you don't have a Linux machine handy, NVIDIA offers a <a href="https://brev.nvidia.com/launchable/deploy?launchableID=env-3Azt0aYgVNFEuz7opyx3gscmowS" target="_blank" rel="noopener noreferrer">one-click Brev deploy</a> that spins up a GPU instance with NemoClaw pre-installed. There's also an experimental CLI option:

```bash
nemoclaw deploy <instance>
```

This installs Docker, the NVIDIA Container Toolkit (if a GPU is present), and OpenShell on the VM, then runs setup and connects you to the sandbox.

### Key Commands After Install

Once your sandbox is running, here are the commands you'll actually use:

```bash
nemoclaw my-assistant connect    # drop into the agent's shell
nemoclaw my-assistant status     # check sandbox health and config
nemoclaw my-assistant logs --follow  # tail logs in real time
openshell term                   # launch the TUI dashboard
```

## Use Cases

Here are the scenarios where NemoClaw actually makes sense right now.

**Sandboxed coding assistants.** You want an AI agent that can write and run code but can't reach arbitrary endpoints or read files outside the project. If you've set up [Claude Code with custom configs](/blog/claude-code-config-guide), you already understand the value of controlled environments. NemoClaw's network and filesystem policies handle this directly. The agent codes inside `/sandbox`, and everything else is off limits.

**Always-on agents on RTX or DGX hardware.** If you have NVIDIA hardware sitting around, you can run a persistent OpenClaw agent with NemoClaw's security layer. The inference routing means you can use Nemotron locally for privacy-sensitive work or route to the cloud when you need more power.

**Team deployments with controlled egress.** For teams running shared agents, the network policy system gives you a way to define exactly which external services the agent can reach. New destinations get surfaced for approval. No silent data exfiltration.

**Telegram-bridged assistants.** OpenClaw already supports Telegram integration. With NemoClaw, you can expose an agent over Telegram while keeping it sandboxed. Remote access to a secured agent, not an open pipe to your machine.

## NemoClaw vs OpenClaw

Here's how the two compare side by side:

| Feature | OpenClaw | NemoClaw |
|---|---|---|
| Sandbox isolation | None (runs on host) | Landlock + seccomp + netns |
| Network control | No restrictions | Policy-based allowlist, hot-reloadable |
| Filesystem restrictions | Full host access | Limited to /sandbox and /tmp |
| Inference routing | Direct API calls | Intercepted and routed through NVIDIA cloud |
| Process security | Standard OS permissions | seccomp syscall filtering, no privilege escalation |
| Installation complexity | Single install script | Single install script + onboard wizard |
| Monitoring (TUI) | None | Real-time dashboard with operator approvals |
| Cloud deploy | Manual setup | One-click Brev deploy or CLI |

The short version: OpenClaw gives you the AI agent. NemoClaw gives you the AI agent inside a sandbox you control.

## Is NemoClaw Ready for Production?

NVIDIA is calling this an early-stage alpha, and that's the right framing. NemoClaw works, the security layers are real, and the installation is genuinely simple. But it's early. There are rough edges. <a href="https://github.com/NVIDIA/NemoClaw/issues" target="_blank" rel="noopener noreferrer">The GitHub issues</a> show people hitting setup problems on WSL2, macOS support is still being tracked, and some policy configurations need more documentation.

What's useful right now: if you're running OpenClaw agents and you want actual isolation without building your own container setup, NemoClaw gets you there in one command. The protection layers are meaningful. Network namespaces, Landlock, and seccomp are battle-tested Linux security primitives, not custom sandboxing hacks.

What's not ready yet: production team deployments, cross-platform support, and some of the more advanced policy configurations. Give it time.

The <a href="https://github.com/NVIDIA/NemoClaw" target="_blank" rel="noopener noreferrer">source is on GitHub</a>, and OpenShell itself is fully open source. The hardware is not vendor-specific either. NemoClaw runs on any Linux machine, not just NVIDIA GPUs. If you've been waiting for a security layer to drop before [going all-in on autonomous agents](/blog/pm-ships-with-claude-code), this is a solid starting point.
