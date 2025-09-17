from django.db.models.signals import post_save
from django.dispatch import receiver

from core import models
from core.tasks import send_email_worker


@receiver(post_save, sender=models.Order)
def handle_order_post_save(sender, instance, created, **kwargs):
    if not created:
        return

    send_email_worker(instance.id)
