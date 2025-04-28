import random
from dungeon.utils.room_text.room_events import ROOM_EVENTS
from buffs.models import BuffDebuff


ATTRIBUTE_MAPPING = {
    "health": "max_hp",
    "attack": "base_attack",
    "defense": "armor",
}


def process_room_event(character, event_type):
    """Возвращает (системный_результат)"""

    if event_type == "Trap":
        text = random.choice(ROOM_EVENTS["Trap"])
        damage = random.randint(5, 15)
        character.hp = max(0, character.hp - damage)
        character.save()
        return text, f"🩸 Вы потеряли {damage} HP из-за ловушки!"

    elif event_type == "Buff":
        attribute = random.choice(["Health", "Attack", "Defense"])
        buff_name = f"{attribute} Boost"
        buff = BuffDebuff.objects.get(name=buff_name)
        text = random.choice(ROOM_EVENTS["Buff"][attribute])
        calculation_buff_or_debuff("Buff", character, buff)

        return (
            text,
            f"🛡️ Вы получили бафф: {buff.get_attribute_display()} +{int((buff.value - 1) * 100)}% на {buff.duration} ходов.",
        )

    elif event_type == "Debuff":
        attribute = random.choice(["Health", "Attack", "Defense"])
        debuff_name = f"{attribute} Curse"
        debuff = BuffDebuff.objects.get(name=debuff_name)
        text = random.choice(ROOM_EVENTS["Debuff"][attribute])
        calculation_buff_or_debuff("Debuff", character, debuff)

        return (
            text,
            f"☠️ Вас поразил дебафф: {debuff.get_attribute_display()} –{int((1 - debuff.value) * 100)}% на {debuff.duration} ходов.",
        )


def calculation_buff_or_debuff(event_type: str, character, buff_obj):
    """
    Универсальная функция применения баффов и дебаффов.

    :param event_type: "Buff" или "Debuff"
    :param character: объект Character
    :param buff_obj: объект BuffDebuff
    """
    attribute_key = buff_obj.attribute
    model_field = ATTRIBUTE_MAPPING.get(attribute_key)

    if model_field is None:
        raise ValueError(f"Нет сопоставления для атрибута '{attribute_key}'")

    current_value = getattr(character, model_field, None)
    if current_value is None:
        raise ValueError(f"Character не имеет атрибута '{model_field}'")

    if event_type == "Buff":
        new_value = int(current_value * buff_obj.value)
    elif event_type == "Debuff":
        new_value = int(current_value * buff_obj.value)
    else:
        raise ValueError(f"Неверный тип события: {event_type}")

    setattr(character, model_field, new_value)
    character.save()

    return f"{model_field.capitalize()} изменено с {current_value} до {new_value}"
