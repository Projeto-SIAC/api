import graphene

from management.queries import UserQuery, TeacherQuery
from management.mutations import JWTMutation
import management.mutations


class Query(UserQuery, TeacherQuery, graphene.ObjectType):
    pass


class Mutation(management.mutations.Mutation, JWTMutation , graphene.ObjectType):
    pass
