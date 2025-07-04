from django.shortcuts import render


def index(request):
    return render(request, "core/index.html")


def product(request):
    return render(request, "core/product.html")


def catalog(request):
    return render(request, "core/catalog.html")


def contacts(request):
    return render(request, "core/contacts.html")