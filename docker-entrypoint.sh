#!/bin/sh

echo "📦 Collect static files"
poetry run python manage.py collectstatic --noinput

echo "📌 Apply database migrations"
poetry run python manage.py migrate

echo "👑 Create superuser (if not exists)"
poetry run python manage.py createsuperuser --noinput || true

echo "🚀 Starting gunicorn server"
poetry run gunicorn -b 0.0.0.0:8000 knight_dungeon.wsgi:application
