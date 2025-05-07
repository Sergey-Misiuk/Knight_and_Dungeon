import random
from buffs.utils.buff_debuff_logic import calculation_buff_or_debuff
from dungeon.utils.room_text.room_events import ROOM_EVENTS
from buffs.models import BuffDebuff


def process_room_event(character, event_type):
    """Возвращает (системный_результат)"""

    if event_type == "Trap":
        text = random.choice(ROOM_EVENTS["Trap"])
        damage = random.randint(5, 15)
        character.hp = max(0, character.hp - damage)
        character.save()
        return text, f"🩸  Вы потеряли {damage} HP из-за ловушки!"

    elif event_type == "Buff":
        attribute = random.choice(["Health", "Attack", "Defense"])
        buff = BuffDebuff.objects.get(attribute=attribute, effect_type=event_type)
        text = random.choice(ROOM_EVENTS["Buff"][attribute])
        calculation_buff_or_debuff(event_type, character, buff)

        # На данный момент реализация бафа на колличество ходов не работает
        return (
            text,
            # f"🛡️  Вы получили бафф: {buff.get_attribute_display()} +{round((buff.value - 1) * 100)}% на {buff.duration} ходов.",
            f"🛡️  Вы получили бафф: {buff.get_attribute_display()} +{round((buff.value - 1) * 100)}%",
        )

    elif event_type == "Debuff":
        attribute = random.choice(["Health", "Attack", "Defense"])
        debuff = BuffDebuff.objects.get(attribute=attribute, effect_type=event_type)
        text = random.choice(ROOM_EVENTS["Debuff"][attribute])
        result_value = calculation_buff_or_debuff(event_type, character, debuff)

        if not result_value:
            return (
                "Ты очень ослаб рыцарь, может пора умереть?",
                f"Твой показатель {debuff.attribute} равен 1",
            )

        # На данный момент реализация дебафа на колличество ходов не работает
        return (
            text,
            # f"☠️  Вас поразил дебафф: {debuff.get_attribute_display()} –{round((1 - debuff.value) * 100)}% на {debuff.duration} ходов.",
            f"☠️  Вас поразил дебафф: {debuff.get_attribute_display()} –{round((1 - debuff.value) * 100)}%",
        )

    return None, None
