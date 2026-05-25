#!/usr/bin/env bash
set -euo pipefail

echo "Ubuntu Cloud Skills Book 2 LAN IP help"
echo

echo "Purpose: show safe commands for finding the private LAN IP of the future server machine."
echo "This command does not change your network, open firewall ports, connect by SSH, or expose anything publicly."
echo

cat <<'TEXT'
Run these commands on the machine that will act as the Book 2 server.

Simple option:

  hostname -I

More detailed IPv4 option:

  ip -4 addr show

Look for a private IPv4 address, commonly starting with one of these ranges:

  10.x.x.x
  192.168.x.x
  172.16.x.x through 172.31.x.x

Example:

  10.0.0.113

Do not use router port forwarding for the beginner path.
Do not open SSH to the public internet for the beginner path.
Do not commit your local IP address if it appears in private notes you do not want published.

After a later lesson asks you to configure local inputs, copy:

  cp book2/env.example .env.local

Then edit .env.local locally. That file is ignored by Git.
TEXT
