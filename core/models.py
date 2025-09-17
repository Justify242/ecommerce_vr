import re

from unidecode import unidecode

from django.db import models
from ckeditor.fields import RichTextField


class TimeBasedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FaqItem(TimeBasedModel):
    title = models.CharField(max_length=200, verbose_name="Заголовок вопроса")
    text = RichTextField(verbose_name="Текст вопроса")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Часто задаваемый вопрос"
        verbose_name_plural = "Часто задаваемые вопросы"


class Technology(TimeBasedModel):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    description = RichTextField(verbose_name="Описание")

    @staticmethod
    def _slugify(text):
        text = unidecode(text)
        return re.sub(r"\W+", "-", text.lower()).strip("-")

    @property
    def slug(self):
        return self._slugify(self.name)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Технология нанесения"
        verbose_name_plural = "Технологии нанесения"


class Order(TimeBasedModel):
    full_name = models.CharField(max_length=200, verbose_name="ФИО пользователя")
    contact = models.CharField(max_length=100, verbose_name="Контакт пользователя")
    count = models.PositiveIntegerField(verbose_name="Тираж", default=0)
    product_type = models.TextField(verbose_name="Тип изделия")

    def __str__(self):
        return f"Заказ | {self.full_name} | {self.contact}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
