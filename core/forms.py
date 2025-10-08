from django import forms

from core.models import Order



class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            "full_name",
            "phone",
            "email",
            "telegram",
            "description",
            "privacy_terms_accepted"
        ]
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "control"}),
            "phone": forms.TextInput(attrs={"class": "control"}),
            "email": forms.TextInput(attrs={"class": "control"}),
            "telegram": forms.TextInput(attrs={"class": "control"}),
            "description": forms.TextInput(attrs={"class": "control"}),
            "privacy_terms_accepted": forms.CheckboxInput(attrs={"class": "checkbox-control", "required": True}),
        }
