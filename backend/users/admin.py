from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "telegram_id", "gold", "created_at")
    search_fields = ("telegram_id",)
    ordering = ("-created_at",)
