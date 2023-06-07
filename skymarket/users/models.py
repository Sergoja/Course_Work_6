from datetime import date

from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.db.models import TextChoices

from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles(TextChoices):
    USER = "member", "Пользователь"
    ADMIN = "admin", "Админ"


class User(AbstractBaseUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    role = models.CharField(
        max_length=10,
        choices=UserRoles.choices,
        default=UserRoles.USER)
    phone = models.CharField(max_length=15)
    last_login = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='logos/', null=True)
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    @property
    def is_admin(self):
        if self.role == "admin":
            return True

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    objects = UserManager()
