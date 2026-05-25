# Lesson 4 — First Ubuntu Server Safety

Book 2 starts here.

The goal is not to rent a server immediately.

The goal is to understand the safety boundary before one machine starts managing another machine.

## The Book 2 pivot

Book 2 is LAN-first.

That means the preferred practice setup is:

```text
Ubuntu client machine -> private home network -> Ubuntu server machine
```

Examples:

- desktop to laptop,
- laptop to old desktop,
- desktop to mini PC,
- host machine to Ubuntu VM.

A rented VPS can still be useful later, but it is not required for the core learning path.

## Why this matters

A public VPS adds risk too early:

- billing,
- public SSH exposure,
- DNS confusion,
- domain and HTTPS timing,
- provider-specific dashboards,
- root login mistakes,
- accidental long-running resources.

A LAN server lab keeps the learning path calmer:

- no paid cloud account,
- no DigitalOcean requirement,
- no AWS requirement,
- no router port forwarding,
- no public DNS,
- no public server exposure,
- no real customer data.

You can still learn real server skills.

## Client and server

In Book 2 language:

- the **client** is the machine where you type the connecting command,
- the **server** is the machine that accepts the connection.

A local laptop can act like a practice server even though it is not a true cloud VPS.

That distinction is important: the command-line habit transfers, but public production hosting responsibilities come later.

## Safe commands for this stage

From the repo root, run:

```bash
make verify
make doctor
make book2-doctor
make book2-check-inputs
make book2-lan-ip-help
```

These commands are safe. They do not connect to a server, install packages, change firewall rules, open router ports, deploy files, or write receipts.

## Local settings

Book 2 includes a template:

```text
book2/env.example
```

For your own machine, copy it to an ignored local file:

```bash
cp book2/env.example .env.local
```

Then edit `.env.local` later when a lesson asks you to do so.

Do not commit `.env.local`.

## What this lesson does not do

This lesson does not require a VPS yet.

No Book 2 command in this scaffold connects to a server.

This lesson does not ask you to run:

- package-install commands,
- firewall-open commands,
- SSH commands,
- DNS commands,
- HTTPS commands,
- router port-forwarding steps, or
- provider dashboard steps.

Those actions belong in later lessons, after the boundary is clear.

## Proof-first checkpoint

At the end of this lesson, you should be able to explain:

1. Which machine is the client?
2. Which machine will be the server?
3. Are both machines on the same private LAN?
4. Why are we avoiding router port forwarding?
5. Why are we not starting with DigitalOcean or AWS?
6. Which files contain safe Book 2 guidance?
7. Which commands are safe and non-mutating?

This is the right first step for Book 2: learn the boundary before crossing it.
