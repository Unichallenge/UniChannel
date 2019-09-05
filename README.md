
# UniChannel

## Development

To setup your development environment, after cloning, do:

```bash
cd app
# Setup the Angular application
npm install
cd ..

# Setup the Django app
cd server
virtualenv
source venv/bin/activate
pip install -r requirements.txt
```

You will also need to populate your `server/unichallenge/site_config.py` file with:

* The database connection information about your local MySQL installation.
* The Firebase configuration for your app.
* the `DEBUG = True` flag, to indicate this is a dev environment.

You should also most probably run all migrations and create a superuser:

```bash
cd server;
python manage.py migrate
python manage.py createsuperuser
```

After all this, you can simply run these commands (in seperate terminals):

```bash
cd server; source venv/bin/activate; python manage.py runserver
cd app; yarn run serve
```

And **voila!** The app is now running at [http://localhost:4200](http://localhost:4200)!

## Production

### Deploy the app

To deploy the app, run while in its directory:

```bash
fab -h deployer@<host> deploy
```

The script will take care of building the images, running any pending migrations and (re)starting the apps.

### Setup the app

Ensure **Docker**, **Docker Compose**, **Python >3.6** and **Fabric >2** are installed.

Using the `root` user, execute:

```bash
# Or substitute with your own directory
mkdir /usr/unichannel
# Create the unichannel user
useradd unichannel
# Create the deployer user
useradd deployer
# Make unichannel the owner
chown -R unichannel:unichannel /usr/unichannel
# Allow the deployer to run Docker commands and access the new directory
usermod -a -G docker deployer
usermod -a -G unichannel deployer
```

Now using the `unichannel` user:

```bash
# Initialize the repository
cd /usr/unichannel
git clone git@github.com:Unichallenge/unichannel.git 

# Create the user SSH keys and allow other users to make deploys
cd
ssh-keygen
mkdir .ssh; chmod 700 .ssh
cat > .ssh/authorized_keys
```

The `.ssh/authorized_keys` file should have the following format:

```bash
command="cd /usr/unichannel; fab $SSH_ORIGINAL_COMMAND",no-pty ssh-rsa # ...
```

This will ensure people with deploy access can **only execute** `fabric` tasks.

Next up, create the `/usr/unichannel/unichannel` directory and place the `firebase.json` private key file you
generated from Firebase. More about how to create it [here](https://firebase.google.com/docs/admin/setup#initialize_the_sdk).

You must also create the `/usr/unichannel/.env` file containing all the environment variables
necessary for your application to run. This should contain the following:

* `UID` = The UID of the `unichallenge` user.
* `GID` = The GID of the `unichallenge` user.
* `MARIA_PASS` = A unique password for your MariaDB installation.
* `SENTRY_DSN` = The Sentry DSN for error logging.

Compose will automatically take these into consideration when setting up its environment.

You can now try and deploy the app itself!
