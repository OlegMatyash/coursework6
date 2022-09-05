from django.conf import settings
from django.db import models


class Ad(models.Model):
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Фото",
        help_text="Разместите фото для объявления",
        null=True,
        blank=True,
    )

    title = models.CharField(
        max_length=200,
        verbose_name="Название товара",
        help_text="Введите название товара",
    )

    price = models.PositiveIntegerField(
        verbose_name="Цена товара",
        help_text="Добавьте цену товара",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="ads",
        verbose_name="Автор объявления",
        help_text="Выберите автора объявления",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания объявления",
        help_text="Введите время создания объявления",
    )

    description = models.CharField(
        blank=True,
        null=True,
        max_length=1000,
        verbose_name="Описание товара",
        help_text="Введите описание товара",
    )

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ("-created_at",)


class Comment(models.Model):
    text = models.CharField(
        max_length=1000,
        verbose_name="Комментарий",
        help_text="Оставьте свой комментарий здесь",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания комментария",
        help_text="Введите время создания комментария",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор комментария",
        help_text="Выберите автора комментария",
    )
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Объявление",
        help_text="Объявление, к которому относится комментарий",
    )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ("-created_at",)
