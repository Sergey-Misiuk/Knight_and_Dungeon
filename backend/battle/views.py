from django.http import HttpResponse

from dungeon.utils.generate_room import RoomEventGenerator as room_generate
from heroes.models import Character

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



def index(request):
    """
    Функция отображения домашней страницы
    """
    player = Character.objects.get(name="Test")
    
    dis = room_generate(character=player)
    res = dis.choose_event_type()
    disc = dis.generate_event()
    return HttpResponse(f"⚔️ Knight & Dungeon — сервер работает!Произошел ивент {player} - {disc}")


class RoomEnterAPIView(APIView):
    """
    API для входа в комнату и генерации события.
    """

    def post(self, request, *args, **kwargs):
        # Tестовый вариант, напрямую прокидываем игрока
        character_id = request.data.get("character_id")
        character_name = request.data.get("character_name")

        if not character_id or not character_name:
            return Response({"error": "Character ID or Name is required"}, status=400)

        try:
            character = Character.objects.get(id=character_id)
        except Character.DoesNotExist:
            return Response({"error": "Character not found"}, status=404)

        generator = room_generate(character)
        handler_event = generator.generate_event()

        return Response({
            "text": handler_event["event_text"],
            "description": handler_event["system_text"],
        }, status=status.HTTP_200_OK)
