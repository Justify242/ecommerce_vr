from django.urls import path

from core.views import index, product, catalog, contacts

urlpatterns = [
    path('index/', index, name="index"),
    path('product/', product, name="product"),
    path('catalog/', catalog, name="catalog"),
    path('contacts/', contacts, name="contacts"),
]