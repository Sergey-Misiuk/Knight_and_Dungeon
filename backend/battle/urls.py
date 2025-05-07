from django.contrib import admin
from django.urls import path
from battle.views import AttackEnemyAPIView

urlpatterns = [
    # path('', index, name='index'),
    # path('room/enter/', RoomBattleEnterAPIView.as_view(), name='room_enter'),
    path('attack/', AttackEnemyAPIView.as_view(), name='attack_enemy'),
]