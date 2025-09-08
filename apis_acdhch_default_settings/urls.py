from django.apps import apps
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from apis_acdhch_default_settings.views import Imprint

from apis_core.apis_entities.api_views import GetEntityGeneric

urlpatterns = [
    path("apis/", include("apis_core.urls", namespace="apis")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("entity/<int:pk>/", GetEntityGeneric.as_view(), name="GetEntityGenericRoot"),
    path("admin/", admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()

if apps.is_installed("apis_bibsonomy"):
    urlpatterns.append(
        path("bibsonomy/", include("apis_bibsonomy.urls", namespace="bibsonomy"))
    )

urlpatterns.append(path("", TemplateView.as_view(template_name="base.html")))
urlpatterns.append(path("imprint", Imprint.as_view(), name="imprint"))
urlpatterns += [
    path("", include("apis_acdhch_django_auditlog.urls")),
]
