from django.db import models
import random

from items.utils.items_naming import get_item_name_by_tier


# TIER_CHOICES = [
#     (1, "Обычное"),
#     (2, "Редкое"),
#     (3, "Эпическое"),
#     (4, "Легендарное"),
# ]
# TIER_CHOICES = [
#     (1, "Обычное", "Обычный", "Обычные"),
#     (2, "Редкое", "Редкий", "Редкие"),
#     (3, "Эпическое", "Эпический", "Эпические"),
#     (4, "Легендарное", "Легендарный", "Легендарные"),
# ]


class Weapon(models.Model):

    name = models.CharField(max_length=100)
    min_damage = models.IntegerField()
    max_damage = models.IntegerField()
    tier = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = get_item_name_by_tier(self.tier, "weapon")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} (T{self.tier}) {self.min_damage}-{self.max_damage} ATK"


class Armor(models.Model):
    SLOT_CHOICES = [
        ("helmet", "Шлем"),
        ("chestplate", "Нагрудник"),
        ("gloves", "Перчатки"),
        ("boots", "Сапоги"),
    ]

    name = models.CharField(max_length=100)
    slot = models.CharField(max_length=20, choices=SLOT_CHOICES)
    tier = models.IntegerField(default=1)

    min_defense = models.IntegerField()
    max_defense = models.IntegerField()

    def get_random_defense(self):
        return random.randint(self.min_defense, self.max_defense) 

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = get_item_name_by_tier(self.tier, self.slot)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.get_slot_display()} T{self.tier}) {self.min_defense}-{self.max_defense} DEF"


class InventoryItem(models.Model):
    character = models.ForeignKey("heroes.Character", on_delete=models.CASCADE, related_name="inventory")
    item_type = models.CharField(max_length=10, choices=[("weapon", "Оружие"), ("armor", "Броня")])
    weapon = models.ForeignKey("items.Weapon", null=True, blank=True, on_delete=models.SET_NULL)
    armor = models.ForeignKey("items.Armor", null=True, blank=True, on_delete=models.SET_NULL)
    is_equipped = models.BooleanField(default=False)
    
    def __str__(self):
        if self.item_type == "weapon":
            return f"{self.weapon}"
        elif self.item_type == "armor":
            return f"{self.armor}"
        return "Unknown Item"