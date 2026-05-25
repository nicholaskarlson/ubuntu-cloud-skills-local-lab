# Book 2 Companion Code

Book 2 is now planned as:

**Your First Ubuntu Server Lab**

Working subtitle:

**Practice VPS-style skills safely at home before renting a cloud server.**

The goal is to move the Book 1 proof-first habits to a second Ubuntu machine on a private LAN before asking readers to rent a VPS, configure DNS, expose SSH publicly, or use provider-specific services.

## Default Book 2 path

The default path is LAN-first:

```text
Ubuntu client machine -> private home network -> Ubuntu server machine
```

Examples of server machines:

- an Ubuntu laptop,
- an old Ubuntu desktop,
- a mini PC,
- a Raspberry Pi-style Linux box running Ubuntu or another Linux distribution,
- an Ubuntu VM, or
- a rented VPS only as an optional later migration path.

Book 2 should teach a careful reader to:

- understand the difference between client and server,
- identify a private LAN IP address,
- prepare for SSH without exposing the machine to the public internet,
- work as a non-root user where appropriate,
- keep the server updated,
- understand firewall posture before opening services,
- serve the same small creator site from an Ubuntu server,
- run smoke checks,
- inspect server logs,
- save safe receipts,
- back up the deployed site,
- restore from a backup, and
- clean up or shut down what they started.

## Planned release tag

When Book 2 companion code is complete and aligned with the manuscript, it should receive this stable tag:

```text
book2-v1.0.0
```

Until that tag exists, Book 2 work on `main` or development branches should be treated as evolving.

## Current scaffold status

This repo currently includes the Book 2 LAN-first pivot and safe readiness layer.

That means:

- the Book 2 safety boundary is documented,
- the LAN server lab guide is documented,
- the optional VPS checklist is documented,
- the first Book 2 lesson scaffold exists,
- a local non-secret environment example exists,
- safe Book 2 readiness and input-check commands exist,
- repository tests confirm those files are present, and
- no live SSH, deployment, firewall mutation, DNS, HTTPS, router port-forwarding, or provider automation is included yet.

This is intentional. Server work should begin locally and explicitly before any public exposure enters the codebase.

For backward compatibility with the first scaffold, this remains true: no live VPS automation is included yet.

## Reader path

Book 2 should preserve the Book 1 rhythm:

```text
inspect -> run one small step -> verify -> save safe evidence -> clean up
```

The main difference is that Book 2 introduces a second machine, so the project must be more conservative about:

- hostnames,
- IP addresses,
- SSH keys,
- firewall settings,
- logs,
- receipts,
- backups,
- restore drills,
- public exposure, and
- provider billing only if the reader later chooses a VPS.

## What this scaffold does not do

This scaffold does not:

- create a VPS,
- require DigitalOcean,
- require AWS,
- require a domain name,
- open router ports,
- connect to another machine by SSH,
- install packages on a server,
- change firewall rules,
- deploy a public website,
- configure DNS,
- request HTTPS certificates,
- store server credentials, or
- require a paid cloud account.

Those steps belong in later, explicit Book 2 drop-ins.

## Current safe command surface

This layer adds safe, non-mutating Book 2 commands:

```bash
make book2-doctor
make book2-check-inputs
make book2-lan-ip-help
```

These commands do not connect to any server.

## Expected future command surface

Later Book 2 increments may add commands such as:

```bash
make book2-ssh-check
make book2-server-info
make book2-deploy-dry-run
make book2-deploy-public
make book2-smoke
make book2-logs-receipt
make book2-backup-public
make book2-restore-public
make book2-cleanup-checklist
make book2-verify
```

Those commands should be added gradually, with tests and documentation, and with dry-run or inspect-first behavior wherever possible.
