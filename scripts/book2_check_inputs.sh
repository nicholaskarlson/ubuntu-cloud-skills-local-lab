#!/usr/bin/env bash
set -euo pipefail

echo "Ubuntu Cloud Skills Book 2 input check"
echo

echo "Purpose: validate local Book 2 settings without connecting to another machine."
echo "This command does not use ssh, install packages, change firewall rules, open router ports, deploy files, write receipts, or require a paid cloud account."
echo

mode="${BOOK2_MODE:-lan}"
host="${BOOK2_HOST:-}"
user="${BOOK2_USER:-}"
port="${BOOK2_SSH_PORT:-22}"
domain="${BOOK2_DOMAIN:-}"
public_url="${BOOK2_PUBLIC_URL:-}"
identity_file="${BOOK2_IDENTITY_FILE:-}"

is_private_ipv4() {
  local ip="$1"
  [[ "$ip" =~ ^10\.([0-9]{1,3}\.){2}[0-9]{1,3}$ ]] && return 0
  [[ "$ip" =~ ^192\.168\.([0-9]{1,3}\.)[0-9]{1,3}$ ]] && return 0
  [[ "$ip" =~ ^172\.(1[6-9]|2[0-9]|3[0-1])\.([0-9]{1,3}\.)[0-9]{1,3}$ ]] && return 0
  return 1
}

ok=0
warn=0

case "$mode" in
  lan)
    echo "OK: BOOK2_MODE=lan"
    ;;
  vps)
    echo "INFO: BOOK2_MODE=vps is recognized, but the core Book 2 path remains LAN-first."
    ;;
  *)
    echo "ERROR: BOOK2_MODE must be 'lan' or 'vps'. Current value: $mode" >&2
    ok=1
    ;;
esac

if [[ -z "$host" ]]; then
  echo "INFO: BOOK2_HOST is not set. That is fine until a later SSH lesson."
  warn=1
else
  if [[ "$mode" == "lan" ]]; then
    if is_private_ipv4 "$host"; then
      echo "OK: BOOK2_HOST looks like a private LAN IPv4 address."
    else
      echo "WARN: BOOK2_HOST is set but does not look like a private IPv4 LAN address."
      echo "      For the LAN-first path, expected examples are 10.x.x.x, 192.168.x.x, or 172.16-31.x.x."
      warn=1
    fi
  else
    echo "INFO: BOOK2_HOST is set for non-LAN mode."
  fi
fi

if [[ -z "$user" ]]; then
  echo "INFO: BOOK2_USER is not set. That is fine until a later SSH lesson."
  warn=1
elif [[ "$user" == "root" ]]; then
  echo "WARN: BOOK2_USER is root. The learning path should prefer a normal non-root user."
  warn=1
else
  echo "OK: BOOK2_USER is set and is not root."
fi

if [[ "$port" =~ ^[0-9]+$ ]] && (( port >= 1 && port <= 65535 )); then
  echo "OK: BOOK2_SSH_PORT is a valid port number."
else
  echo "ERROR: BOOK2_SSH_PORT must be an integer from 1 to 65535." >&2
  ok=1
fi

if [[ -n "$domain" ]]; then
  echo "INFO: BOOK2_DOMAIN is set. Domains are optional and not needed for the LAN-first path."
else
  echo "OK: BOOK2_DOMAIN is blank for the LAN-first path."
fi

if [[ -n "$public_url" ]]; then
  echo "INFO: BOOK2_PUBLIC_URL is set. Public URLs belong to a later optional publishing path."
else
  echo "OK: BOOK2_PUBLIC_URL is blank for the LAN-first path."
fi

if [[ -n "$identity_file" ]]; then
  if [[ -f "$identity_file" ]]; then
    echo "OK: BOOK2_IDENTITY_FILE points to an existing local file. Do not commit private key files."
  else
    echo "WARN: BOOK2_IDENTITY_FILE is set but the file was not found."
    warn=1
  fi
else
  echo "OK: BOOK2_IDENTITY_FILE is blank. Later lessons may use your default SSH key setup."
fi

echo
if [[ "$ok" -ne 0 ]]; then
  echo "ERROR: Book 2 input check found invalid settings." >&2
  exit 1
fi

if [[ "$warn" -ne 0 ]]; then
  echo "OK with notes: Book 2 input check completed with setup reminders."
else
  echo "OK: Book 2 input check completed."
fi
