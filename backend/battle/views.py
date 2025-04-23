from django.http import HttpResponse


def index(request):
    """
    Функция отображения домашней страницы
    """

    return HttpResponse("⚔️ Knight & Dungeon — сервер работает!")