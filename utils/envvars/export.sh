#!/usr/bin/env bash

touch .env
echo "DEBUG=$DEBUG" >> .env
echo "SECRET_KEY=$SECRET_KEY" >> .env
echo "REMOTE_HOST=$REMOTE_HOST" >> .env
echo "REMOTE_USER=$REMOTE_USER" >> .env
echo "REMOTE_APP_DIR=$REMOTE_APP_DIR" >> .env
echo "SSH_AUTH_SOCK=/ssh-agent" >> .env
echo "SENTRY_DSN=$SENTRY_DSN" >> .env
