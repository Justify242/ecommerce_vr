from django.http import JsonResponse
from django.shortcuts import render

from extra_settings.models import Setting

from core.forms import OrderForm
from core.models import Technology, FaqItem, Case


def index(request):
    technologies = Technology.objects.order_by("id")
    faq_items = FaqItem.objects.order_by("id")
    cases = Case.objects.filter(is_published=True).order_by("id").prefetch_related("caseimage_set")

    telegram_raw = Setting.get("TELEGRAM", "@example").replace("@", "")
    whatsapp_raw = (
        Setting.get("WHATSAPP", "8 (800) 555-35-35")
        .replace("-", "")
        .replace("+", "")
        .replace("(", "")
        .replace(")", "")
        .replace(" ", "")
    )

    form = OrderForm()
    context = {
        "form": form,
        "cases": cases,
        "technologies": technologies,
        "faq_items": faq_items,
        "address": Setting.get("ADDRESS", "г. Москва"),
        "email": Setting.get("EMAIL", "email@example.ru"),
        "telegram": Setting.get("TELEGRAM", "@example"),
        "telegram_raw": telegram_raw,
        "whatsapp": Setting.get("WHATSAPP", "8 (800) 555-35-35"),
        "whatsapp_raw": whatsapp_raw,
        "private_terms_file": Setting.get("PRIVATE_TERMS_FILE", ""),
        "public_offer_file": Setting.get("PUBLIC_OFFER_FILE", ""),
    }

    return render(request, template_name="core/index.html", context=context)



def new_order(request):
    form = OrderForm(request.POST)

    if form.is_valid():
        form.save()
        return JsonResponse({"detail": "ok"}, status=200)

    errors = []
    for field, error_list in form.errors.items():
        for error in error_list:
            errors.append(error)

    return JsonResponse({"detail": "\n".join(errors)}, status=400)
