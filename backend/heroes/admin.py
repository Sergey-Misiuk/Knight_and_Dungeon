from django.contrib import admin
from items.models import InventoryItem
from heroes.models import Character
from django.urls import reverse
from django.utils.html import format_html


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "user",
        "difficulty",
        "level",
        "experience",
        "is_alive",
        "weapon_link",
        "helmet_link",
        "chestplate_link",
        "gloves_link",
        "boots_link",
    )
    list_filter = ("difficulty", "is_alive", "archetype")
    search_fields = ("name", "user__telegram_id")
    list_display_links = ("name", "weapon_link")

    fieldsets = (
        (
            "🧍 Основная информация",
            {"fields": ("name", "user", "archetype", "difficulty", "is_alive")},
        ),
        (
            "📊 Прогресс",
            {"fields": ("level", "experience", "skill_points", "count_room")},
        ),
        ("❤️ Здоровье", {"fields": ("hp", "max_hp")}),
        ("🪙 Экономика", {"fields": ("personal_gold",)}),
        (
            "🗡️ Снаряжение",
            {"fields": ("weapon", "helmet", "chestplate", "gloves", "boots")},
        ),
    )

    def weapon_link(self, obj):
        if obj.weapon:
            url = reverse("admin:items_weapon_change", args=[obj.weapon.id])
            return format_html('<a href="{}">{}: ID {}</a>', url, obj.weapon.name, obj.weapon.id)
        return "—"
    weapon_link.short_description = "Оружие"

    def _armor_link(self, obj, slot_name, label):
        armor_piece = getattr(obj, slot_name)
        if armor_piece:
            url = reverse("admin:items_armor_change", args=[armor_piece.id])
            return format_html('<a href="{}">{}: ID {}</a>', url, armor_piece.name, armor_piece.id)
        return "—"

    def helmet_link(self, obj):
        return self._armor_link(obj, "helmet", "Шлем")
    helmet_link.short_description = "Шлем"

    def chestplate_link(self, obj):
        return self._armor_link(obj, "chestplate", "Нагрудник")
    chestplate_link.short_description = "Нагрудник"

    def gloves_link(self, obj):
        return self._armor_link(obj, "gloves", "Перчатки")
    gloves_link.short_description = "Перчатки"

    def boots_link(self, obj):
        return self._armor_link(obj, "boots", "Сапоги")
    boots_link.short_description = "Сапоги"