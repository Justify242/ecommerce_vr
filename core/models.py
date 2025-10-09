import re

from unidecode import unidecode

from django.utils.html import format_html
from django.db import models
from django.core.exceptions import ValidationError

from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class TimeBasedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Case(TimeBasedModel):
    name = models.CharField(max_length=200, verbose_name="Наименование кейса")
    is_published = models.BooleanField(default=True, verbose_name="Кейс опубликован")

    @property
    def main_image(self):
        img = self.caseimage_set.filter(is_main=True).order_by("-id").first()
        return img.image.url if img else None

    @property
    def data_images(self):
        imgs = self.caseimage_set.order_by("-id")
        urls = ", ".join([f'"{img.image.url}"' for img in imgs])
        return f"[{urls}]"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кейс"
        verbose_name_plural = "Кейсы"


class CaseImage(TimeBasedModel):
    case = models.ForeignKey("Case", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="cases/images/", verbose_name="Изображение")
    resized_image = ImageSpecField(
        source="image",
        # processors=[ResizeToFill(1400, 600)],
        format='JPEG',
        options={'quality': 60}
    )
    is_main = models.BooleanField(default=False, verbose_name="Основное")

    def preview(self):
        if self.image:
            return format_html(
                '<img src="{}" style="max-height: 200px; max-width: 250px;" />',
                self.resized_image.url
            )
        return "(Нет изображения)"

    def __str__(self):
        return f"Изображение кейса | {self.case}"

    class Meta:
        verbose_name = "Изображение кейса"
        verbose_name_plural = "Изображения кейсов"


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
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Почта")
    telegram = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Ник в Telegram"
    )
    description = models.TextField(verbose_name="Комментарий к заказу", blank=True)
    privacy_terms_accepted = models.BooleanField(
        default=False,
        verbose_name="Согласен с политикой обработки данных"
    )

    def clean(self):
        if not self.privacy_terms_accepted:
            raise ValidationError(
                "Для отправки заказа требуется согласиться с "
                "условиями политики конфиденциальности"
            )

    def __str__(self):
        return f"Заказ | {self.full_name} | {self.phone} | {self.email} | {self.telegram}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
