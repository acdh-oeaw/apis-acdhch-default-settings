import os
import re
from typing import Any, Dict

from django.core.management.utils import get_random_secret_key
import dj_database_url

if os.environ.get("SENTRY_DSN"):
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=os.environ.get("SENTRY_DSN"),
        integrations=[
            DjangoIntegration(),
        ],
        environment="production",
        # we disable tracing by default
        enable_tracing=False,

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
    )

SECRET_KEY = os.environ.get("SECRET_KEY", get_random_secret_key())

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(os.path.join(__file__, "../")))
)

# Application definition
# put apis_override_select2js at the beginning of the list
# to make its static files weigh more than from the other apps
INSTALLED_APPS = [
    "apis_override_select2js",
    "dal",
    "dal_select2",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "crispy_bootstrap4",
    "django_filters",
    "django_tables2",
    "rest_framework",
    "apis_ontology",
    "apis_acdhch_default_settings",
    "apis_core.apis_relations",
    "apis_core.apis_entities",
    "apis_core.apis_metainfo",
    "apis_core.apis_vocabularies",
    "apis_core.generic",
    "apis_core.core",
    "rest_framework.authtoken",
    "drf_spectacular",
]

# https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_X_FORWARDED_HOST
USE_X_FORWARDED_HOST = True
# https://docs.djangoproject.com/en/5.0/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# drf-spectacular settings
# https://drf-spectacular.readthedocs.io/en/latest/settings.html
SPECTACULAR_SETTINGS: Dict[str, Any] = {
    "TITLE": "APIS generic API",
    "DESCRIPTIOPN": "Provides access to the main APIS data-model endpoints.",
    "LICENSE": {"name": "MIT License", "url": "https://www.mit.edu/~amini/LICENSE.md"},
    "VERSION": "0.13",
    "DEFAULT_GENERATOR_CLASS": 'apis_core.generic.generators.CustomSchemaGenerator'
}

# django-csp settings
# https://django-csp.readthedocs.io/en/latest/migration-guide.html#migration-guide-chapter
CSP_DEFAULT_SRC = (
    "'self'",
    "'unsafe-inline'",
    "cdnjs.cloudflare.com",
    "cdn.jsdelivr.net",
    "fonts.googleapis.com",
    "ajax.googleapis.com",
    "cdn.rawgit.com",
    "*.acdh.oeaw.ac.at",
    "unpkg.com",
    "fonts.gstatic.com",
    "cdn.datatables.net",
    "code.highcharts.com",
    "*.acdh-dev.oeaw.ac.at",
    "*.acdh.oeaw.ac.at",
    "openstreetmap.org",
    "*.openstreetmap.org",
)
CSP_FRAME_SRC = ("sennierer.github.io",)

# django-crispy-forms settings
# https://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap4"

# django-rest-framework settings
# https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 50,
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.DjangoModelPermissions",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        # "drf_spectacular.contrib.django_filters.DjangoFilterBackend",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE
MIDDLEWARE = [
    "allow_cidr.middleware.AllowCIDRMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "csp.middleware.CSPMiddleware",
    "crum.CurrentRequestUserMiddleware",
]

# https://docs.djangoproject.com/en/5.0/ref/settings/#root-urlconf
ROOT_URLCONF = "apis_acdhch_default_settings.urls"

# https://docs.djangoproject.com/en/5.0/ref/settings/#templates
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
            ]
        },
    }
]

# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = "en"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")
STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = "/media/"

# django-tables2 setting
# https://django-tables2.readthedocs.io/en/latest/pages/custom-rendering.html#available-templates
DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap4.html"

# apis-core-rdf settings
APIS_BASE_URI = "TO CHANGE"
APIS_MIN_CHAR = 0
APIS_NEXT_PREV = True
APIS_LIST_VIEWS_ALLOWED = False
APIS_DETAIL_VIEWS_ALLOWED = False
SHARED_URL = "https://shared.acdh.oeaw.ac.at/"

# django-allow-cidr settings
# https://github.com/mozmeao/django-allow-cidr
ALLOWED_CIDR_NETS = ["10.0.0.0/8", "127.0.0.0/8"]

# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# https://github.com/jazzband/dj-database-url
DATABASES = {'default': dj_database_url.config(default='sqlite:///db.sqlite3', conn_max_age=600)}

# https://docs.djangoproject.com/en/5.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
if os.environ.get("PUBLIC_URL"):
    ALLOWED_HOSTS.append(re.sub(r"https?://", "", os.environ.get("PUBLIC_URL")))

if os.environ.get("ALLOWED_HOSTS"):
    ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")

# setting of apis_acdhch_default_settings.ldapauth
if os.environ.get("AUTH_LDAP_USER_LIST", False):
    AUTH_LDAP_SERVER_URI = os.environ.get("ARZ_AUTH_LDAP_SERVER_URI")
    AUTH_LDAP_USER_DN_TEMPLATE = "%(user)s@oeaw.ads"

    # https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-AUTHENTICATION_BACKENDS
    AUTHENTICATION_BACKENDS = [
        "apis_acdhch_default_settings.ldapauth.CustomLDAPBackend",
        "django.contrib.auth.backends.ModelBackend",
    ]

# https://docs.djangoproject.com/en/5.0/howto/logging/
# setup logging to log everything to stdout
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    'formatters': {
       'verbose': {
           'format': '%(asctime)s %(name)-6s %(levelname)-8s %(message)s',
       },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}

# Our deployment infrastructure sets the GITLAB_ENVIRONMENT_URL to the
# repository from which the instance is deployed. Lets reuse this
# information to set the repository url in APIS
if os.environ.get("GITLAB_ENVIRONMENT_URL"):
    GIT_REPOSITORY_URL = os.environ.get("GITLAB_ENVIRONMENT_URL")
