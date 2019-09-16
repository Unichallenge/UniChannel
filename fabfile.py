from fabric import Connection, task

@task
def deploy(c):
    c.run('deploy-remote')

@task
def deploy_remote(c):
    # Make sure we are at the correct branch
    c.run('git fetch; git reset --hard origin/master')

    # Build static
    c.run('rm -rf app/static')
    c.run('cp -r server/static app/static')

    # All the Docker stuff
    c.run('PATH=$PATH docker-compose build')
    c.run('PATH=$PATH docker-compose down --remove-orphans')
    c.run('PATH=$PATH docker-compose up -d mariadb')
    c.run('PATH=$PATH docker-compose run uwsgi python manage.py migrate')
    c.run('PATH=$PATH docker-compose up -d')

    print('=== UniChannel was deployed successfully! ===')


@task
def logs(c):
    c.run('logs-remote')

@task
def logs_remote(c):
    c.run('PATH=$PATH docker-compose logs -f')