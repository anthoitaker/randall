DOCKER_COMPOSE = docker-compose -f docker-compose.dev.yml
DRUN = $(DOCKER_COMPOSE) run --rm
MANAGE = $(DRUN) --entrypoint python randall manage.py
FABFILE = tools/fabric/fabfile.py
PYLINT = tools/lint/pylint.sh

.PHONY: up exec lint test migrate migrations build push fab-update fab-deploy

up:
		$(DOCKER_COMPOSE) up -d randall

exec:
		$(DOCKER_COMPOSE) exec randall /bin/bash

lint:
		$(DRUN) --entrypoint /bin/bash randall $(PYLINT)

test:
		$(MANAGE) test

migrate:
		$(MANAGE) migrate

migrations:
		$(MANAGE) makemigrations

build:
		docker build -t anthoitaker/randall .

push:
		docker push anthoitaker/randall

fab-update:
		$(DRUN) fabric -f $(FABFILE) update

fab-deploy:
		$(DRUN) fabric -f $(FABFILE) deploy
