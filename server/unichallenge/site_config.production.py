import os
import firebase_admin
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

ALLOWED_HOSTS = ['*']

MEDIA_URL = '/media/'
MEDIA_ROOT = '/media/'

CSRF_TRUSTED_ORIGINS = ['.unichallenge.gr', 'localhost']
CSRF_COOKIE_DOMAIN = 'channel.unichallenge.gr'

MAX_ATTEMPTS = 3
MAX_RUN_TIME = 600

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'uknow',
        'USER': 'root',
        'PASSWORD': os.environ['MARIADB_PASSWORD'],
        'HOST': 'mariadb'
    }
}

# Sentry
sentry_sdk.init(
    dsn=os.environ['SENTRY_DSN'],
    integrations=[DjangoIntegration()]
)

# Firebase
firebase_admin.initialize_app(
    firebase_admin.credentials.Certificate('/firebase.json')
)
