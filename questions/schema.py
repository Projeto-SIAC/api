import graphene

from questions.queries import LevelQuery, QuestionQuery
from questions.mutations import LevelMutation, QuestionMutation


class Query(LevelQuery, QuestionQuery, graphene.ObjectType):
    pass

class Mutation(LevelMutation, QuestionMutation, graphene.ObjectType):
    pass
