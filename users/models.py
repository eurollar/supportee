from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Custom user's model
    """
    CHOICES = [
        ('user', 'Client'),
        ('support', 'Support')
    ]

    type = models.CharField(max_length=15, choices=CHOICES, default='user')
