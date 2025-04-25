from django.core.management.base import BaseCommand
from buffs.models import BuffDebuff
from buffs.management.data.buffs_init import BUFFS_DATA


class Command(BaseCommand):
    help = "Загрузка дефолтных баффов и дебаффов"

    def handle(self, *args, **kwargs):
        created_count = 0

        for buff_data in BUFFS_DATA:
            obj, created = BuffDebuff.objects.get_or_create(
                name=buff_data["name"],
                defaults={
                    "effect_type": buff_data["effect_type"],
                    "attribute": buff_data["attribute"],
                    "value": buff_data["value"],
                    "duration": buff_data["duration"],
                    "description": buff_data["description"],
                }
            )
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Загружено новых баффов: {created_count}"))
