import json
import os

from django.core.management.base import BaseCommand

from ads_api.models import Advertisement


class Command(BaseCommand):
    help = "Load ads from a JSON file"

    def add_arguments(self, parser):
        parser.add_argument(
            "json_file",
            type=str,
            nargs="?",
            help="The JSON file containing ads data",
        )

    def handle(self, *args, **kwargs):
        json_file = kwargs["json_file"]

        if not json_file:
            json_file = os.path.join("test_data", "data.json")

        if not os.path.exists(json_file):
            self.stdout.write(
                self.style.ERROR(f"File {json_file} does not exist")
            )
            return

        with open(json_file, "r", encoding="utf-8") as file:
            ads_data = json.load(file)
            ads_to_create = []
            ads_to_update = []

            for ad_data in ads_data:
                ad_id = ad_data["ad_id"]
                ad, created = Advertisement.objects.update_or_create(
                    ad_id=ad_id,
                    defaults={
                        "title": ad_data["title"],
                        "author": ad_data["author"],
                        "views": ad_data["views"],
                        "position": ad_data["position"],
                    },
                )
                if created:
                    ads_to_create.append(ad)
                else:
                    ads_to_update.append(ad)

            if ads_to_create:
                Advertisement.objects.bulk_create(ads_to_create)

            if ads_to_update:
                Advertisement.objects.bulk_update(
                    ads_to_update, ["title", "author", "views", "position"]
                )

        self.stdout.write(self.style.SUCCESS("Successfully loaded ads data"))
