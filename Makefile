
.PHONY: run inspect build push

run:
		docker-compose run --rm --name randall-service --service-ports randall

inspect:
		docker exec -it randall-service /bin/bash

build:
		docker build -t anthoitaker/randall .

push:
		docker push anthoitaker/randall
