import random
from dungeon.room_events import ROOM_EVENTS
from buffs.models import BuffDebuff

def process_room_event(character, event_type):
    """Возвращает (текст_атмосферы, системный_результат)"""
    
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
        # Применение эффекта – позже можно в battle.effects
        return text, f"🛡️ Вы получили бафф: {buff.name} (+{int((buff.value - 1) * 100)}%) на {buff.duration} ходов."

    elif event_type == "Debuff":
        attribute = random.choice(["Health", "Attack", "Defense"])
        debuff_name = f"{attribute} Curse"
        debuff = BuffDebuff.objects.get(name=debuff_name)
        text = random.choice(ROOM_EVENTS["Debuff"][attribute])
        # Применение эффекта — можно будет хранить как active_effect
        return text, f"☠️ Вас поразил дебафф: {debuff.name} (–{int((1 - debuff.value) * 100)}%) на {debuff.duration} ходов."
