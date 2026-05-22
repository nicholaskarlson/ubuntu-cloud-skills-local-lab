#!/usr/bin/env bash
set -euo pipefail

echo "Ubuntu Cloud Skills Local Lab stack inspection"
echo

echo "Repository:"
pwd
echo

echo "Local site files:"
find public -maxdepth 1 -type f -print | sort

echo
echo "Compose services:"
docker compose ps || true

echo
echo "Local web address:"
echo "http://localhost:8080"

echo
echo "Tip: run 'make up' to start the lab and 'make logs' to inspect web logs."
