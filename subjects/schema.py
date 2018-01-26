import graphene
from graphene_django import DjangoObjectType

from subjects.models import Subject, Topic


class SubjectType(DjangoObjectType):
    class Meta:
        model = Subject


class TopicType(DjangoObjectType):
    class Meta:
        model = Topic


class Query(graphene.ObjectType):
    subjects = graphene.List(SubjectType)
    topics = graphene.List(TopicType)

    def resolve_subjects(self, info, **kwargs):
        return Subject.objects.all()

    def resolve_topics(self, info, **kwargs):
        return Topic.objects.all()
