
from battle.utils.battle_logic import BattleManager
from enemies.models import EnemyStats
from dungeon.utils.room_logic import process_room_event
from heroes.models import Character
import random


class RoomEventType:
    CHEST = "Сундук"
    BATTLE = "Битва"
    BUFF = "Бафф"
    DEBUFF = "Дебаф"
    TRAP = "Ловушка"
    EMPTY = "Пусто"


class RoomEventGenerator:
    """
    Генератор событий для комнаты.
    """

    EVENT_WEIGHTS = {
        RoomEventType.BATTLE: 40,
        RoomEventType.CHEST: 25,
        RoomEventType.BUFF: 10,
        RoomEventType.DEBUFF: 10,
        RoomEventType.TRAP: 5,
        RoomEventType.EMPTY: 10,
    }

    def __init__(self, character: Character):
        self.character = character
        self.difficulty = character.difficulty

    def choose_event_type(self) -> str:
        """
        Выбирает тип события на основе весов.
        """
        events = list(self.EVENT_WEIGHTS.keys())
        weights = list(self.EVENT_WEIGHTS.values())
        return random.choices(events, weights=weights, k=1)[0]

    def generate_event(self) -> str:
        """
        Генерирует событие для комнаты.
        """
        event_type = self.choose_event_type()

        if event_type == RoomEventType.BATTLE:
            return self.handle_battle()
        elif event_type == RoomEventType.CHEST:
            return self.handle_chest()
        elif event_type == RoomEventType.BUFF:
            return self.handle_buff()
        elif event_type == RoomEventType.DEBUFF:
            return self.handle_debuff()
        elif event_type == RoomEventType.TRAP:
            return self.handle_trap()
        elif event_type == RoomEventType.EMPTY:
            return self.handle_empty()
        return "🚪 Комната неизвестного типа."

    def handle_battle(self):

        enemy_stats = EnemyStats.objects.filter(difficulty=self.difficulty).order_by("?").first()

        if not enemy_stats:
            return {"event_text": "⚔️ Врагов не найдено!", "system_text": None}

        battle = BattleManager(self.character, enemy_stats)

        result_texts = []

        result_texts.append(battle.character_attack())

        if not battle.is_enemy_dead():
            result_texts.append(battle.enemy_attack())

        battle.save_character_state()

        if battle.is_enemy_dead():
            result_texts.append("🏆 Вы победили врага и получили награду!")
            # Здесь можно добавить увеличение опыта персонажа!
        elif battle.is_character_dead():
            result_texts.append("☠️ Вы погибли в бою...")

        return {
            "event_text": "⚔️ Начался бой!",
            "system_text": "\n".join(result_texts),
        }

        # return {
        #     "event_text": "⚔️ Впереди вас враг, готовьтесь к битве!",
        #     "system_text": None,
        # }

    def handle_chest(self):
        return {
            "event_text": "🪙 Вы нашли сундук!",
            "system_text": None,
        }

    def handle_buff(self):
        text, system_text = process_room_event(self.character, "Buff")
        return {
            "event_text": text,
            "system_text": system_text,
        }

    def handle_debuff(self):
        text, system_text = process_room_event(self.character, "Debuff")
        return {
            "event_text": text,
            "system_text": system_text,
        }

    def handle_trap(self):
        text, system_text = process_room_event(self.character, "Trap")
        return {
            "event_text": text,
            "system_text": system_text,
        }

    def handle_empty(self):
        return {
            "event_text": "🧹 Пустая комната. Пора отдохнуть...",
            "system_text": None,
        }
