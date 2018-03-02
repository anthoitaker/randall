
.PHONY: run

run:
		docker-compose run --rm --name randall-service --service-ports randall
