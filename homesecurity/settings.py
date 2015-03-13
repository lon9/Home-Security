"""
Django settings for homesecurity project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import LANGUAGE_CODE, TIME_ZONE,\
    STATICFILES_DIRS, STATIC_ROOT, STATICFILES_STORAGE
import dj_database_url
from socket import gethostname
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATICFILES_STORAGE='whitenoise.django.GzipManifestStaticFilesStorage'

hostname = gethostname()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@71lbdkiwo_wf!)h0og^#z022$48#7=_9ldccg^(=zb&219640'

# SECURITY WARNING: don't run with debug turned on in production!
#デバッグモードをするか判定
if 'VAIO' in hostname:
    DEBUG = True
    TEMPLATE_DEBUG = True
else:
    DEBUG = False
    TEMPLATE_DEBUG = False
    ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrapform',
    'cms',
    'gunicorn',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'homesecurity.urls'

WSGI_APPLICATION = 'homesecurity.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
#データベースをどれにするか判定
if 'VAIO' in hostname:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),   
        }
    }
else:
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config()
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT='staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)