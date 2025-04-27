#!/bin/bash

echo "🔧 Применяем миграции..."
poetry run python manage.py migrate

echo "👑 Создаём суперпользователя (если ещё нет)..."
poetry run python manage.py createsuperuser --noinput || true

echo "🛡 Загружаем баффы и дебаффы..."
poetry run python manage.py load_buffs

echo "🛡 Загружаем сложность подземелий..."
poetry run python manage.py load_dungeon_difficulty

echo "✅ Всё готово!"
