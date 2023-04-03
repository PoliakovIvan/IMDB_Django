from .base import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'IMDBdb',
        'USER': 'postgres',
        'PASSWORD': '111',
        'HOST': 'db',
        'PORt': '5432',
    }
}