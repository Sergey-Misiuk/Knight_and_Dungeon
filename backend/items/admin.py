from django.contrib import admin
from items.models import Weapon, Armor


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "tier", "min_damage", "max_damage")
    list_filter = ("tier", "name",)
    search_fields = ("name",)


@admin.register(Armor)
class ArmorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "tier", "slot", "min_defense", "max_defense")
    list_filter = ("tier", "name",)
    search_fields = ("name",)