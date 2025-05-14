from django.contrib import admin
from items.models import InventoryItem, Weapon, Armor


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "tier", "min_damage", "max_damage")
    list_filter = ("tier", "name",)
    search_fields = ("name",)
    list_display_links = ("name",)


@admin.register(Armor)
class ArmorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "tier", "slot", "min_defense", "max_defense")
    list_filter = ("tier", "name",)
    search_fields = ("name",)
    list_display_links = ("name",)
    

@admin.register(InventoryItem)
class InventoryCharacterAdmin(admin.ModelAdmin):
    list_display = ("id", "character", "item_type", "weapon", "armor", "is_equipped")