from django.core.management.base import BaseCommand
from rooms import models as room_models

NAME = "facilities"


class Command(BaseCommand):

    help = f"This command creates {NAME}"

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for facility in facilities:
            room_models.Facility.objects.create(name=facility)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} {NAME} created!"))
