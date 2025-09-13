from django.contrib import admin

from core import models
from core.forms import OrderParameterForm


class CalculatorOptionInline(admin.TabularInline):
    model = models.CalculatorOption
    fields = ["name"]
    extra = 1
    can_delete = True


class CalculatorOptionChoiceInline(admin.TabularInline):
    model = models.CalculatorOptionChoice
    fields = ["value"]
    extra = 1
    can_delete = True


class OrderParameterInline(admin.TabularInline):
    form = OrderParameterForm
    model = models.OrderParameter
    fields = [
        "option",
        "value",
        "note",
        "file"
    ]
    extra = 1
    can_delete = True


@admin.register(models.Category)
class Category(admin.ModelAdmin):
    pass


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Calculator)
class CalculatorAdmin(admin.ModelAdmin):
    filter_horizontal = ["options"]


@admin.register(models.CalculatorOption)
class CalculatorOptionAdmin(admin.ModelAdmin):
    inlines = [CalculatorOptionChoiceInline]


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderParameterInline]