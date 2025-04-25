from django.db import models


class DungeonDifficulty(models.Model):
    name = models.CharField(max_length=50)
    exp_multiplier = models.FloatField()
    rooms_before_boss = models.IntegerField()
    bonus_exp_chest = models.IntegerField(default=5)
    bonus_exp_buff = models.IntegerField(default=3)

    def __str__(self):
        return self.name
