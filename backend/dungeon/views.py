from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dungeon.utils.room_logic import process_room_event
from heroes.models import Character
from enemies.models import Enemy, EnemyStats
from dungeon.models import CurrentRoom, RoomEventType
from dungeon.serializers import CurrentRoomSerializer

import random


class EnterRoomAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Тестово: пока берём первого персонажа (потом сделать по telegram_id!!!!!!!)
        character = Character.objects.get(name="Heroes")

        CurrentRoom.objects.filter(character=character).delete()

        event_type = random.choices(
            [
                RoomEventType.BATTLE,
                RoomEventType.CHEST,
                RoomEventType.BUFF,
                RoomEventType.DEBUFF,
                RoomEventType.TRAP,
                RoomEventType.EMPTY,
            ],
            weights=[40, 25, 10, 10, 5, 10],
            k=1
        )[0]

        enemy_stats = None
        event_text = None
        event_result = None
        room = None

        if event_type in ["Chest", "Buff", "Debuff", "Trap", "Empty"]:
            event_text, event_result = process_room_event(character, event_type)
            room = CurrentRoom.objects.create(
                character=character,
                event_type=event_type,
                enemy=enemy_stats,
                enemy_hp=None,
                enemy_attack=None,
                enemy_defense=None,
                enemy_crit_chance=None,
                enemy_exp=None,
            )
 
        elif event_type == RoomEventType.BATTLE:
            if character.count_room >= character.difficulty.rooms_before_boss:
                available_enemies = Enemy.objects.filter(is_boss=True)
            else:
                available_enemies = Enemy.objects.filter(is_boss=False)

            base_enemy = random.choice(list(available_enemies))
            enemy_stats = EnemyStats.objects.get(enemy=base_enemy, difficulty=character.difficulty)
        
            room = CurrentRoom.objects.create(
                character=character,
                event_type=event_type,
                enemy=enemy_stats,
                enemy_hp=enemy_stats.final_hp(),
                enemy_attack=enemy_stats.final_attack(),
                enemy_defense=enemy_stats.final_defense(),
                enemy_crit_chance=enemy_stats.final_crit_chance(),
                enemy_exp=enemy_stats.final_exp_reward(),
            )

        serializer = CurrentRoomSerializer(
            room,
            context={"event_text": event_text, "event_result": event_result}
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
