from django.contrib import admin
from django.urls import path
from dungeon.views import EnterRoomAPIView

urlpatterns = [
    # path('room/enter/', RoomEnterAPIView.as_view(), name='room_enter'),
    path('create/current_room/', EnterRoomAPIView.as_view(), name='create_current_room'),
]