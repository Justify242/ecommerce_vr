from django import forms

from core.models import Order



class OrderForm(forms.ModelForm):
    count = forms.IntegerField(
        initial=None,
        widget=forms.NumberInput(
            attrs={"class": "control"}
        )
    )

    class Meta:
        model = Order
        fields = [
            "full_name",
            "contact",
            "count",
            "product_type",
        ]
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "control"}),
            "contact": forms.TextInput(attrs={"class": "control"}),
            "product_type": forms.TextInput(attrs={"class": "control"}),
        }
