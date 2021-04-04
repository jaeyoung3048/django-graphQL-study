import jwt

from django.conf import settings


def encode_jwt(data):
    return jwt.encode(data, settings.SECRET_KEY, algorithm="HS256")


def decode_jwt(access_token):
    return jwt.decode(
        access_token,
        settings.SECRET_KEY,
        algorithms=["HS256"],
        options={"verify_aud": False},
    )
