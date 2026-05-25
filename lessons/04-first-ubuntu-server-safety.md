# Lesson 4: First Ubuntu Server Safety

Book 1 stayed local. Book 2 begins the move to a real Ubuntu server.

This lesson is a safety and planning lesson. It does not require a VPS yet.

## Goal

By the end of this lesson, you should understand the difference between:

```text
local lab work
```

and

```text
public server work
```

A local lab is forgiving. A public server needs more care.

## The Book 1 habit still applies

Book 1 taught this rhythm:

```text
inspect -> run -> verify -> save safe evidence -> clean up
```

Book 2 keeps the same rhythm, but the commands become more serious because some of them may affect a real server.

## Local or remote?

Before running a command in Book 2, ask:

1. Does this run on my local machine?
2. Does this run on the server?
3. Does this only inspect?
4. Does this change files, packages, services, firewall rules, or public exposure?
5. Can I undo it?
6. What safe receipt would prove it worked?

This question matters more than memorizing commands.

## What not to save

Do not put these in Git or receipts:

- SSH private keys,
- passwords,
- passphrases,
- provider tokens,
- raw secrets,
- private customer data,
- credential screenshots,
- billing screenshots with private account details.

A safe receipt should prove the step without exposing access.

## Planned Book 2 path

Book 2 should move in small steps:

1. Confirm the repo is healthy.
2. Read the server safety boundary.
3. Prepare a disposable Ubuntu VPS.
4. Confirm SSH access.
5. Work as a non-root user.
6. Update packages.
7. Inspect firewall posture.
8. Serve the creator site.
9. Run a smoke test.
10. Inspect logs.
11. Save safe receipts.
12. Back up the deployed site.
13. Practice restore.
14. Clean up paid resources when finished.

## First commands for this scaffold

For now, use only safe local inspection commands:

```bash
make verify
make doctor
make repo-map
make series-status
```

No Book 2 command in this scaffold connects to a server.

## Stop point

Stop here until the next Book 2 drop-in adds explicit readiness checks.

The next code increment should still be conservative: it should check local inputs and explain what would be needed for a VPS, not mutate a remote server.
