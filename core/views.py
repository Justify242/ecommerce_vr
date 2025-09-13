from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.contrib import messages

from dal import autocomplete

from core.models import (
    Category,
    Product,
    CalculatorOption,
    CalculatorOptionChoice, OrderParameter
)
from core.forms import (
    DynamicCalculatorForm,
    OrderForm,
    FeedbackForm
)


class CalculatorOptionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = CalculatorOption.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class CalculatorOptionChoiceAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        option_id = self.forwarded.get("option")
        if option_id:
            qs = CalculatorOptionChoice.objects.filter(option_id=option_id)
        else:
            qs = CalculatorOptionChoice.objects.none()

        return qs


def index(request):
    categories = Category.objects.filter(is_active=True)
    context = {
        "categories": categories
    }

    return render(request, template_name="core/index.html", context=context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_form = OrderForm(request.POST or None)
    calculator_form = DynamicCalculatorForm(
        request.POST or None,
        options=product.calculator.options.all()
    )

    template_name = "core/product.html"
    context = {
        "calculator_form": calculator_form,
        "order_form": order_form
    }

    if request.method == "POST":
        if not calculator_form.is_valid() or not order_form.is_valid():
            return render(request, template_name=template_name, context=context)

        data = calculator_form.json_dump()
        order = order_form.save()

        for parameter in data:
            field_name, label, value = parameter.values()

            option = CalculatorOption.objects.get(field_name=field_name)
            OrderParameter.objects.get_or_create(
                order=order,
                option=option,
                value_id=value
            )

    return render(request, template_name=template_name, context=context)


def catalog(request):
    return render(request, "core/catalog.html")


def contacts(request):
    return render(request, "core/contacts.html")


def feedback(request):
    form = FeedbackForm(request.POST or None)
    template_name = "core/feedback.html"

    context = {"form": form}

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Форма отправлена")
        else:
            messages.error(request, "Ошибка валидации формы")

    return render(request, template_name=template_name, context=context)


