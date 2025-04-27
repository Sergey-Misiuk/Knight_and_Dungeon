from django.contrib import admin
from .models import Character


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user", "level", "experience", "is_alive", "archetype")
    list_filter = ("difficulty", "is_alive", "archetype")
    search_fields = ("name", "user__telegram_id")


