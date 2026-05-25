# Book 2 Server Safety Boundary

Book 2 introduces a second Ubuntu machine. That is a useful milestone, but it changes the risk profile.

Book 1 is local on one machine.

Book 2 should be LAN-first by default.

That means Book 2 can teach server habits without immediately creating a public server.

## Core boundary

Book 2 should not hide server actions behind mysterious automation.

A reader should understand:

- what machine is the client,
- what machine is the server,
- what host or LAN IP they are using,
- what account they are using,
- whether a command is local or remote,
- whether a command only inspects,
- whether a command changes server state,
- whether anything is exposed outside the private LAN,
- where logs are stored,
- where backups are stored,
- what receipts are safe to keep, and
- how to stop or clean up what they started.

## LAN-first boundary

The core path should not require:

- DigitalOcean,
- AWS,
- any paid VPS,
- a domain name,
- public DNS,
- router port forwarding,
- public SSH exposure,
- customer data,
- payment handling, or
- production uptime.

A rented VPS can be an optional migration path later, after the LAN lab is understood.

## Secrets and private data

Never commit or save:

- SSH private keys,
- passphrases,
- server passwords,
- cloud provider tokens,
- DNS provider tokens,
- customer data,
- raw access logs containing sensitive query strings,
- credential screenshots, or
- billing screenshots with private account details.

Receipts should prove the workflow without storing private access.

Good receipts can include:

```text
LAN SSH check passed
server smoke check passed
service active
backup archive created
restore drill completed
cleanup checklist reviewed
```

Bad receipts include anything that grants access or exposes private account information.

## Public exposure checklist

Before any later Book 2 workflow makes a site public, the reader should be able to answer:

1. Am I still inside my private LAN, or am I exposing something publicly?
2. What server am I using?
3. What user am I logged in as?
4. Which port is open?
5. What service is listening?
6. What content is being served?
7. Is this an IP-only LAN test, a public-IP test, or a domain-based HTTPS test?
8. How do I stop the service?
9. How do I back up and restore the site files?
10. If this is a paid VPS, how do I destroy the paid resource when finished?
11. What receipt can I safely keep?

## Provider portability

Book 2 should not become a DigitalOcean-only, AWS-only, or provider-specific course.

Provider-specific examples may appear later, but the core repo should remain provider portable:

- Ubuntu LTS server,
- SSH,
- standard Linux users and permissions,
- simple web serving,
- standard logs,
- standard backup archives,
- clear cleanup reminders.

## Mutating commands

Commands that change a server should be introduced later and should be obvious from their names.

Prefer names such as:

```text
book2-deploy-public
book2-backup-public
book2-restore-public
```

Avoid names that hide the action.

Inspection commands should come first:

```text
book2-doctor
book2-check-inputs
book2-lan-ip-help
```

Later connection commands should be explicit:

```text
book2-ssh-check
book2-server-info
```

## Teaching rule

The reader should never wonder:

```text
Did that command just change my server?
```

If a command changes anything, say so before the command is used.
