from django.http import JsonResponse
from django.shortcuts import render

from extra_settings.models import Setting

from core.forms import OrderForm
from core.models import Technology, FaqItem


def index(request):
    technologies = Technology.objects.order_by("id")
    faq_items = FaqItem.objects.order_by("id")

    form = OrderForm()
    context = {
        "form": form,
        "technologies": technologies,
        "faq_items": faq_items,
        "address": Setting.get("ADDRESS", "г. Москва"),
        "email": Setting.get("EMAIL", "email@example.ru"),
        "telegram": Setting.get("TELEGRAM", "@example"),
        "whatsapp": Setting.get("WHATSAPP", "8 (800) 555-35-35")
    }

    return render(request, template_name="core/index.html", context=context)



def new_order(request):
    form = OrderForm(request.POST)

    if form.is_valid():
        form.save()
        return JsonResponse({"detail": "ok"}, status=200)

    return JsonResponse({"detail": "failed"}, status=400)
