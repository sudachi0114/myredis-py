.PHONY: homono
honmono:
	docker compose up -d

.PHONY: clean
clean:
	docker compose down
