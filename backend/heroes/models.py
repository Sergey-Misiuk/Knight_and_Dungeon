from django.db import models
from users.models import User


class Character(models.Model):
    ARCHETYPE_CHOICES = [
        ("brave", "Бесстрашный"),
        ("sarcastic", "Саркастичный"),
        ("dark", "Мрачный"),
    ]

    # User
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # Personal Gold
    personal_gold = models.IntegerField(default=0)
    # Level
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    skill_points = models.IntegerField(default=0)
    # Characteristics
    hp = models.IntegerField(default=100)
    max_hp = models.IntegerField(default=100)
    base_attack = models.IntegerField(default=10)
    armor = models.IntegerField(default=5)
    # Room
    count_room = models.IntegerField(default=1)

    difficulty = models.ForeignKey("dungeon.DungeonDifficulty", on_delete=models.SET_NULL, null=True)

    is_alive = models.BooleanField(default=True)
    archetype = models.CharField(max_length=20, choices=ARCHETYPE_CHOICES, default="brave")

    def __str__(self):
        return self.name

    def gain_experience(self, amount):
        self.experience += amount
        while self.experience >= self.required_experience():
            self.level_up()

    def level_up(self):
        self.level += 1
        self.skill_points += 1
        self.experience -= self.required_experience()

    def required_experience(self):
        return 100 + (self.level - 1) * 50
