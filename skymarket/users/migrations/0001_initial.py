# Generated by Django 4.2.1 on 2023-06-07 12:46

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
                    "role",
                    models.CharField(
                        choices=[("member", "Пользователь"), ("admin", "Админ")],
                        default="member",
                        max_length=10,
                    ),
                ),
                ("phone", models.CharField(max_length=15)),
                ("last_login", models.DateTimeField(auto_now_add=True)),
                ("image", models.ImageField(null=True, upload_to="logos/")),
                ("email", models.EmailField(max_length=50, unique=True)),
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
