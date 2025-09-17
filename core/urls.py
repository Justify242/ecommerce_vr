from django.urls import path

from core.views import index, new_order

urlpatterns = [
    path('index/', index, name="index"),
    path('new-order/', new_order, name="new_order"),
]