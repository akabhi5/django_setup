from .base import *
from dotenv import dotenv_values


SECRET_KEY = dotenv_values('.env')['SECRET_KEY']

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
