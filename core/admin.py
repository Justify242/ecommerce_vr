from django.contrib import admin

from core import models


class CaseImageInline(admin.TabularInline):
    model = models.CaseImage
    can_delete = True
    extra = 0
    readonly_fields = [
        "preview"
    ]


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(models.FaqItem)
class FaqItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Technology)
class TechnologyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Case)
class CaseAdmin(admin.ModelAdmin):
    inlines = [CaseImageInline]