"""
Django settings for kkhospital project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import posixpath

try:
   from config import *
except ImportError:
   pass

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y#p2efh3_3b9e!mioi97elz5cgx-u6v@&6d!0+4d3pt_=fw-w9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'app',
    # 'bootstrapform',

    'allauth',
    'allauth.account',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kkhospital.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'app'),
            os.path.join(BASE_DIR, 'app', 'templates'),
            os.path.join(BASE_DIR, 'app', 'templates', 'allauth'),
        ],
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

WSGI_APPLICATION = 'kkhospital.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'NAME': MSSQL_DATABASE,
        'ENGINE': 'sql_server.pyodbc',
        'HOST': MSSQL_HOST,
        'USER': MSSQL_USERNAME,
        'PASSWORD': MSSQL_PASSWORD,
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase', # This is where you put the name of the db file.
                 # If one doesn't exist, it will be created at migration time.
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'min_length': 9,
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    # 'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'), )
LOGIN_URL = 'home'
LOGIN_REDIRECT_URL = 'home'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
# EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
# ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQURIED = True
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
ACCOUNT_USERNAME_MIN_LENGTH = 3

ACCOUNT_FORMS = {
    'login': 'app.forms.Login_Mod',
    'signup': 'app.forms.Signup_Mod',
}
