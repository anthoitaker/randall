DOCKER_COMPOSE = docker-compose -f docker-compose.dev.yml
DRUN = $(DOCKER_COMPOSE) run --rm

.PHONY: run inspect build push fab-update fab-deploy

run:
		$(DRUN) --name randall-service --service-ports randall

inspect:
		docker exec -it randall-service /bin/bash

build:
		docker build -t anthoitaker/randall .

push:
		docker push anthoitaker/randall

fab-update:
		$(DRUN) --name randall-fab fabric update

fab-deploy:
		$(DRUN) --name randall-fab fabric deploy
