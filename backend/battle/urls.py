from django.contrib import admin
from django.urls import path
from battle.views import RoomEnterAPIView, index

urlpatterns = [
    path('', index, name='index'),
    path('room/enter/', RoomEnterAPIView.as_view(), name='room_enter'),
]