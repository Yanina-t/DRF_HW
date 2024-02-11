from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
