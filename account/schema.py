from graphene_django.types import DjangoObjectType

from account.models.user import User
from account.models.user_profile import Profile


class UserInfoType(DjangoObjectType):
    class Meta:
        model = User
        fields = ["email", "is_staff", "is_superuser"]


class UserProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = "__all__"
