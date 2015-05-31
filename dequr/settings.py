"""
Django settings for dequr project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from unipath import Path
BASE_DIR = Path(__file__).ancestor(2)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$=#j301saw%gz+q@%xk0$4rqsk!b=0hqznd(@ma3t4_)qlunxu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

DJANGO_APP = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
THIRD_PARTY_APP = (
    'social.apps.django_app.default',
    'formtools',
)

LOCAL_APP = (
    'apps.category',
    'apps.company',
    'apps.complaint',
    'apps.general',
    'apps.users',
)

INSTALLED_APPS = DJANGO_APP + THIRD_PARTY_APP + LOCAL_APP

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'dequr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('templates')],
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

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.google.GoogleOAuth2',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_FACEBOOK_KEY = '1573536116267749'
SOCIAL_AUTH_FACEBOOK_SECRET = '0160f7f0bbd27956969edc7ed08cbc5e'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_TWITTER_KEY = 'Gvs0S9GVgs0dLTIK0gqNgkLAl'
SOCIAL_AUTH_TWITTER_SECRET = 'DeSXhystfnu8QxZ3iC9si5kMsIjSrTYYHRfYf4Hi39XBZys8B8'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '218181437660-1da1jq9u1momipeufg9rhvk69lqkp4uc.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'KOraASPufazoIhqKrWDhMoMO'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'apps.users.pipeline.get_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'apps.users.pipeline.user_details',
)

AUTH_USER_MODEL = 'users.User'

WSGI_APPLICATION = 'dequr.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
#instanciaprueba.cqminbbwlacp.us-west-2.rds.amazonaws.com:3306
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dequr',
        'USER': 'dequr',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '3306',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
if DEBUG:
    STATICFILES_DIRS = [BASE_DIR.child('static')]
else:
    STATIC_ROOT = BASE_DIR.child('static')
    STATICFILES_DIRS = []

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
