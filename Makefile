.PHONY: help verify check-env up down logs ps lab-smoke lab-smoke-receipt receipt-version receipt-note clean

help:
	@echo "Targets:"
	@echo "  make verify             - run local repo checks; does not require Docker"
	@echo "  make check-env          - check required local tools"
	@echo "  make up                 - start the local web lab"
	@echo "  make ps                 - show running containers"
	@echo "  make logs               - show web container logs"
	@echo "  make lab-smoke          - start lab and confirm local web page responds"
	@echo "  make lab-smoke-receipt  - run smoke test and save a local receipt"
	@echo "  make down               - stop the local web lab"
	@echo "  make receipt-version    - save Docker version receipt"
	@echo "  make receipt-note       - write a manual receipt from stdin"
	@echo "  make clean              - stop lab and remove local temp files"

verify:
	python3 -m unittest discover -s tests -v

check-env:
	bash scripts/check_env.sh

up:
	docker compose up -d

ps:
	docker compose ps

logs:
	docker compose logs web

lab-smoke:
	docker compose up -d
	sleep 2
	curl -fsS http://localhost:8080 > /tmp/ubuntu-cloud-skills-local-lab.html
	grep -q "Ubuntu Cloud Skills Local Lab" /tmp/ubuntu-cloud-skills-local-lab.html
	docker compose ps
	@echo "OK: local web lab responded at http://localhost:8080"

lab-smoke-receipt:
	bash -c 'set -euo pipefail; tmp="$$(mktemp)"; { \
	  echo "Local web smoke-test receipt"; \
	  echo; \
	  date -Iseconds; \
	  echo; \
	  echo "Command: make lab-smoke-receipt"; \
	  echo; \
	  docker compose up -d; \
	  sleep 2; \
	  curl -fsS http://localhost:8080 > /tmp/ubuntu-cloud-skills-local-lab.html; \
	  grep -q "Ubuntu Cloud Skills Local Lab" /tmp/ubuntu-cloud-skills-local-lab.html; \
	  docker compose ps; \
	  echo; \
	  echo "OK: local web lab responded at http://localhost:8080"; \
	} | tee "$$tmp"; bash scripts/write_receipt.sh local-web-smoke < "$$tmp"; rm -f "$$tmp"'

down:
	docker compose down

receipt-version:
	mkdir -p receipts
	{ \
	  echo "Docker version receipt"; \
	  echo; \
	  date -Iseconds; \
	  echo; \
	  docker --version; \
	  docker compose version; \
	} > receipts/docker-version.txt
	@echo "Wrote receipts/docker-version.txt"

receipt-note:
	@echo "Type a short receipt note, then press Ctrl-D:"
	bash scripts/write_receipt.sh manual-note

clean:
	docker compose down
	rm -rf .tmp .cache
	rm -f /tmp/ubuntu-cloud-skills-local-lab.html
