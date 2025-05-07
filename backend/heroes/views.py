from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from heroes.models import Character
from users.models import User
from dungeon.models import DungeonDifficulty
from heroes.serializers import CharacterSerializer


class CreateCharacterView(APIView):
    def post(self, request):
        telegram_id = request.data.get("telegram_id")
        character_name = request.data.get("character_name")
        difficulty_name = request.data.get("difficulty")

        if not character_name or not difficulty_name:
            return Response({"error": "Укажите имя пользователя и сложность."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(telegram_id=telegram_id)
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)

        try:
            difficulty = DungeonDifficulty.objects.get(name=difficulty_name)
        except DungeonDifficulty.DoesNotExist:
            return Response({"error": "Сложность не найдена."}, status=status.HTTP_404_NOT_FOUND)

        if hasattr(user, 'character'):
            return Response({"error": "У пользователя уже есть персонаж."}, status=status.HTTP_400_BAD_REQUEST)

        character = Character.objects.create(
            user=user,
            name=character_name,
            difficulty=difficulty,
            max_hp=100,
            hp=100,
            base_attack=10,
            armor=5,
        )

        serialized_character = CharacterSerializer(character)

        return Response({
            "message": "Персонаж успешно создан.",
            "character": serialized_character.data
        }, status=status.HTTP_201_CREATED)
