"""
Django settings for bookmarked project.

Generated by 'django-admin startproject' using Django 1.11.15.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'logic'
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookmarked.urls'

TEMPLATE_BASE = 'templates'
TEMPLATE_PATH = os.path.join(BASE_DIR, TEMPLATE_BASE)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_PATH],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookmarked.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'


if os.environ.get('ENVIRONMENT') == None:
    MONGO_URL = 'localhost'
    MONGO_PORT = str(27017)
    MONGO_URI = "mongodb://" + MONGO_URL + ":" + MONGO_PORT + "/"
    DEBUG = True
    SECRET_KEY = 'abcdef'
elif os.environ.get('ENVIRONMENT') == 'production':
    MONGO_USER = os.environ['MONGO_USER']
    MONGO_PASSWORD = os.environ['MONGO_PASSWORD']
    MONGO_URL = os.environ['MONGO_URL']
    MONGO_PORT = os.environ['MONGO_PORT']
    MONGO_DBNAME = os.environ['MONGO_DBNAME']
    MONGO_URI = "mongodb://" + MONGO_USER + ":" + MONGO_PASSWORD + "@" + MONGO_URL + ":" + MONGO_PORT + "/" + MONGO_DBNAME
    DEBUG = False
    SECRET_KEY = os.environ['SECRET_KEY']
