DOCKER_COMPOSE = docker-compose -f docker-compose.dev.yml
DRUN = $(DOCKER_COMPOSE) run --rm
FABFILE = utils/fabric/fabfile.py
PYLINT = utils/lint/pylint.sh

.PHONY: run inspect build push fab-update fab-deploy

run:
		$(DRUN) --name randall-service --service-ports randall

inspect:
		docker exec -it randall-service /bin/bash

lint:
		$(DRUN) --name randall-lint --entrypoint $(PYLINT) randall

test:
		$(DRUN) --name randall-test --entrypoint python randall manage.py test

build:
		docker build -t anthoitaker/randall .

push:
		docker push anthoitaker/randall

fab-update:
		$(DRUN) --name randall-fab fabric -f $(FABFILE) update

fab-deploy:
		$(DRUN) --name randall-fab fabric -f $(FABFILE) deploy
