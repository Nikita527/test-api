from rest_framework import serializers

from ads_api.models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    """Отображения объявлений в формате API."""

    class Meta:
        model = Advertisement
        fields = [
            "title",
            "ad_id",
            "author",
            "views",
            "position",
        ]
