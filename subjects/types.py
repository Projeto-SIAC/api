from graphene_django import DjangoObjectType

from subjects.models import Subject, Topic


class SubjectType(DjangoObjectType):
    class Meta:
        model = Subject


class TopicType(DjangoObjectType):
    class Meta:
        model = Topic
