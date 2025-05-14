from django.urls import path
from items.views import EquipeWeaponView

urlpatterns = [
    path('character/equip_weapon/', EquipeWeaponView.as_view(), name='equip_weapon'),
]