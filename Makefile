.PHONY: homono
honmono:
	docker run --name honmono -d redis:latest

get-homono-console: honmono
	docker exec -it honmono redis-cli

.PHONY: rm-homono
rm-homono:
	docker stop honmono && docker rm honmono
