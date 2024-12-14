"""
Django settings for w3indonesia project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yw(kdds#31ig@jw6q^dy@f5o14u3sz0y8ai3tx3)a7_bpf793b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['w3indonesia.com', 'www.w3indonesia.com', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'tutorial',
    'home',
    'ckeditor',
    'ckeditor_uploader',
    'news',
    'bootcamp',
    'scholarship',
    'jobs',
    'contact',
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

ROOT_URLCONF = 'w3indonesia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
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

WSGI_APPLICATION = 'w3indonesia.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'w3indonesia_db',
        'USER': 'endo',
        'PASSWORD': 'Merdeka2021_',
        'HOST': 'localhost',
        'PORT': '5432', 
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# STATIC_URL adalah URL di mana static files dapat diakses

STATIC_URL = '/static/'

# STATIC_ROOT adalah folder tempat static files dikumpulkan saat menjalankan `collectstatic`
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Direktori untuk static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            # Group 1 - Basic formatting
            ['Bold', 'Italic', 'Underline', 'Strike', '-', 'Link', 'Unlink', '-', 'CodeSnippet'],
            
            # Group 2 - List and indentation
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent'],
            
            # Group 3 - Alignment and other styling
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', '-', 'Font', 'FontSize', '-', 'TextColor', 'BGColor'],
            
            # Group 4 - Insert and media
            ['Image', 'Table', 'HorizontalRule', 'Smiley', '-', 'SpecialChar'],
            
            # Group 5 - Undo, redo, and source view
            ['Undo', 'Redo', '-', 'Source'],

            # Group 6 - Markdown-related tools
            ['Blockquote', 'Styles'],
        ],
        'height': 300,
        'width': '100%',
        'extraPlugins': ['codesnippet'],  # Ensure the CodeSnippet plugin is loaded
        'codeSnippet_theme': 'monokai',  # Optional: Use a syntax highlighting theme for code snippets
        'enterMode': 2,  # CKEDITOR.ENTER_BR for <br> line breaks instead of <p> tags
        'shiftEnterMode': 1,  # CKEDITOR.ENTER_P for <p> tags on shift-enter
        'allowedContent': True,  # Allows all HTML tags and attributes
        'extraAllowedContent': 'pre code',  # Allow pre/code tags specifically
    },
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'media')