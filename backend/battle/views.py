from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from heroes.models import Character
from dungeon.models import CurrentRoom

import random


class AttackEnemyAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Временная заглушка: выбираем первого персонажа (добавишь позже выбор по telegram_id)
        character = Character.objects.get(name="Heroes")
        room = character.current_room

        if room.event_type != "Battle" or not room.enemy:
            return Response({"detail": "Сейчас не время для битвы."}, status=status.HTTP_400_BAD_REQUEST)

        # === Атака игрока ===
        # is_crit = random.random() < (character.crit_chance / 100)
        is_crit = random.random() < (100 / 100)
        player_damage = max(character.base_attack - room.enemy_defense, 1)
        if is_crit:
            player_damage *= 2
        room.enemy_hp = max(0, room.enemy_hp - player_damage)

        player_text = (
            f"🗡️ Вы нанесли {player_damage} урона (крит!)" if is_crit
            else f"🗡️ Вы нанесли {player_damage} урона"
        )

        # === Проверка, побеждён ли враг ===
        if room.enemy_hp == 0:
            room.is_cleared = True
            character.experience += room.enemy_exp
            character.count_room += 1
            character.save()
            room.save()

            return Response({
                "player_action": player_text,
                "enemy_action": "💀 Противник повержен!",
                "enemy_hp": 0,
                "player_hp": character.hp,
                "is_cleared": True,
                "exp_earned": room.enemy_exp,
            })
        print()
        print()
        print(random.random())
        print()
        print(random.random() < (room.enemy_crit_chance / 100))
        # === Ответный удар врага ===
        is_crit_enemy = random.random() < (room.enemy_crit_chance / 100)
        enemy_damage = max(room.enemy_attack - character.armor, 1)
        if is_crit_enemy:
            enemy_damage *= 2

        character.hp = max(0, character.hp - enemy_damage)
        character.save()
        room.save()

        enemy_text = (
            f"💢 Противник критует и наносит {enemy_damage} урона!"
            if is_crit_enemy else f"👊 Противник атакует и наносит {enemy_damage} урона."
        )

        if character.hp == 0:
            enemy_text += " ☠️ Вы пали в бою..."

        return Response({
            "player_action": player_text,
            "enemy_action": enemy_text,
            "enemy_hp": room.enemy_hp,
            "player_hp": character.hp,
            "is_cleared": False,
        })
