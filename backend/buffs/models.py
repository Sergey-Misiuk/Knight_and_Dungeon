from django.db import models


class BuffDebuff(models.Model):
    EFFECT_TYPE_CHOICES = [
        ("Buff", "Баф"),
        ("Debuff", "Дебафф"),
    ]

    ATTRIBUTE_CHOICES = [
        ("Attack", "Атака"),
        ("Defense", "Защита"),
        ("Health", "Здоровье"),
        # ("crit_chance", "Шанс крита"),
    ]

    name = models.CharField(max_length=100, unique=True)
    effect_type = models.CharField(max_length=10, choices=EFFECT_TYPE_CHOICES)
    attribute = models.CharField(max_length=20, choices=ATTRIBUTE_CHOICES)
    value = models.FloatField(help_text="1.2 = +20%, 0.8 = -20%")
    duration = models.IntegerField(help_text="На сколько ходов эффект действует")
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.effect_type})"
