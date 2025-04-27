from django.core.management.base import BaseCommand
from dungeon.models import DungeonDifficulty
from dungeon.management.data.dungeon_difficulty_init import DUNGEON_DIFFICULTY


class Command(BaseCommand):
    help = "Загрузка сложностей подземельев"

    def handle(self, *args, **kwargs):
        created_count = 0

        for dungeon in DUNGEON_DIFFICULTY:
            obj, created = DungeonDifficulty.objects.get_or_create(
                name=dungeon["name"],
                defaults={
                    "exp_multiplier": dungeon["exp_multiplier"],
                    "rooms_before_boss": dungeon["rooms_before_boss"],
                    "bonus_exp_chest": dungeon["bonus_exp_chest"],
                    "bonus_exp_buff": dungeon["bonus_exp_buff"],
                    "hp_multiplier": dungeon["hp_multiplier"],
                    "attack_multiplier": dungeon["attack_multiplier"],
                    "defense_multiplier": dungeon["defense_multiplier"],
                    "crit_multiplier": dungeon["crit_multiplier"],
                }
            )
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Загружено новых сложностей: {created_count}"))
