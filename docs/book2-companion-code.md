# Book 2 Companion Code

Book 2 is planned as:

**Your First Ubuntu Cloud Server**

The goal is to move the Book 1 proof-first habits to a real Ubuntu VPS without losing the safety model.

Book 2 should teach a careful reader to:

- connect with SSH,
- work as a non-root user,
- keep the server updated,
- understand firewall posture before public exposure,
- serve the same small creator site from an Ubuntu server,
- use Caddy or another simple web server intentionally,
- run smoke checks,
- inspect server logs,
- save safe receipts,
- back up the deployed site,
- restore from a backup, and
- clean up paid resources when finished.

## Planned release tag

When Book 2 companion code is complete and aligned with the manuscript, it should receive this stable tag:

```text
book2-v1.0.0
```

Until that tag exists, Book 2 work on `main` or development branches should be treated as evolving.

## Current scaffold status

This repo currently includes the Book 2 planning scaffold only.

That means:

- the Book 2 safety boundary is documented,
- the VPS readiness checklist is documented,
- the first Book 2 lesson scaffold exists,
- repository tests confirm those files are present, and
- no live VPS automation is included yet.

This is intentional. Public server work should begin only after the reader path and safety boundary are clear.

## Reader path

Book 2 should preserve the Book 1 rhythm:

```text
inspect -> run one small step -> verify -> save safe evidence -> clean up
```

The main difference is that Book 2 introduces a real server, so the project must be more conservative about:

- public IP addresses,
- domains,
- firewall settings,
- SSH keys,
- logs,
- receipts,
- backups,
- restore drills, and
- provider billing.

## What this scaffold does not do

This scaffold does not:

- create a VPS,
- connect to a VPS,
- install packages on a server,
- change firewall rules,
- deploy a public website,
- configure DNS,
- request HTTPS certificates,
- store server credentials, or
- require a paid cloud account.

Those steps belong in later, explicit Book 2 drop-ins.

## Expected future command surface

Later Book 2 increments may add commands such as:

```bash
make book2-doctor
make book2-check-inputs
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
