from django.contrib import admin
from .models import Character


# @admin.register(Character)
# class CharacterAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "name",
#         "user",
#         "difficulty",
#         "personal_gold",
#         "count_room",
#         "level",
#         "experience",
#         "skill_points",
#         "hp",
#         "max_hp",
#         "weapon",
#         "helmet",
#         "chestplate",
#         "gloves",
#         "boots",
#         "is_alive",
#         "archetype",
#     )
#     list_filter = ("difficulty", "is_alive", "archetype")
#     search_fields = ("name", "user__telegram_id")



@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "user", "difficulty", "level", "experience", "is_alive"
    )
    list_filter = ("difficulty", "is_alive", "archetype")
    search_fields = ("name", "user__telegram_id")

    fieldsets = (
        ("🧍 Основная информация", {
            "fields": ("name", "user", "archetype", "difficulty", "is_alive")
        }),
        ("📊 Прогресс", {
            "fields": ("level", "experience", "skill_points", "count_room")
        }),
        ("❤️ Здоровье", {
            "fields": ("hp", "max_hp")
        }),
        ("🪙 Экономика", {
            "fields": ("personal_gold",)
        }),
        ("🗡️ Снаряжение", {
            "fields": ("weapon", "helmet", "chestplate", "gloves", "boots")
        }),
    )