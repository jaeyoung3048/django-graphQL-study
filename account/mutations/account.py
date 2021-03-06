import graphene

from datetime import datetime, timedelta

from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.db import transaction

from account.models.user import User
from account.models.user_profile import Profile
from account.models.token import Token
from account.mutations.inputs import UserInput, UserProfileInput

from utils.jwt import encode_jwt


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
    access_token = graphene.String()
    refresh_token = graphene.String()

    @classmethod
    def mutate(cls, root, info, user_input):
        try:
            user_obj = User.objects.get(email=user_input.email)
            validate_password(user_input, user_obj)

            iat = datetime.now()
            exp = iat + timedelta(hours=1)

            access_token = encode_jwt({
                "token_type": "access",
                "email": user_input.email,
                "iat": iat.timestamp(),
                "exp": exp.timestamp(),
                "permission": {
                    "is_staff": user_input.is_staff,
                    "is_superuser": user_input.is_superuser
                }
            })

            exp = iat + timedelta(days=10)

            refresh_token = encode_jwt({
                "token_type": "refresh",
                "email": user_input.email,
                "iat": iat.timestamp(),
                "exp": exp.timestamp(),
                "permission": {
                    "is_staff": user_input.is_staff,
                    "is_superuser": user_input.is_superuser
                }
            })

            Token.objects.update(user=user_obj, token=refresh_token)

        except Exception as e:
            raise ValidationError(e)

        return cls(success=True, access_token=access_token, refresh_token=refresh_token)