from django.db import models

from account.models.user import User


class Token(models.Model):
    token = models.TextField()
    user = models.OneToOneField(
        User,
        related_name='token',
        on_delete=models.CASCADE
    )