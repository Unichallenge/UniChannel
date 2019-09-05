from fabric import Connection, task

@task
def deploy(c):
    c.run('deploy-remote')

@task
def deploy_remote(c):
    c.run('git fetch; git reset --hard origin/$(git symbolic-ref --short HEAD)')

    print('--- Building static assets ---')
    c.run('rm -rf app/static')
    c.run('cp -r server/static app/static')

    print('--- Building new containers ---')
    c.run('PATH=$PATH docker-compose build')

    print('--- Stopping old instances ---')
    c.run('PATH=$PATH docker-compose down --remove-orphans')

    print('--- Running pending migrations ---')
    c.run('PATH=$PATH docker-compose up -d mariadb')
    c.run('PATH=$PATH docker-compose run uwsgi python manage.py migrate')

    print('--- Starting new instances ---')
    c.run('PATH=$PATH docker-compose up -d')

    print('=== UniChannel was deployed successfully! ===')


@task
def logs(c):
    c.run('logs-remote')

@task
def logs_remote(c):
    c.run('PATH=$PATH docker-compose logs -f')