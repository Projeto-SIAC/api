import graphene
from subjects.models import Subject, Topic
from subjects.types import SubjectType, TopicType


class TopicQuery(graphene.ObjectType):
    topic = graphene.Field(TopicType, id=graphene.UUID())
    topics = graphene.List(TopicType)

    def resolve_topic(self, info, id, **kwargs):
        return Topic.objects.get(pk=id)

    def resolve_topics(self, info, **kwargs):
        return Topic.objects.all()


class SubjectQuery(graphene.ObjectType):
    subject = graphene.Field(SubjectType, id=graphene.UUID())
    subjects = graphene.List(SubjectType)

    def resolve_subject(self, info, id, **kwargs):
        return Subject.objects.get(pk=id)

    def resolve_subjects(self, info, **kwargs):
        return Subject.objects.all()
