ATTRIBUTE_MAPPING = {
    "Health": "max_hp",
    "Attack": "base_attack",
    "Defense": "armor",
}


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
        new_value = round(current_value * buff_obj.value)
    elif event_type == "Debuff":
        new_value = round(current_value * buff_obj.value)
        if attribute_key == "Health":
            if character.max_hp > new_value:
                character.save()

        if new_value <= 1:
            setattr(character, model_field, 1)
            return None
    else:
        raise ValueError(f"Неверный тип события: {event_type}")

    setattr(character, model_field, new_value)
    character.save()

    return f"{model_field.capitalize()} изменено с {current_value} до {new_value}"
