import os
from fabric.api import cd, env, put, run

REMOTE_HOST = os.getenv('REMOTE_HOST')
REMOTE_USER = os.getenv('REMOTE_USER')
REMOTE_APP_DIR = os.getenv('REMOTE_APP_DIR')

env.hosts = ['{user}@{host}'.format(user=REMOTE_USER, host=REMOTE_HOST)]

def update():
    with cd(REMOTE_APP_DIR):
        put('docker-compose.yml', 'deploy.yml')

def deploy():
    with cd(REMOTE_APP_DIR):
        run('docker-compose -f deploy.yml pull')
        run('docker-compose -f deploy.yml up -d randall')
