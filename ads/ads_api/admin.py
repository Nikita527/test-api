from django.contrib import admin
from django.contrib.admin import register

from ads_api.models import Advertisement

EMTY_MSG = "-пусто-"


@register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    """Админ панель для объявлений."""

    list_display = (
        "title",
        "author",
        "views",
        "position",
    )
    search_fields = ("name",)
    empty_value_display = EMTY_MSG

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
