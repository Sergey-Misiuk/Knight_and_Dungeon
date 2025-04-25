from django.db import models


class Enemy(models.Model):
    ENEMY_TYPE_CHOICES = [
        ("skeleton", "Скелет"),
        ("goblin", "Гоблин"),
        ("orc", "Орк"),
        ("undead", "Нежить"),
        ("werewolf", "Оборотень"),
        ("mage", "Маг"),
        ("dragon", "Дракон"),
    ]

    name = models.CharField(max_length=100, choices=ENEMY_TYPE_CHOICES)
    is_boss = models.BooleanField(default=False)
    base_hp = models.IntegerField(default=50)
    base_attack = models.IntegerField(default=10)
    base_defense = models.IntegerField(default=5)
    base_crit_chance = models.FloatField(default=0.05)

    def __str__(self):
        return f"{'Босс' if self.is_boss else 'Враг'}: {self.get_name_display()}"


class EnemyStats(models.Model):
    enemy = models.ForeignKey(Enemy, on_delete=models.CASCADE, related_name="stats")
    difficulty = models.ForeignKey('heroes.DungeonDifficulty', on_delete=models.CASCADE)

    hp_multiplier = models.FloatField(default=1.0)
    attack_multiplier = models.FloatField(default=1.0)
    defense_multiplier = models.FloatField(default=1.0)
    crit_bonus = models.FloatField(default=0.0)
    exp_reward = models.IntegerField(default=10)

    def __str__(self):
        return f"{self.enemy.get_name_display()} ({self.difficulty.name})"

    def final_hp(self):
        return int(self.enemy.base_hp * self.hp_multiplier)

    def final_attack(self):
        return int(self.enemy.base_attack * self.attack_multiplier)

    def final_defense(self):
        return int(self.enemy.base_defense * self.defense_multiplier)

    def final_crit_chance(self):
        return self.enemy.base_crit_chance + self.crit_bonus
