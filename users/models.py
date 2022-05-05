from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    CHOICES = [
        ('user', 'Пользователь'),
        ('support', 'Саппорт')
    ]

    type = models.CharField(max_length=15, choices=CHOICES, default='user')
