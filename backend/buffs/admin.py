from django.contrib import admin
from .models import BuffDebuff


@admin.register(BuffDebuff)
class BuffDebuffAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "effect_type", "attribute", "value", "duration")
    list_filter = ("effect_type", "attribute")
    search_fields = ("name",)
