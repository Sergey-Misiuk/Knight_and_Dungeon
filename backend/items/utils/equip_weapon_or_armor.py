from items.models import InventoryItem


def equip_weapon(character, inventory_item):

    res, _ = InventoryItem.objects.get_or_create(
        character=character,
        item_type="weapon",
        weapon=inventory_item,
        is_equipped=True
    )
    InventoryItem.objects.filter(
        character=character, item_type="weapon", is_equipped=True
    ).exclude(weapon=inventory_item).update(is_equipped=False)

    character.weapon = res.weapon
    character.save()


def equip_armor(character, inventory_item):
    slot = inventory_item.armor.slot

    InventoryItem.objects.filter(
        character=character, item_type="armor", armor__slot=slot, is_equipped=True
    ).update(is_equipped=False)

    inventory_item.is_equipped = True
    inventory_item.save()

    setattr(character, slot, inventory_item.armor)
    character.save()
