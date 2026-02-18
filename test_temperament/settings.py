import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _

# --- PATHS ---
BASE_DIR = Path(__file__).resolve().parent.parent
LOCALE_PATHS = [BASE_DIR / 'locale']

# --- SECURITY ---
SECRET_KEY = 'django-insecure-3+&=ccik4#pp2%^19u3e72v)^60!g^13j8e4+w*=d#an-#v-qn'
DEBUG = False
ALLOWED_HOSTS = ['*']

# --- APPS ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quizz',
]

# --- MIDDLEWARE ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Esențial pentru traduceri
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- TEMPLATES ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n', # Esențial pentru variabilele de limbă
            ],
        },
    },
]

# --- DATABASE ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- AUTHENTICATION ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LOGIN_REDIRECT_URL = '/quizz/rezultate/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

# --- INTERNATIONALIZATION ---
LANGUAGE_CODE = 'ro'  # Limba default
LANGUAGES = [
    ('ro', _('Română')),
    ('fr', _('Français')),
]

USE_I18N = True
USE_TZ = True
LANGUAGE_COOKIE_NAME = 'django_language'

# --- STATIC FILES ---
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# --- MISC ---
ROOT_URLCONF = 'test_temperament.urls'
WSGI_APPLICATION = 'test_temperament.wsgi.application'