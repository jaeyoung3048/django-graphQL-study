from mysite.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'graphQL',
        'USER': 'root',
        'PASSWORD': get_secret('MYSQL_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
