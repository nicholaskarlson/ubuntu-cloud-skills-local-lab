#!/usr/bin/env bash
set -euo pipefail

echo "Ubuntu Cloud Skills Local Lab environment check"
echo

echo "Required local tools:"
command -v git >/dev/null
echo "OK: git -> $(git --version)"

command -v python3 >/dev/null
echo "OK: python3 -> $(python3 --version)"

command -v docker >/dev/null
echo "OK: docker -> $(docker --version)"

docker compose version >/dev/null
echo "OK: docker compose -> $(docker compose version)"

echo
echo "Optional useful tool:"
if command -v curl >/dev/null; then
  echo "OK: curl -> $(curl --version | head -n 1)"
else
  echo "WARN: curl not found; install it if you want to run local web smoke checks."
fi

echo
echo "OK: environment check completed"
