import graphene
from graphene_django import DjangoObjectType

from questions.models import Difficulty, Question, Option, Attachment


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

    class Meta:
        model = Question


class Query(graphene.ObjectType):
    difficulty = graphene.Field(DifficultyType, id=graphene.UUID())
    difficulties = graphene.List(DifficultyType)

    question = graphene.Field(QuestionType, id=graphene.UUID())
    questions = graphene.List(QuestionType)

    def resolve_difficulty(self, info, id, **kwargs):
        return Difficulty.objects.get(pk=id)

    def  resolve_difficulties(self, info, **kwargs):
        return Difficulty.objects.all()

    def resolve_question(self, info, id, **kwargs):
        return Question.objects.get(pk=id)

    def resolve_questions(self, info, **kwargs):
        return Question.objects.all()
