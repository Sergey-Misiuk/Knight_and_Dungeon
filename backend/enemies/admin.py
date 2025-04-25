from django.contrib import admin
from .models import Enemy, EnemyStats


@admin.register(Enemy)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_boss", "base_hp", "base_attack", "base_defense", "base_crit_chance")
    list_filter = ("is_boss", "name",)
    search_fields = ("name",)


@admin.register(EnemyStats)
class DungeonDifficultyAdmin(admin.ModelAdmin):
    list_display = ("id", "enemy", "difficulty", "hp_multiplier", "attack_multiplier", "defense_multiplier", "crit_bonus")
    list_filter = ("enemy", "difficulty",)
