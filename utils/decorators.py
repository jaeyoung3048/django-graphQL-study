from django.core.validators import ValidationError

from account.models.token import Token


def login_required(func):
    def wrapper(cls, root, info):
        try:
            auth_header = info.context.META.get('HTTP_AUTHORIZATION')

            token = auth_header.split(" ")[1]

            token_obj = Token.objects.get(token=token)

            if token_obj.user.is_authenticated:
                info.context.user = token_obj.user
            else:
                raise Token.DoesNotExist

        except Token.DoesNotExist:
            raise ValidationError('Authentication failed')
        except Exception as e:
            raise ValidationError(e)

        return func(cls, root, info)
    return wrapper