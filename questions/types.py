import graphene
from graphene_django import DjangoObjectType

from questions.models import Difficulty, Question, Option, Attachment

from management.types import TeacherType
from management.resolvers import resolve_user

from subjects.types import TopicType
from subjects.resolvers import resolve_topics


class DifficultyType(DjangoObjectType):

    class Meta:
        model = Difficulty


class OptionType(DjangoObjectType):

    class Meta:
        model = Option


class AttachmentType(DjangoObjectType):

    class Meta:
        model = Attachment


class QuestionType(DjangoObjectType):

    topics = graphene.List(TopicType)
    created_by = graphene.Field(TeacherType)
    is_subjective = graphene.Boolean(source='is_subjective')

    class Meta:
        model = Question

    def resolve_created_by(self, info, **kwargs):
        return resolve_user(self.created_by)

    def resolve_topics(self, info, **kwargs):
        topics = [t.topic for t in self.questiontopic_set.all()]
        return resolve_topics(topics)
