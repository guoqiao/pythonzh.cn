import os
from os.path import dirname, abspath
from path import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(dirname(abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'si^7v_12e*!alrw55=9g#s^)q9sixng03dy=f^7c&mzoxew92j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
SITE_ID = 1
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'taggit',
    'django_comments',
    'notifications',
    'autoslug',
    'users',
    'forum',
    'replies',
    'categories',
    'covers',
    'bootstrap_pagination',
    'captcha',
    'simplemde',
    'pagedown',
]

COMMENTS_APP = 'replies'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
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

WSGI_APPLICATION = 'wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_ADAPTER = 'users.adapter.AccountAdapter'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_FORMS = {
    'login': 'users.forms.LoginForm',
    'signup': 'users.forms.SignupForm',
}
ACCOUNT_USERNAME_MIN_LENGTH = 3
ACCOUNT_USERNAME_VALIDATORS = 'users.validators.ASCIIUsernameValidator'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MARKDOWN_EXTENSIONS = [
    'markdown.extensions.fenced_code',
    'markdown.extensions.tables',
    'markdown.extensions.codehilite',
]

MARKDOWN_EXTENSION_CONFIGS = {}

BLEACH_ALLOWED_TAGS = ['a', 'img', 'br', 'strong', 'b', 'code', 'pre',
                       'p', 'div', 'del', 'dl', 'dt', 'dd', 'em', 'span', 'h1', 'h2', 'h3', 'h4',
                       'h5', 'h6', 'blockquote', 'ul', 'ol', 'tr', 'th', 'td',
                       'hr', 'li', 'u', 'embed', 's', 'table', 'thead', 'tbody',
                       'caption', 'small', 'q', 'sup', 'sub', ]

BLEACH_ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title'],
    'abbr': ['title'],
    'acronym': ['title'],
    'div': ['class'],
    'span': ['class'],
    '*': ['id'],
    'img': ['src'],
}

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/users/login/'

NOTIFICATION_TEMPLATES = {
    '@': 'notifications/mention.html',
    'reply': 'notifications/reply.html',
}

USE_PAGEDOWN = False

SHELL_PLUS_PRE_IMPORTS = (
    ('datetime', '*'),
    ('path', 'Path'),
)
