from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from heroes.models import Character
from items.utils.equip_weapon_or_armor import equip_armor, equip_weapon
from items.models import Weapon


class EquipeWeaponView(APIView):
    def post(self, request):
        character = Character.objects.get(name="Heroes")

        new_weapon = Weapon.objects.get(name="ГИГА")
        equip_weapon(character, new_weapon)

        return Response(
            {
                "message": "Оружие успешно экипировано.",
            },
            status=status.HTTP_201_CREATED,
        )
