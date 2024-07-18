from django.conf import settings
from django.db import models


class Advertisement(models.Model):
    """Объявления."""

    title = models.CharField(
        "Заголовок", max_length=settings.LENGTH_OF_NAME_FIELDS
    )
    ad_id = models.IntegerField(unique=True)
    author = models.CharField(
        "Автор", max_length=settings.LENGTH_OF_NAME_FIELDS
    )
    views = models.IntegerField("Количество просмотров.")
    position = models.IntegerField("Позиция.")

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["-views"]

    def __str__(self):
        return self.title
