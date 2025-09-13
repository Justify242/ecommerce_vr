import json

from django import forms
from dal import autocomplete

from core.models import Order, OrderParameter, Feedback


class DynamicCalculatorForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.options = kwargs.pop("options")
        super().__init__(*args, **kwargs)

        # Добавляем поля динамически
        self._set_fields()

    def _set_fields(self):
        for option in self.options:
            choices = [(choice.id, choice.value) for choice in option.choices.all()]

            self.fields[option.field_name] = forms.ChoiceField(
                label=option.name,
                choices=choices,
                required=True,
                widget=forms.Select()
            )

    def json_dump(self):
        if not hasattr(self, "cleaned_data"):
            raise ValueError("You must call is_valid() before calling json_dump().")

        data = []
        for name, field in self.fields.items():
            value = self.cleaned_data.get(name)
            data.append({
                "field_name": name,
                "label": field.label,
                "value": value,
            })
        return data


class OrderParameterForm(forms.ModelForm):
    class Meta:
        model = OrderParameter
        fields = "__all__"
        widgets = {
            "option": autocomplete.ModelSelect2(url="option_autocomplete"),
            "value": autocomplete.ModelSelect2(
                url="optionchoice_autocomplete",
                forward=["option"]
            ),
            "note": forms.Textarea(),
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "email",
            "phone"
        ]
