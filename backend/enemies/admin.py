from django.contrib import admin
from .models import Enemy, EnemyStats


@admin.register(Enemy)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_boss", "base_hp", "base_attack", "base_defense", "base_crit_chance", "base_exp_reward")
    list_filter = ("is_boss", "name",)
    search_fields = ("name",)


@admin.register(EnemyStats)
class DungeonDifficultyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "enemy",
        "difficulty",
        "final_hp",
        "final_attack",
        "final_defense",
        "final_crit_chance",
        "final_exp_reward",
    )
    list_filter = ("enemy", "difficulty",)
