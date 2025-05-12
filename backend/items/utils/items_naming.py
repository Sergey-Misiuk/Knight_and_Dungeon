TIER_ADJECTIVES = {
    1: {"m": "Обычный", "f": "Обычная", "n": "Обычное", "pl": "Обычные"},
    2: {"m": "Хороший", "f": "Хорошая", "n": "Хорошее", "pl": "Хорошие"},
    3: {"m": "Редкий", "f": "Редкая", "n": "Редкое", "pl": "Редкие"},
    4: {
        "m": "Эпический",
        "f": "Эпическая",
        "n": "Эпическое",
        "pl": "Эпические"
        },
    5: {
        "m": "Легендарный",
        "f": "Легендарная",
        "n": "Легендарное",
        "pl": "Легендарные",
    },
}

ITEM_GRAMMAR = {
    "weapon": ("меч", "m"),
    "helmet": ("шлем", "m"),
    "chestplate": ("нагрудник", "m"),
    "gloves": ("перчатки", "pl"),
    "boots": ("сапоги", "pl"),
}


def get_item_name_by_tier(tier: int, slot: str) -> str:
    noun, gender = ITEM_GRAMMAR[slot]
    adjective = TIER_ADJECTIVES[tier][gender]
    return f"{adjective} {noun}"
