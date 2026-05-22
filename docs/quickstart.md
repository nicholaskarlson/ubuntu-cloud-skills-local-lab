# Quickstart

This quickstart proves that the local lab can run a tiny website from your own machine.

The core path does not require a paid cloud account. It runs locally with Docker and Docker Compose.

## 1. Check the repository

Run the lightweight repository checks:

```bash
make verify
```

This confirms that the expected files are present and that the local contract tests pass.

This step does not require Docker to be running.

## 2. Check your local tools

Run the environment check:

```bash
make check-env
```

You should see version information for:

- Git
- Python 3
- Docker
- Docker Compose

The script also checks for `curl`, which is used by the local web smoke test.

## 3. Start the local web lab

Start the local web server container:

```bash
make up
```

Then open this address in your browser:

```text
http://localhost:8080
```

You should see a page titled:

```text
Ubuntu Cloud Skills Local Lab
```

That page is served from:

```text
public/index.html
```

through the web container defined in:

```text
compose.yaml
```

## 4. Confirm the running container

Show the local lab container status:

```bash
make ps
```

You should see the web service running and port `8080` mapped to the container's web port.

## 5. Run the local smoke test

Run the automated local web smoke test:

```bash
make lab-smoke
```

This command:

1. starts the web container,
2. fetches `http://localhost:8080`,
3. confirms that the expected page title is present,
4. prints the container status, and
5. reports success.

Expected final message:

```text
OK: local web lab responded at http://localhost:8080
```

## 6. Save a Docker version receipt

Save a local version receipt:

```bash
make receipt-version
```

This writes:

```text
receipts/docker-version.txt
```

That file is intentionally ignored by Git because receipts are local evidence, not source code.

A sample receipt is provided at:

```text
receipts/samples/docker-version-example.txt
```

## 7. Inspect logs

View the web container logs:

```bash
make logs
```

Logs are part of the proof-first habit. They help you see what the server actually did.

## 8. Stop the lab

Stop and remove the local lab container and network:

```bash
make down
```

You can also run:

```bash
make clean
```

to stop the lab and remove temporary local files created by the smoke test.

## Safety notes

Do not commit secrets.

Do not put any of these into this repository:

- passwords
- API tokens
- SSH private keys
- cloud credentials
- payment credentials
- private customer data

This lab is designed to teach cloud-style skills locally before you decide whether to use a paid VPS or cloud provider.

## Troubleshooting

### Port 8080 is already in use

Another program may already be using port `8080`.

Stop the other program, or edit `compose.yaml` to use a different local port.

For example:

```yaml
ports:
  - "8081:80"
```

Then open:

```text
http://localhost:8081
```

### Docker is installed but not running

Start Docker, then try again:

```bash
make check-env
```

### The page does not appear

Try these checks:

```bash
make ps
make logs
curl -fsS http://localhost:8080
```

Then stop and restart the lab:

```bash
make down
make up
```

### You want to reset the lab

Run:

```bash
make clean
make up
```

Then open:

```text
http://localhost:8080
```
