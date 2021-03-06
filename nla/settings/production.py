"""
Django settings for nla project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

from nla.settings.default import *

SECRET_KEY = os.environ['NLA_SECRET_KEY']
EXPONEA_TOKEN = os.environ['NLA_EXPONEA_TOKEN']
EXPONEA_TRACK_REGISTRATION = True

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
