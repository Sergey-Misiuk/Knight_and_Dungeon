from django.contrib import admin
from .models import DungeonDifficulty


@admin.register(DungeonDifficulty)
class DungeonDifficultyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "exp_multiplier", "rooms_before_boss")