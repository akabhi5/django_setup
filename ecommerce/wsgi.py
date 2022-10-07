import os

from dotenv import dotenv_values

from django.core.wsgi import get_wsgi_application


settings_path = 'ecommerce.settings'
if dotenv_values('.env')['ENV'] == 'PRODUCTION':
    settings_path += '.production'
else:
    settings_path += '.local'


os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_path)

application = get_wsgi_application()
