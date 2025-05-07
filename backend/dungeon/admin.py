from django.contrib import admin
from dungeon.models import DungeonDifficulty, CurrentRoom


@admin.register(DungeonDifficulty)
class DungeonDifficultyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "exp_multiplier",
        "rooms_before_boss",
        "hp_multiplier",
        "attack_multiplier",
        "defense_multiplier",
        "crit_multiplier",
    )


@admin.register(CurrentRoom)
class CurrentRoomAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "character",
        "event_type",
        "enemy",
        "enemy_hp",
        "enemy_attack",
        "enemy_defense",
        "enemy_crit_chance",
        "enemy_exp",
        "is_boss_enemy",
        "is_cleared",
        "created_at",
    )
    list_filter = ("event_type", "is_cleared", "enemy__enemy__is_boss")

    @admin.display(boolean=True, description="Босс?")
    def is_boss_enemy(self, obj):
        if obj.enemy:
            return obj.enemy.enemy.is_boss
        return None
