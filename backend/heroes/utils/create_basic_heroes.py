from items.models import InventoryItem, Weapon, Armor


def assign_default_equipment(character):
    # Weapon
    basic_weapon, _ = Weapon.objects.get_or_create(
        name="Старый меч",
        defaults={"min_damage": 5, "max_damage": 10, "tier": 1}
    )

    # Armor
    basic_helmet, _ = Armor.objects.get_or_create(
        name="Старый шлем",
        slot="helmet",
        defaults={"min_defense": 1, "max_defense": 2, "tier": 1}
    )
    basic_chestplate, _ = Armor.objects.get_or_create(
        name="Старая кираса",
        slot="chestplate",
        defaults={"min_defense": 2, "max_defense": 4, "tier": 1}
    )
    basic_gloves, _ = Armor.objects.get_or_create(
        name="Старые перчатки",
        slot="gloves",
        defaults={"min_defense": 1, "max_defense": 2, "tier": 1}
    )
    basic_boots, _ = Armor.objects.get_or_create(
        name="Старые сапоги",
        slot="boots",
        defaults={"min_defense": 1, "max_defense": 2, "tier": 1}
    )

    character.weapon = basic_weapon
    character.helmet = basic_helmet
    character.chestplate = basic_chestplate
    character.gloves = basic_gloves
    character.boots = basic_boots
    character.save()
    
    for item in [basic_weapon, basic_helmet, basic_chestplate, basic_gloves, basic_boots]:
        if isinstance(item, Weapon):
            InventoryItem.objects.create(character=character, item_type="weapon", weapon= item, is_equipped=True)
        else:
            InventoryItem.objects.create(character=character, item_type="armor", armor=item, is_equipped=True)
