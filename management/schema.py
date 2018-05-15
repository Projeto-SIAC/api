import graphene

from management.queries import UserQuery, TeacherQuery
from management.mutations import UserMutation, JWTMutation


class Query(UserQuery, TeacherQuery, graphene.ObjectType):
    pass


class Mutation(UserMutation, JWTMutation, graphene.ObjectType):
    pass
