import graphene

from management.queries import UserQuery, TeacherQuery
from management.mutations import JWTMutation


class Query(UserQuery, TeacherQuery, graphene.ObjectType):
    pass


class Mutation(JWTMutation, graphene.ObjectType):
    pass





