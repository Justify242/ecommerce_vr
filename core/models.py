import os.path

from django.db import models
from django.urls import reverse

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class TimeBasedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeBasedModel):
    name = models.CharField(max_length=150, verbose_name="Наименование категории")
    slug = models.SlugField(unique=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Категория активна")

    image = models.ImageField(upload_to="categories/images/", null=True, blank=True)
    resized_image = ImageSpecField(
        source="image",
        processors=[ResizeToFill(640, 480)],
        format="JPEG",
        options={"quality": 70}
    )

    @property
    def resized_image_url(self):
        if not self.image or not os.path.exists(self.image.path):
            return "/static/assets/no_image.png"

        return self.resized_image.url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(TimeBasedModel):
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        verbose_name="Категория товара",
        related_name="products"
    )
    name = models.CharField(max_length=150, verbose_name="Наименование товара")
    calculator = models.ForeignKey("Calculator", on_delete=models.SET_NULL, null=True)
    show_calculator = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)

    image = models.ImageField(upload_to="products/images/", null=True, blank=True)
    resized_image = ImageSpecField(
        source="image",
        processors=[ResizeToFill(640, 480)],
        format="JPEG",
        options={"quality": 70}
    )

    @property
    def resized_image_url(self):
        if not self.image or not os.path.exists(self.image.path):
            return "/static/assets/no_image.png"

        return self.resized_image.url

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Calculator(TimeBasedModel):
    name = models.CharField(max_length=150, verbose_name="Наименование калькулятора")
    options = models.ManyToManyField("CalculatorOption")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Калькулятор"
        verbose_name_plural = "Калькуляторы"


class CalculatorOption(TimeBasedModel):
    field_name = models.CharField(max_length=100, verbose_name="Наименование поля", blank=True)
    name = models.CharField(max_length=150, verbose_name="Наименование настройки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Параметр калькулятора"
        verbose_name_plural = "Параметры калькуляторов"


class CalculatorOptionChoice(TimeBasedModel):
    option = models.ForeignKey("CalculatorOption", on_delete=models.CASCADE, related_name="choices")
    value = models.CharField(max_length=100, verbose_name="Значение")

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Значение параметра калькулятора"
        verbose_name_plural = "Значения параметров калькуляторов"


class Order(TimeBasedModel):
    phone = models.CharField(max_length=100, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Электронная почта")

    def __str__(self):
        return f"Заказ | {self.phone} | {self.email}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class OrderParameter(TimeBasedModel):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    option = models.ForeignKey(
        "CalculatorOption",
        on_delete=models.PROTECT,
        verbose_name="Параметр"
    )
    value = models.ForeignKey(
        "CalculatorOptionChoice",
        on_delete=models.PROTECT,
        verbose_name="Значение"
    )
    note = models.TextField(
        blank=True,
        null=True,
        verbose_name="Примечание"
    )
    file = models.FileField(
        upload_to="orders/files/",
        null=True,
        blank=True,
        verbose_name="Вложение"
    )

    def __str__(self):
        return f"Параметр заказа {self.order}"

    class Meta:
        verbose_name = "Параметр заказа"
        verbose_name_plural = "Параметры заказов"


class OrderFiles(TimeBasedModel):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    file = models.FileField(upload_to="orders/files/")

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = "Вложение заказа"
        verbose_name_plural = "Вложения заказов"


class Feedback(TimeBasedModel):
    name = models.CharField(max_length=150, verbose_name="Имя отправителя")
    email = models.EmailField(verbose_name="Почта отправителя")
    message = models.TextField(verbose_name="Сообщение")

    def __str__(self):
        return f"Обратная связь {self.name}"

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"