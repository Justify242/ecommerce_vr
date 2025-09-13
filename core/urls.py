from django.urls import path

from core.views import (
    index,
    product_detail,
    catalog,
    contacts,
    feedback,

    CalculatorOptionAutocomplete,
    CalculatorOptionChoiceAutocomplete,
)

urlpatterns = [
    path('index/', index, name="index"),
    path('catalog/', catalog, name="catalog"),
    path('contacts/', contacts, name="contacts"),
    path("product/<slug:slug>/", product_detail, name="product_detail"),
    path("feedback/", feedback, name="feedback"),

    path('option-autocomplete/', CalculatorOptionAutocomplete.as_view(), name='option_autocomplete'),
    path('optionchoice-autocomplete/', CalculatorOptionChoiceAutocomplete.as_view(), name='optionchoice_autocomplete'),
]