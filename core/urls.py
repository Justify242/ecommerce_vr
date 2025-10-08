from django.urls import path
from django.contrib.sitemaps.views import sitemap

from core.views import index, new_order
from core.sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path('', index, name="index"),
    path('new-order/', new_order, name="new_order"),

    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
]