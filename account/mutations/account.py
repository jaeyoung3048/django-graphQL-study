import graphene

from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.db import transaction

from account.models.user import User
from account.models.user_profile import Profile
from account.models.token import Token
from account.mutations.inputs import UserInput, UserProfileInput


class RegisterMutation(graphene.Mutation):
    class Arguments:
        user_profile_input = UserProfileInput(required=True)

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, user_profile_input):
        user_data = user_profile_input.user

        try:
            with transaction.atomic():
                user_obj = User.objects.create(**user_data)
                validate_password(user_data.password, user_obj)
                user_obj.set_password(user_data.password)

                user_obj.save()

                user_profile_input['user'] = user_obj

                Profile.objects.update_or_create(user_profile_input)
        except Exception as e:
            raise ValidationError(e)

        return cls(success=True)


class SigninMutation(graphene.Mutation):
    class Arguments:
        user_input = UserInput(required=True)

    success = graphene.Boolean()
    token = graphene.String()