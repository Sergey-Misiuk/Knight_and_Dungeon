#!/bin/bash

echo "🔧 Применяем миграции..."
poetry run python manage.py migrate

echo "👑 Создаём суперпользователя (если ещё нет)..."
poetry run python manage.py create_default_superuser

echo "🛡 Загружаем баффы и дебаффы..."
poetry run python manage.py load_buffs

echo "🏰 Загружаем уровни сложности подземелий..."
poetry run python manage.py load_dungeon_difficulty

echo "👹 Загружаем врагов..."
poetry run python manage.py load_enemies

echo "✅ Всё готово!"
