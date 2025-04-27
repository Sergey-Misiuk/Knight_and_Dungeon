from django.core.management.base import BaseCommand
from enemies.models import Enemy, EnemyStats
from dungeon.models import DungeonDifficulty
from enemies.management.data.enemies_init import ENEMIES_DATA


class Command(BaseCommand):
    help = "Загружает базовых врагов и их характеристики по уровням сложности"

    def handle(self, *args, **kwargs):
        created_enemies = 0
        created_stats = 0

        difficulties = DungeonDifficulty.objects.all()
        if not difficulties.exists():
            self.stdout.write(self.style.ERROR("❌ Нет уровней сложности в базе данных. Сначала запусти команду load_dungeon_difficulty!"))
            return

        for enemy_key, data in ENEMIES_DATA.items():
            enemy, created = Enemy.objects.get_or_create(
                name=enemy_key,
                defaults={
                    "base_hp": data["base_hp"],
                    "base_attack": data["base_attack"],
                    "base_defense": data["base_defense"],
                    "base_crit_chance": data["base_crit_chance"],
                    "base_exp_reward": data["base_exp_reward"],
                    "is_boss": data["is_boss"],
                },
            )
            if created:
                created_enemies += 1

            # Теперь создаём EnemyStats для каждой сложности
            for difficulty in difficulties:
                EnemyStats.objects.get_or_create(
                    enemy=enemy,
                    difficulty=difficulty
                )
                created_stats += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Создано врагов: {created_enemies}"))
        self.stdout.write(self.style.SUCCESS(f"✅ Создано статов для врагов: {created_stats}"))