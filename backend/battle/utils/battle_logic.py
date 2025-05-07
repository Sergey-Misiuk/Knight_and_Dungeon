from heroes.models import Character
from enemies.models import EnemyStats


class BattleManager:
    def __init__(self, character: Character, enemy_stats: EnemyStats):
        self.character = character
        self.enemy_stats = enemy_stats
        self.enemy_hp = enemy_stats.final_hp()
        self.character_hp = character.hp

    def character_attack(self):
        """Игрок атакует врага."""
        damage = self.character.base_attack
        self.enemy_hp -= damage
        return f"👊 Вы нанесли {damage} урона врагу!"

    def enemy_attack(self):
        """Враг атакует игрока."""
        damage = self.enemy_stats.final_attack()
        self.character_hp -= damage
        return f"💥 Враг наносит вам {damage} урона!"

    def is_enemy_dead(self):
        return self.enemy_hp <= 0

    def is_character_dead(self):
        return self.character_hp <= 0

    def save_character_state(self):
        """Сохраняет текущее здоровье героя."""
        self.character.hp = max(self.character_hp, 0)
        self.character.save()
