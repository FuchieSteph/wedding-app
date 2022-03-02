from pathlib import Path
from django.utils.translation import gettext_lazy as _

import os

BASE_DIR = Path(__file__).resolve().parent.parent
SITE_ROOT = os.path.dirname(os.path.realpath(__name__))
PROJECT_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f!n_jw=(@zejc5+lrkxzm%40d7df(#sf8a(t&nj5fqnc(tf_el'

# Application definition
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
MEDIA_URL = '/media/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'theme/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

#STATICFILES_DIRS=[(os.path.join(PROJECT_DIR,'theme/static'))]

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

ROSETTA_LOGIN_URL = "/members/login"

LANGUAGES = (
    ('en', _('Anglais')),
    ('fr', _('Français')),
)

LOCALE_PATHS = ( os.path.join(PROJECT_DIR, 'locale'), )

USE_I18N = True