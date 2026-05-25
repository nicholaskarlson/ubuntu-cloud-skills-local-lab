#!/usr/bin/env bash
set -euo pipefail

echo "Ubuntu Cloud Skills Book 2 doctor"
echo

echo "Purpose: safe LAN-first Book 2 readiness checks."
echo "This command does not connect by SSH, install packages, change firewall rules, open router ports, deploy files, write receipts, or require a paid cloud account."
echo

missing=0
check_file() {
  local path="$1"
  if [[ -e "$path" ]]; then
    echo "OK: $path"
  else
    echo "ERROR: missing $path" >&2
    missing=1
  fi
}

echo "Book 2 LAN-first files:"
check_file docs/book2-companion-code.md
check_file docs/book2-lan-server-lab.md
check_file docs/book2-server-safety-boundary.md
check_file docs/book2-vps-checklist.md
check_file lessons/04-first-ubuntu-server-safety.md
check_file book2/env.example
check_file scripts/book2_doctor.sh
check_file scripts/book2_check_inputs.sh
check_file scripts/book2_lan_ip_help.sh
check_file tests/test_book2_lan_pivot.py

if [[ "$missing" -ne 0 ]]; then
  echo
  echo "ERROR: Book 2 doctor found missing files." >&2
  exit 1
fi

echo

echo "Tool readiness for future Book 2 work:"
if command -v git >/dev/null 2>&1; then
  echo "OK: git -> $(git --version)"
else
  echo "WARN: git not found"
fi

if command -v python3 >/dev/null 2>&1; then
  echo "OK: python3 -> $(python3 --version)"
else
  echo "ERROR: python3 not found" >&2
  exit 1
fi

if command -v ssh >/dev/null 2>&1; then
  echo "OK: ssh client command is available"
else
  echo "INFO: ssh client command not found. Install OpenSSH client before later SSH lessons."
fi

if command -v curl >/dev/null 2>&1; then
  echo "OK: curl -> $(curl --version | head -n 1)"
else
  echo "INFO: curl not found. Install it before later server smoke checks."
fi

echo

echo "Book 2 default posture:"
echo "OK: default mode is LAN-first."
echo "OK: DigitalOcean is not required."
echo "OK: AWS is not required."
echo "OK: router port forwarding is not part of the beginner path."
echo "OK: a rented VPS is optional later, not the starting point."

echo

echo "Next safe commands:"
echo "  make book2-check-inputs"
echo "  make book2-lan-ip-help"
echo "  Read docs/book2-lan-server-lab.md"
echo

echo "OK: Book 2 doctor completed"
