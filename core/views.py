from django.shortcuts import render

from core.forms import OrderForm
from core.models import Technology, FaqItem


def index(request):
    technologies = Technology.objects.order_by("name")
    faq_items = FaqItem.objects.order_by("title")

    form = OrderForm()
    context = {
        "form": form,
        "technologies": technologies,
        "faq_items": faq_items
    }

    return render(request, template_name="core/index.html", context=context)



