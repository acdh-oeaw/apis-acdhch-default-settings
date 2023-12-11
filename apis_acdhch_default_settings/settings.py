import os
import re
from typing import Any, Dict

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

# We fall back to a DEFAULT_SECRET_KEY, but you should
# override this using an environment variable!
DEFAULT_SECRET_KEY = "a+nkut46lzzg_=ul)zrs29$u_6^*)2by2mjmwn)tqlgw)_at&l"
SECRET_KEY = os.environ.get("SECRET_KEY", DEFAULT_SECRET_KEY)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(os.path.join(__file__, "../")))
)

SHARED_URL = "https://shared.acdh.oeaw.ac.at/"

PROJECT_NAME = "apis"
PROJECT_SHARED = "https://shared.acdh.oeaw.ac.at/apis/"
PROJECT_DEFAULT_MD = {
    "title": "TITLE",
    "author": "Matthias Schlögl, Peter Andorfer",
    "subtitle": "SUBTITLE",
    "description": """This is a default metadata file. To change this, provide\
    provide a following file {PROJECT_SHARED}/{PROJECT_NAME}/metadata.json""",
    "github": "https://github.com/acdh-oeaw/apis-webpage-base",
    "production instance": None,
    "purpose_de": "",
    "purpose_en": """""",
    "version": ["apis_core", "charts", "django"],
    "matomo_id": "",
    "matomo_url": "",
    "imprint": "/imprint",
    "social_media": [
        ("fab fa-twitter", "https://twitter.com/ACDH_OeAW"),
        ("fab fa-youtube", "https://www.youtube.com/channel/UCgaEMaMbPkULYRI5u6gvG-w"),
    ],
    "social_media": [
        ("fab fa-twitter fa-2x", "https://twitter.com/ACDH_OeAW"),
        (
            "fab fa-youtube fa-2x",
            "https://www.youtube.com/channel/UCgaEMaMbPkULYRI5u6gvG-w",
        ),
    ],
    "app_type": "database",
}

# Application definition

INSTALLED_APPS = [
    "dal",
    "dal_select2",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "reversion",
    "crispy_forms",
    "django_filters",
    "django_tables2",
    "rest_framework",
    "apis_core.core",
    "apis_core.apis_entities",
    "apis_core.apis_metainfo",
    "apis_core.apis_relations",
    "apis_core.apis_vocabularies",
    "apis_core.apis_labels",
    "rest_framework.authtoken",
    # "drf_yasg",
    "drf_spectacular",
    "csvexport",
    "apis_ontology",
]

# put apis_override_select2js at the beginning of the list
# to make its static files weigh more than from the other apps
INSTALLED_APPS = ["apis_override_select2js"] + INSTALLED_APPS

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SPECTACULAR_SETTINGS: Dict[str, Any] = {
    "TITLE": "APIS generic API",
    "DESCRIPTIOPN": "Provides access to the main APIS data-model endpoints.",
    "LICENSE": {"name": "MIT License", "url": "https://www.mit.edu/~amini/LICENSE.md"},
    "VERSION": "0.13",
}


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

CRISPY_TEMPLATE_PACK = "bootstrap3"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 50,
    "DEFAULT_PERMISSION_CLASSES": (
        # "rest_framework.permissions.DjangoModelPermissions",
        # "rest_framework.permissions.IsAuthenticated",
        "rest_framework.permissions.DjangoObjectPermissions",
        # use IsAuthenticated for every logged in user to have global edit rights
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

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",  # this is default
)

MIDDLEWARE = [
    "allow_cidr.middleware.AllowCIDRMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "csp.middleware.CSPMiddleware",
    "reversion.middleware.RevisionMiddleware",
    "crum.CurrentRequestUserMiddleware",
]

ROOT_URLCONF = "apis_achdch_default_settings.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "apis_ontology", "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apis_core.context_processors.custom_context_processors.list_apis_settings",
            ]
        },
    }
]

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

APIS_BASE_URI = "TO CHANGE"

APIS_MIN_CHAR = 0

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

DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap4.html"

APIS_COMPONENTS = []
# APIS settings

APIS_TEI_TEXTS = ["xml/tei transcription"]
APIS_CETEICEAN_CSS = "https://teic.github.io/CETEIcean/css/CETEIcean.css"
APIS_CETEICEAN_JS = "https://teic.github.io/CETEIcean/js/CETEI.js"

APIS_NEXT_PREV = True

APIS_ALTERNATE_NAMES = [
    "Taufname",
    "Ehename",
    "Name laut ÖBL XML",
    "alternative Namensform",
    "alternative name",
    "Künstlername",
    "Mädchenname",
    "Pseudonym",
    "weitere Namensform",
]

APIS_RELATIONS_FILTER_EXCLUDE = [
    "*uri*",
    "*tempentityclass*",
    "user",
    "*__id",
    "*source*",
    "label",
    "*temp_entity*",
    "*collection*",
    "*published*",
    "*_set",
    "*_set__*",
    "_ptr",
    "baseclass",
    "*id",
    "*written*",
    "relation_type__*",
    "*__text*",
    "text*",
    "*annotation_set_relation*",
    "*start_start_date*",
    "*end_end_date*",
    "*start_end_date*",
    "*end_start_date*",
    "*label*",
    "*review*",
    "*__name",
    "*__status",
    "*__references",
    "*__notes",
]



APIS_VOCABULARIES = {"exclude": ["userAdded"]}

APIS_METAINFO = {"exclude": ["groups_allowed"]}

# TODO RDF: Remove this dictionary from settings entirely and attach it only to entity models
APIS_ENTITIES = {}

APIS_API_EXCLUDE_SETS = True  # exclude reverse links to entities

APIS_LIST_VIEWS_ALLOWED = False
APIS_DETAIL_VIEWS_ALLOWED = False
MAX_AGE = 60 * 60

APIS_IIIF_WORK_KIND = "IIIF"
APIS_IIIF_ENT_IIIF_REL = "has iiif image"
APIS_IIIF_SERVER = "https://iiif.acdh.oeaw.ac.at/"
APIS_OSD_JS = (
    "https://cdnjs.cloudflare.com/ajax/libs/openseadragon/2.4.0/openseadragon.min.js"
)
APIS_OSD_IMG_PREFIX = (
    "https://cdnjs.cloudflare.com/ajax/libs/openseadragon/2.4.0/images/"
)

ALLOWED_CIDR_NETS = ["10.0.0.0/8", "127.0.0.0/8"]

DATABASES = { 'default': dj_database_url.config(default='sqlite:///db.sqlite3', conn_max_age=600) }

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
if os.environ.get("PUBLIC_URL"):
    ALLOWED_HOSTS.append(re.sub(r"https?://", "", os.environ.get("PUBLIC_URL")))

if os.environ.get("ALLOWED_HOSTS"):
    ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")
