from django.contrib.messages import constants as messages
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'drj@01r%3(lk-h89cg=oaksu*&f%bvnw66n*2r7sn@!1*u2*j^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]


# Application definition

DEFAULT_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DJANGO_APPS = [
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
]

PROJECT_APPS = [
    'products',
    'users',
    'core',
    'shops',
    'orders',
    'cart',
    'compare',
]

THIRD_PARTY_APPS = [
    'django_summernote',
    'crispy_forms',
    'social_django',
    'django_extensions',
    'import_export',
    'robots',
    'djsingleton',
]

INSTALLED_APPS = DEFAULT_APPS + DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shops.context_processors.categories',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# For custom user model
AUTH_USER_MODEL = "users.User"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'staticfiles'),
]
STATIC_ROOT = os.path.join(BASE_DIR,'static')

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# login details
LOGIN_REDIRECT_URL = 'core:dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'


# social auth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
]

SOCIAL_AUTH_FACEBOOK_KEY = '201191034510296'  # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'b72b0d0d81947670575456e1767bb260'  # Facebook App Secret

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']


# Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '492673619534-pjt4fm43m7njlnof82tluofsdusfvfe7.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'iPjP2v_j8OCPBSTQgYtpHdga'


# cart session id
CART_SESSION_ID = "cart"

SITE_ID = 1

# Messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}


CART_SESSION_ID = 'cart'
COMPARE_SESSION_ID = 'compare'

# SECURE_SSL_REDIRECT = True





JAZZMIN_SETTINGS = {
    # title of the window
    'site_title': 'Trade Nepal Online',

    # Title on the brand, and the login screen (19 chars max)
    'site_header': 'Trade Nepal Online',

    # Welcome text on the login screen
    'welcome_sign': 'Welcome to Trade Nepal Online Admin panel',

    # Copyright on the footer
    'copyright': 'Trade Nepal Online Pvt. Ltd',


    # Whether to display the side menu
    'show_sidebar': True,
    'custom_css': 'css/admin.css',

}
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    "accent": "accent-lightblue",
    "navbar": "navbar-primary navbar-dark",
    "no_navbar_border": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True
}

X_FRAME_OPTIONS = 'SAMEORIGIN'

try:
    from .local_settings import *
except ImportError:
    pass

try:
    from .dev_settings import *
except ImportError:
    pass