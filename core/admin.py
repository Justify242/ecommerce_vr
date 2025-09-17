from django.contrib import admin

from core import models


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(models.FaqItem)
class FaqItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Technology)
class TechnologyAdmin(admin.ModelAdmin):
    pass