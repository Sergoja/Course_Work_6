# Generated by Django 4.2.2 on 2023-06-27 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[("member", "Пользователь"), ("admin", "Админ")],
                        default="member",
                        max_length=10,
                    ),
                ),
                ("phone", models.CharField(max_length=15)),
                ("image", models.ImageField(null=True, upload_to="logos/")),
                ("email", models.EmailField(max_length=50, unique=True)),
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
