"""
Django settings for bouncer project.

Generated by 'django-admin startproject' using Django 2.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from bouncer.db import DB
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3xd=qp4y_2jlwa6#-cf^_krn8654!ad7ggy#95#d0)p(7dqe2i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['*']

<<<<<<< HEAD
=======

>>>>>>> rebase
# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'rest_framework',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bouncer.urls'

WSGI_APPLICATION = 'bouncer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = DB.config(DEBUG)

# Email Settings
EMAIL_HOST = config("EMAIL_HOST", default="smtp.dummy.net")
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="dummy@gmail.com")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="dummy-password")
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# Global configurations for rest framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # Changed authentication class
        'rest_framework_simplejwt.authentication.JWTTokenUserAuthentication',
    ],
}

# Password Hasher
PASSWORD_HASSHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PawordHasher'
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
