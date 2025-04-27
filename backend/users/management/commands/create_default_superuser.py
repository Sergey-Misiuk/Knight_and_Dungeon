from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from knight_dungeon.settings import conf

User = get_user_model()


class Command(BaseCommand):
    help = "Создание суперпользователя из переменных окружения."

    def handle(self, *args, **options):
        username = conf.superuser_username
        email = conf.superuser_email
        password = conf.superuser_password

        if not username or not email or not password:
            self.stdout.write(self.style.ERROR("❗ Не заданы переменные окружения для суперпользователя!"))
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f"⚠️ Суперпользователь '{username}' уже существует."))
        else:
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"✅ Суперпользователь '{username}' успешно создан!"))
