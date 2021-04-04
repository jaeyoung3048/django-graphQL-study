import graphene

from account.models.user_profile import Profile
from account.models.user import User
from account.schema import UserInfoType, UserProfileType

from utils.decorators import login_required


class Query(graphene.ObjectType):
    get_user_info = graphene.Field(UserInfoType)
    get_user_profile_get = graphene.Field(UserProfileType)

    @classmethod
    @login_required
    def resolve_get_user_info(cls, root, info):
        return info.context.user

    @classmethod
    @login_required
    def resolve_get_user_profile_info(clsc, root, info):

        user_obj = info.context.user

        return Profile.objects.get(user=user_obj)