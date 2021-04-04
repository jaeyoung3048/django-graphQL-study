import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):

    uid = models.UUIDField(
        unique=True,
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )

    email = models.EmailField(
        unique=True,
        max_length=128,
    )

    is_staff = models.BooleanField(
        default=False
    )

    is_superuser = models.BooleanField(
        default=False
    )


    EMAIL_FIELDS = 'email'
    USERNAME_FIELD = 'email'

    class Meta:
        db_table = "Account.U"
