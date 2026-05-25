# Book 2 Server Safety Boundary

Book 2 introduces a real Ubuntu server. That is a useful milestone, but it also changes the risk profile.

Book 1 is local. Book 2 can be public.

That means Book 2 must be slower, clearer, and more explicit.

## Core boundary

Book 2 should not hide public-server actions behind mysterious automation.

A reader should understand:

- what account they are using,
- what host they are connecting to,
- whether a command is local or remote,
- whether a command only inspects,
- whether a command changes server state,
- whether a command exposes something publicly,
- where logs are stored,
- where backups are stored,
- what receipts are safe to keep, and
- how to stop or clean up what they started.

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
server smoke check passed
Caddy service active
backup archive created
restore drill completed
cleanup checklist reviewed
```

Bad receipts include anything that grants access or exposes private account information.

## Public exposure checklist

Before a Book 2 workflow makes a site public, the reader should be able to answer:

1. What server am I using?
2. What user am I logged in as?
3. Which port is open?
4. What service is listening?
5. What content is being served?
6. Is this an IP-only test or a domain-based HTTPS test?
7. How do I stop the service?
8. How do I back up and restore the site files?
9. How do I destroy the paid VPS if I am finished?
10. What receipt can I safely keep?

## Provider portability

Book 2 should not become a DigitalOcean-only, AWS-only, or provider-specific course.

Provider-specific examples may appear later, but the core repo should remain provider portable:

- Ubuntu LTS server,
- SSH,
- standard Linux users and permissions,
- a simple web server,
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
book2-ssh-check
book2-server-info
```

## Teaching rule

The reader should never wonder:

```text
Did that command just change my server?
```

If a command changes anything, say so before the command is used.
