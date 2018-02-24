import graphene
from graphene_django import DjangoObjectType

from questions.models import Difficulty, Question, Option, Attachment
from management.resolvers import resolve_user
from management.types import TeacherType


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

    created_by = graphene.Field(TeacherType)

    class Meta:
        model = Question

    def resolve_created_by(self, info, **kwargs):
        return resolve_user(self.created_by)
