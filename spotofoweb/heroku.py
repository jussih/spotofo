
from spotofoweb.settings import *

import dj_database_url

DATABASES['default'] = dj_database_url.config()
DATABASES['default']['CONN_MAX_AGE'] = 500

DEBUG = os.environ.get('DEBUG', False)

SECRET_KEY = os.environ.get('SECRET_KEY','')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*',]

SPOTOFO_CLIENT_SECRET = os.environ.get('SPOTOFO_CLIENT_SECRET','')
SPOTOFO_CLIENT_ID = os.environ.get('SPOTOFO_CLIENT_ID','')
SPOTOFO_REDIRECT_URI = os.environ.get('SPOTOFO_REDIRECT_URI','')

INSTALLED_APPS += (
  'raven.contrib.django.raven_compat',
)

RAVEN_CONFIG = {
  'dsn': os.environ.get('SENTRY_DSN', ''),
  'release': os.environ.get('HEROKU_SLUG_COMMIT', None),
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry', 'console'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s %(data)s'
        },
    },
    'filters': {
      'default': {
        '()': 'logging_helpers.Filter',
      },
    },
    'handlers': {
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

