# Book 2 LAN Server Lab

Book 2 starts with a local-network server lab, not a paid cloud provider.

The reader should be able to learn real server habits with two machines on the same private network:

```text
client machine -> home router / private LAN -> server machine
```

This gives the reader a VPS-style command-line experience without a VPS bill, public SSH exposure, router port forwarding, public DNS, or a domain name.

## Why LAN first?

LAN-first is safer for beginners because it avoids several early risks:

- surprise cloud billing,
- public internet exposure,
- provider dashboard changes,
- domain and DNS confusion,
- HTTPS certificate timing issues,
- root login mistakes on public machines,
- router port-forwarding mistakes, and
- support problems caused by different VPS provider interfaces.

The durable skills still transfer:

- SSH concepts,
- hostnames and IP addresses,
- users and permissions,
- service inspection,
- logs,
- firewall posture,
- deployment habits,
- smoke tests,
- backup and restore,
- safe receipts, and
- cleanup.

## Recommended hardware paths

Good Book 2 server-machine options include:

- a spare Ubuntu laptop,
- an old Ubuntu desktop,
- a mini PC,
- a Linux VM,
- a Raspberry Pi-style Linux machine, or
- a rented VPS only after the LAN path is understood.

The repo should not assume one hardware vendor, ISP, router, cloud provider, or paid account.

## Network boundary

The beginner path should stay inside the private LAN.

Avoid in the main path:

- opening port 22 to the internet,
- opening ports 80 or 443 from a home router,
- dynamic DNS as a required step,
- production hosting from a personal laptop,
- real customer downloads from a home network,
- payment handling from a home server, and
- router port forwarding.

Those topics can be discussed later as advanced warnings or optional migration paths.

## Safe setup idea

The likely manuscript flow is:

1. Choose a client machine and a server machine.
2. Confirm both machines are on the same private network.
3. Install or enable the SSH server on the server machine manually.
4. Understand `ssh.service` and possible socket activation.
5. Allow SSH on the server firewall only after understanding the scope.
6. Find the server machine LAN IP.
7. Connect from the client machine in a later explicit SSH lesson.
8. Save only safe proof receipts.

This drop-in does not perform those setup steps automatically.

## Safe commands in this repo

Current safe commands:

```bash
make book2-doctor
make book2-check-inputs
make book2-lan-ip-help
```

These commands inspect local files, explain required inputs, and print helpful guidance. They do not connect by SSH, install packages, change UFW, deploy files, or write receipts.

## Local environment example

Use `book2/env.example` as a template for local-only settings.

For your private machine, copy it outside version control, for example:

```bash
cp book2/env.example .env.local
```

Then edit `.env.local` for your own LAN lab. Do not commit `.env.local`.

The default mode is:

```text
BOOK2_MODE=lan
```

A future optional VPS path may use:

```text
BOOK2_MODE=vps
```

The core Book 2 path should remain LAN-first.
