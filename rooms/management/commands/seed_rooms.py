import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


NAME = "rooms"


class Command(BaseCommand):

    help = f"This command created {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many rooms you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: (seeder.faker.first_name()) + "'s Room",
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 7),
                "price": lambda x: random.randint(50, 200),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()
        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for _ in range(3, random.randint(10, 15)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                )
            for amenity in amenities:
                magic_number = random.randint(1, 15)
                if magic_number % 2 == 0:
                    room.amenities.add(amenity)
            for facility in facilities:
                magic_number = random.randint(1, 15)
                if magic_number % 2 == 0:
                    room.facilities.add(facility)
            for rule in rules:
                magic_number = random.randint(1, 15)
                if magic_number % 2 == 0:
                    room.house_rules.add(rule)
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
