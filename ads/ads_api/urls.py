from django.urls import path

from ads_api.views import AdvertisementDetailView

urlpatterns = [
    path(
        "ads/<int:ad_id>/",
        AdvertisementDetailView.as_view(),
        name="ads-detail",
    ),
]
