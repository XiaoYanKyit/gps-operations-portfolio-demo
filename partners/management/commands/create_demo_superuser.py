
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create the portfolio demo admin account if needed."

    def handle(self, *args, **options):
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        if not all([username, email, password]):
            raise CommandError(
                "Demo admin environment variables are missing."
            )

        User = get_user_model()

        if User.objects.filter(username=username).exists():
            self.stdout.write("Demo admin already exists.")
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )

        self.stdout.write(
            self.style.SUCCESS("Demo admin created successfully.")
        )
