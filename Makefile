.PHONY: help verify up down logs ps receipt-version clean

help:
	@echo "Targets:"
	@echo "  make verify           - run local repo checks"
	@echo "  make up               - start the local web lab"
	@echo "  make ps               - show running containers"
	@echo "  make logs             - show web container logs"
	@echo "  make down             - stop the local web lab"
	@echo "  make receipt-version  - save Docker version receipt"
	@echo "  make clean            - stop lab and remove local temp files"

verify:
	python3 -m unittest discover -s tests -v

up:
	docker compose up -d

ps:
	docker compose ps

logs:
	docker compose logs web

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

clean:
	docker compose down
	rm -rf .tmp .cache
