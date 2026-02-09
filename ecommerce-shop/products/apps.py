from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
import os


def create_admin(sender, **kwargs):
    User = get_user_model()

    username = os.environ.get("ADMIN_USERNAME")
    password = os.environ.get("ADMIN_PASSWORD")
    email = os.environ.get("ADMIN_EMAIL", "")

    if not username or not password:
        return

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            password=password,
            email=email,
        )


class ProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "products"

    def ready(self):
        post_migrate.connect(create_admin, sender=self)
