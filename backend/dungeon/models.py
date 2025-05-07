from django.db import models
from heroes.models import Character
from enemies.models import EnemyStats


class DungeonDifficulty(models.Model):
    name = models.CharField(max_length=50)
    exp_multiplier = models.FloatField()
    rooms_before_boss = models.IntegerField()
    bonus_exp_chest = models.IntegerField(default=5)
    bonus_exp_buff = models.IntegerField(default=3)

    hp_multiplier = models.FloatField(default=1.0)
    attack_multiplier = models.FloatField(default=1.0)
    defense_multiplier = models.FloatField(default=1.0)
    crit_multiplier = models.FloatField(default=1.0)

    def __str__(self):
        return self.name


class RoomEventType(models.TextChoices):
    BATTLE = "Battle", "Битва"
    CHEST = "Chest", "Сундук"
    BUFF = "Buff", "Бафф"
    DEBUFF = "Debuff", "Дебафф"
    TRAP = "Trap", "Ловушка"
    EMPTY = "Empty", "Пусто"


class CurrentRoom(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE, related_name="current_room")

    event_type = models.CharField(max_length=20, choices=RoomEventType.choices)
    enemy = models.ForeignKey(EnemyStats, on_delete=models.SET_NULL, null=True, blank=True)
    enemy_hp = models.IntegerField(null=True, blank=True)
    enemy_attack = models.IntegerField(null=True, blank=True)
    enemy_defense = models.IntegerField(null=True, blank=True)
    enemy_crit_chance = models.FloatField(null=True, blank=True)
    enemy_exp = models.IntegerField(null=True, blank=True)

    is_cleared = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Комната игрока {self.character.name} — {self.get_event_type_display()}"