from rest_framework import generics

from ads_api.models import Advertisement
from ads_api.serializers import AdvertisementSerializer


class AdvertisementDetailView(generics.RetrieveAPIView):
    """Отображения объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    lookup_field = "ad_id"
