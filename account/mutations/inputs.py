import graphene


class UserInput(graphene.InputObjectType):
    email = graphene.String(required=True)
    password = graphene.String(required=True)


class UserProfileInput(graphene.InputObjectType):
    user = UserInput(required=True)
    name = graphene.String(required=True)
    birth = graphene.Date(required=True)
