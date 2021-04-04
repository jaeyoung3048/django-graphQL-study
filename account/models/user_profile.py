from django.db import models

from account.models.user import User


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        related_name='user_profile',
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=50
    )

    birth = models.DateField()