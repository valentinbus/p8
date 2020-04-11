from . import *
import os
import sentry_sdk
import raven
from sentry_sdk.integrations.django import DjangoIntegration


SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['34.240.239.202']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'p8',
        'USER': 'vbus',
        'PASSWORD': os.getenv('PASSWORD_DB'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

sentry_sdk.init(
    dsn="https://ae6e3668b316442788bf6ca54d69b25a@sentry.io/4140914",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
