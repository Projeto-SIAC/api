import graphene

from questions.queries import DifficultyQuery, QuestionQuery


class Query(DifficultyQuery, QuestionQuery, graphene.ObjectType):
    pass
