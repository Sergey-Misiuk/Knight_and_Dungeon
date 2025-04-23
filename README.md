<h1 align="center">🏰 Knight & Dungeon</h1>
<p align="center">⚔️ Telegram Web Game — Исследуй подземелья, побеждай врагов и управляй своим героем!</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.11-blue?logo=python">
  <img src="https://img.shields.io/badge/Django-5.2-success?logo=django">
  <img src="https://img.shields.io/badge/docker-compose-blue?logo=docker">
</p>

---

## 🚀 Быстрый старт

```bash
git clone https://github.com/your_username/Knight_and_Dungeon.git
cd Knight_and_Dungeon
cp .env.example .env
docker-compose up --build
```

🛡️ Админка: [http://localhost/admin/](http://localhost/admin/)  
🏹 Главная: [http://localhost/](http://localhost/)

---

## ⚙️ Технологии

- 🐍 Python 3.11 + Django 5.2
- 🐘 PostgreSQL 16
- 🐳 Docker + docker-compose
- 🔥 Gunicorn + Nginx
- 📦 Pydantic + Poetry
- 🧙 Django Admin
- 🎮 (Скоро) Phaser.js Frontend
- 💬 Telegram Web App Integration

---


## 🔐 .env (пример)

```env
DEBUG=True
SECRET_KEY=django-insecure-...

PRIMARY_DATABASE_URL=postgresql://knight_user:knight_pass@postgresql:5432/knight_db
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
```

---

## 🛠 Полезные команды

```bash
# Запуск проекта
docker-compose up --build

# Миграции и суперюзер
docker-compose exec backend poetry run python manage.py migrate
docker-compose exec backend poetry run python manage.py createsuperuser

# Собрать статику
docker-compose exec backend poetry run python manage.py collectstatic
```

---

## 📝 Лицензия

MIT — свободно используй, изучай и расширяй 🚀

---
<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzhjM2I3OTkzZGU0Y2JjNDYwMzA2NTYwZGE0YmFkNmNmYzdmMzE0YyZjdD1n/pxMy6cKpDLUmc/giphy.gif" width="200">
  <br><strong>Добро пожаловать в подземелье!</strong>
</p>
