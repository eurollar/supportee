from django.db import models
from users.models import CustomUser


class Ticket(models.Model):
    CHOICES = [
        ('solved', 'Solved tickets'),
        ('unsolved', 'Unsolved tickets'),
        ('frozen', 'Frozen tickets')
    ]
    title = models.CharField(max_length=250)
    text = models.TextField()
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='user'
    )
    status = models.CharField(
        max_length=15,
        choices=CHOICES,
        default='unsolved'
    )
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
