import graphene

from questions.queries import DifficultyQuery, QuestionQuery
from questions.mutations import DifficultyMutation, QuestionMutation


class Query(DifficultyQuery, QuestionQuery, graphene.ObjectType):
    pass

class Mutation(DifficultyMutation, QuestionMutation, graphene.ObjectType):
    pass
