from rest_framework import serializers
from dungeon.models import CurrentRoom


class CurrentRoomSerializer(serializers.ModelSerializer):
    event_text = serializers.SerializerMethodField()
    event_result = serializers.SerializerMethodField()

    class Meta:
        model = CurrentRoom
        fields = [
            "id",
            "character",
            "event_type",
            "enemy",
            "is_cleared",
            "created_at",
            "event_text",
            "event_result",
        ]

    def get_event_text(self, obj):
        return self.context.get("event_text")

    def get_event_result(self, obj):
        return self.context.get("event_result")