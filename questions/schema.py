import graphene
from graphene_django import DjangoObjectType

from questions.models import Difficulty, Question, Option, Attachment


class DifficultyType(DjangoObjectType):
    class Meta:
        model = Difficulty


class Query(graphene.ObjectType):
    difficulty = graphene.Field(DifficultyType, id=graphene.String())
    difficulties = graphene.List(DifficultyType)

    def resolve_difficulty(self, info, id, **kwargs):
        return Difficulty.objects.get(pk=id)

    def  resolve_difficulties(self, info, **kwargs):
        return Difficulty.objects.all()
