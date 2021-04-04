from django.db import models

from account.models.user import User


class Token(models.Model):
    token = models.TextField()

    user = models.OneToOneField(
        User,
        related_name='token',
        on_delete=models.CASCADE,
        primary_key=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )