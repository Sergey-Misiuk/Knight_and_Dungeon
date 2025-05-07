from django.urls import path
from heroes.views import CreateCharacterView

urlpatterns = [
    path('character/create/', CreateCharacterView.as_view(), name='create_character'),
]