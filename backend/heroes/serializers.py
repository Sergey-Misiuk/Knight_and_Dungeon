from rest_framework import serializers
from heroes.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    difficulty = serializers.StringRelatedField()

    class Meta:
        model = Character
        fields = [
            "id",
            "name",
            "level",
            "experience",
            "skill_points",
            "current_room",
            "difficulty",
            "max_hp",
            "hp",
            "base_attack",
            "armor",
            "is_alive",
        ]
