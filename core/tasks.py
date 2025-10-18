import logging

from django.conf import settings
from django.core.mail import send_mail
from django.utils.html import strip_tags

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

    subject = f"Новый заказ {order.full_name}, {order.phone}, {order.email}"
    message = (
        f"Новый заказ<br>"
        f"------------------------------------------------<br>"
        f"<b>ФИО</b>: {order.full_name or 'Не указано'}<br>"
        f"<b>Номер телефона</b>: {order.phone or 'Не указано'}<br>"
        f"<b>Электронная почта</b>: {order.email or 'Не указано'}<br>"
        f"<b>Ник в Telegram</b>: {order.telegram or 'Не указано'}<br>"
        f"------------------------------------------------<br>"
        f"<b>Комментарий к заказу</b>: {order.description or 'Не указано'}<br>"
    )

    try:
        send_mail(
            subject=subject,
            message=strip_tags(message),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
            html_message=message,
        )
    except Exception as exc:
        logger.exception(str(exc))
