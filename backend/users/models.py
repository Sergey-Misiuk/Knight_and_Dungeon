from django.db import models


class User(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    gold = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User {self.telegram_id}"
