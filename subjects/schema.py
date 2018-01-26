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
    subject = graphene.Field(SubjectType, id=graphene.UUID())
    subjects = graphene.List(SubjectType)
    topic = graphene.Field(TopicType, id=graphene.UUID())
    topics = graphene.List(TopicType)

    def resolve_subject(self, info, id, **kwargs):
        return Subject.objects.get(pk=id)

    def resolve_subjects(self, info, **kwargs):
        return Subject.objects.all()

    def resolve_topic(self, info, id, **kwargs):
        return Topic.objects.get(pk=id)

    def resolve_topics(self, info, **kwargs):
        return Topic.objects.all()
