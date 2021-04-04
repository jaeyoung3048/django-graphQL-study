import graphene

from graphene_django.types import DjangoObjectType

from account.models.user import User


class UserInfoType(DjangoObjectType):
    class Meta:
        model = User
        fields = ["email", "is_staff", "is_superuser"]

