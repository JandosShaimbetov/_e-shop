from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="email", max_length=255, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    first_name = models.CharField(max_length=255, verbose_name="first_name")
    last_name = models.CharField(max_length=255, verbose_name="last_name")
    address = models.CharField(
        max_length=255, verbose_name="address", null=True, blank=True
    )
    phone = models.CharField(
        max_length=255, verbose_name="phone", null=True, blank=True
    )

    def __str__(self):
        return self.email
