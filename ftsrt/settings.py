# -*- coding: utf-8 -*-
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
#CMS
gettext = lambda s: s
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

LANGUAGES = [
    ('ru', 'Russian'),
]

ADMINS = (
    ('ildar', 'nurildar9@gmail.com'),
)

MANAGERS = ADMINS

DEFAULT_CHARSET = 'utf8'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bl3000_ftsrt',
        'USER': 'bl3000',
        'PASSWORD': 'P@$$wordBarsik9',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru-RU'

SITE_ID = 2

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'files', 'media')

STATIC_ROOT = os.path.join(PROJECT_DIR, 'files', "static")
 # os.path.join(os.path.expanduser('~'), 'domains/ftsrt.bl3000.myjino.ru/static/')

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'files', "static"),
    os.path.join(PROJECT_DIR, '..', 'administration', 'static'),
    os.path.join(PROJECT_DIR, '..', 'picasagallery', 'static'),
)



# List of finder classes that know how to find static files in
# various locations.


ADMIN_MEDIA_PREFIX = '/static/admin/'
# Make this unique, and don't share it with anybody.
SECRET_KEY = '93j!wn_-g-b5tpn-2s42pgzzu@3qm!63jcpbuieve--(pi$9rk'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'pybb.middleware.PybbMiddleware',
)

ROOT_URLCONF = 'ftsrt.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ftsrt.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'pybb.context_processors.processor',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
    os.path.join(PROJECT_DIR, '..', 'picasagallery', 'templates'),
    os.path.join(PROJECT_DIR, '..', 'administration', 'templates'),
)
#CMS_USE_TINYMCE = False
CMS_TEMPLATES = (
    ('base_cms.html', 'base_cms'),
    ('template_1.html', 'testcms')
)
#forum profile control
AUTH_PROFILE_MODULE = 'pybb.Profile'
#PYBB_ENABLE_SELF_CSS=True
PYBB_ENABLE_ANONYMOUS_POST = True
PYBB_ANONYMOUS_USERNAME = 'Аноним'
PYBB_ATTACHMENT_ENABLE = True

#PICASA
PICASAGALLERY_USER = 'ftsrt.kazan@gmail.com'
# 'ftsrt.kazan@gmail.com'
PICASAGALLERY_PHOTO_THUMBSIZE = '128'
PICASAGALLERY_PHOTO_IMGMAXSIZE = '648'
PICASAGALLERY_ALBUM_THUMBSIZE = '160c'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'picasagallery',
    #costumise admin
    'grappelli',
    'django.contrib.admin',

    # 'django.contrib.admindocs',
    'cms',
    'menus',
    'mptt',
    'south',
    'cms.plugins.text',
    'tinymce',
    'cms.plugins.picture',
    'cms.plugins.link',
    'cms.plugins.file',
    'cms.plugins.snippet',
    'cms.plugins.video',
    #'cms.plugins.googlemap',
    'cms.plugins.video',
    'sekizai',
    'easy_news',
    'registration',
    'pybb',
    'pytils',
    'sorl.thumbnail',
    'pure_pagination',
    'administration',
    #    'pinax-theme-bootstrap',
    #    'django-forms-bootstrap',
    #    'pinax-theme-bootstrap-account',
)

# registration
ACCOUNT_ACTIVATION_DAYS = 2
AUTH_USER_EMAIL_UNIQUE = True

#testing mail server
#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 1025
#EMAIL_HOST_USER = ""
#EMAIL_HOST_PASSWORD = ""
#EMAIL_USE_TLS = False
#DEFAULT_FROM_EMAIL = 'testing@example.com'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'nurildar9@gmail.com'
EMAIL_HOST_PASSWORD = 'n93u26r01'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'nurildar9@gmail.com'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
