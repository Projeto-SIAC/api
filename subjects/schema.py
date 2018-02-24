import graphene
from graphene_django import DjangoObjectType

from subjects.queries import SubjectQuery, TopicQuery


class Query(SubjectQuery, TopicQuery, graphene.ObjectType):
    pass
