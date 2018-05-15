import graphene

from subjects.queries import SubjectQuery, TopicQuery
from subjects.mutations import SubjectMutation


class Query(SubjectQuery, TopicQuery, graphene.ObjectType):
    pass


class Mutation(SubjectMutation, graphene.ObjectType):
    pass
