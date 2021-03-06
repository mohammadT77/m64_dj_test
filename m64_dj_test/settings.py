"""
Django settings for m64_dj_test project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.


BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u7%x0ziy!b=7g(%qudbv+1xix5v9ccrf477zr$)fo3iv9@84tx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'core',
    'app1',
    'app2',
    'app3',
    'app4',
    'app5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'm64_dj_test.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'm64_dj_test.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_URL = 'login_view'
LOGIN_REDIRECT_URL = '/auth/profile'
AUTH_USER_MODEL = 'core.User'

MESSAGE_TAGS = {
    44: 'akbar',
}
# from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 3,
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'detail-formatter': {
            'format': '{levelname}|{asctime}|{funcName}|{filename}|{lineno}|{module}:{message}',
            'style': '{'
        },
        'brief-formatter': {
            'format': '%(levelname)s: %(message)s',
            'style': '%'
        },
    },
    'filters': {
        'min-len-filter': {
            '()': 'core.logging_filters.MinLenFilter',
        },
        'a-start-filter': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': lambda record: not record.getMessage().startswith('a'),
        }
    },
    'handlers': {
        'my-console-handler': {
            'class': 'logging.StreamHandler',  # Console print!
        },
        'my-file-handler': {
            'class': 'logging.FileHandler',  # Write file!
            'filename': BASE_DIR / 'a-test.log',
            'formatter': 'brief-formatter',
        },
        'operator-handler': {
            'class': 'logging.FileHandler',  # Write file!
            'filename': BASE_DIR / 'operators.log',
            'formatter': 'detail-formatter',
            'filters': ['min-len-filter', 'a-start-filter']
        }
    },
    'root': {
        'handlers': ['my-console-handler'],
        'level': 'INFO',
    },
    'loggers': {
        'staff': {
            'handlers': ['my-file-handler'],
            'level': 'WARNING',
            'propagate': False,  # Default: True
        },
        'staff.operator': {
            'handlers': ['operator-handler'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}