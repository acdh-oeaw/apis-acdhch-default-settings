import requests
import os
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from django.conf import settings


@method_decorator(cache_page(60 * 5), name='dispatch')
class Imprint(TemplateView):
    template_name = "imprint.html"

    def get_context_data(self) -> str:
        ctx = super().get_context_data()
        base_url = getattr(settings, "ACDH_IMPRINT_URL", "https://imprint.acdh.oeaw.ac.at/")
        redmine_id = getattr(settings, "REDMINE_ID", os.getenv("SERVICE_ID", ""))

        r = requests.get(f"{base_url}{redmine_id}")

        if r and redmine_id:
            ctx["imprint"] = r.text
        else:
            ctx["imprint"] = """
            One of our services is currently not available. Please try it later or write
            an email to acdh@oeaw.ac.at; if you are service provider, make sure that you
            provided ACDH_IMPRINT_URL and REDMINE_ID.
            """
        return ctx
