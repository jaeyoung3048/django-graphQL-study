from mysite.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'graphQL_test',
        'USER': 'root',
        'PASSWORD': get_secret('MYSQL_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
