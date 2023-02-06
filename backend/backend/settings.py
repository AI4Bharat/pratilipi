"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import logging
import logging.handlers
import os
from pathlib import Path
from dotenv import load_dotenv
from distutils.util import strtobool
from datetime import timedelta

load_dotenv()

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(strtobool(os.getenv("DEBUG", "True")))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "*" if DEBUG else os.getenv("SECRET_KEY")

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "0.0.0.0"]
if DEBUG:
    ALLOWED_HOSTS.append("*")

if os.getenv("ALLOWED_HOSTS", ""):
    additional_hosts = os.getenv("ALLOWED_HOSTS")
    for additional_host in additional_hosts.split(","):
        ALLOWED_HOSTS.append(additional_host)

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "djoser",
    "import_export",
    "rest_framework",
    "drf_yasg",
    "organization",
    "project",
    "video",
    "task",
    "transcript",
    "translation",
    "users",
    "voiceover",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if not DEBUG:
    STATIC_ROOT = BASE_DIR / "static"

# Email Settings
EMAIL_BACKEND = "django_smtp_ssl.SSLEmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = 465
EMAIL_HOST_USER = os.getenv("SMTP_USERNAME")
EMAIL_HOST_PASSWORD = os.getenv("SMTP_PASSWORD")
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")

DOMAIN = "chitralekha.ai4bharat.org"
SITE_NAME = "chitralekha.ai4bharat.org"

DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "forget-password/confirm/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "users/auth/users/username/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "users/auth/users/activation/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SERIALIZERS": {},
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "BLACKLIST_AFTER_ROTATION": False,
    "REFRESH_TOKEN_LIFETIME": timedelta(days=20),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=100),
}

ENABLE_CORS = bool(strtobool(os.getenv("ENABLE_CORS", "False")))
CSRF_COOKIE_SECURE = False

if ENABLE_CORS:
    INSTALLED_APPS.append("corsheaders")
    MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")

    CORS_ALLOW_ALL_ORIGINS = True
    CSRF_COOKIE_SECURE = False
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_CREDENTIALS = True

    CSRF_TRUSTED_ORIGINS = [
        "http://localhost:*",  # for localhost (Developlemt)
    ]
    CUSTOM_CSRF_TRUSTED_ORIGINS = os.getenv("CORS_TRUSTED_ORIGINS", "")
    if CUSTOM_CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS.extend(CUSTOM_CSRF_TRUSTED_ORIGINS.split(","))

AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ]
}

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "one_two",
        "USER": os.getenv("POSTGRES_DB_USERNAME"),
        "PASSWORD": os.getenv("POSTGRES_DB_PASSWORD"),
        "HOST": os.getenv("POSTGRES_DB_HOST"),
        "PORT": os.getenv("POSTGRES_DB_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Calcutta"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "users.User"

# set LOG LEVEL as INFO
LOGLEVEL = "INFO"

# Make a new directory for logs
Path(BASE_DIR / "logs").mkdir(exist_ok=True)

# Define the list of formatters
formatters = {
    "console": {
        "()": "backend.logger.ConsoleFormatter",
        "format": "({server_time}) {console_msg}",
        "style": "{",
    },
    "file": {
        "format": "{levelname} ({asctime}) [{module}:{process}|{thread}] {message}",
        "style": "{",
    },
    "csvfile": {
        "format": "{levelname},{asctime},{module},{process},{thread},{message}",
        "style": "{",
    },
}

# Define the list of handlers
handlers = {
    "console": {
        "level": LOGLEVEL,
        "class": "logging.StreamHandler",
        "formatter": "console",
    }
}

# enable LOGGING
LOGGING = "true"

# If logging is enabled, add file handlers
if LOGGING == "true":
    handlers["file"] = {
        "level": "WARNING",
        "class": "logging.handlers.RotatingFileHandler",
        "filename": os.path.join(BASE_DIR, "logs/default.log"),
        "formatter": "file",
        "maxBytes": 1024 * 1024 * 3,
        "backupCount": 2,
    }
    handlers["file"] = {
        "level": "INFO",
        "class": "logging.handlers.RotatingFileHandler",
        "filename": os.path.join(BASE_DIR, "logs/default.log"),
        "formatter": "file",
        "maxBytes": 1024 * 1024 * 3,
        "backupCount": 2,
    }

# Define logger configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": formatters,
    "handlers": handlers,
    "loggers": {
        "": {
            "level": LOGLEVEL,
            "handlers": handlers.keys(),
        },
        "django": {
            "handlers": [],
        },
        "django.server": {"propagate": True},
    },
}
