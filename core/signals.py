from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from unidecode import unidecode

from core import models


@receiver(pre_save, sender=models.Category)
@receiver(pre_save, sender=models.Product)
def handle_category_pre_save(sender, instance, **kwargs):
    if instance.slug:
        return

    instance.slug = slugify(unidecode(instance.name))


@receiver(post_save, sender=models.CalculatorOption)
def handle_calculator_option_post_save(sender, instance, created, **kwargs):
    if instance.field_name:
        return

    instance.field_name = f"option_{instance.id}"
    instance.save()