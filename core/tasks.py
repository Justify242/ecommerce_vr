import logging

from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from huey.contrib.djhuey import db_task

from core.models import Order


logger = logging.getLogger("tasks")


@db_task()
def send_email_worker(order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        logger.error(f"Заказ с ID {order_id} не существует")
        return

    user_model = get_user_model()
    emails = user_model.objects.exclude(email__isnull=True).values_list("email", flat=True)

    message = (
        f"Новый заказ\n\n"
        f"ФИО: {order.full_name or 'Не указано'}\n"
        f"Контакт: {order.phone or 'Не указано'}\n"
        f"Контакт: {order.email or 'Не указано'}\n"
        f"Контакт: {order.telegram or 'Не указано'}\n"
        f"Комментарий к заказу: {order.description or 'Не указано'}\n"
    )

    try:
        send_mail(
            subject="Новый заказ",
            message=message,
            from_email=None,
            recipient_list=emails,
            fail_silently=False,
        )
    except Exception as exc:
        print(exc)
