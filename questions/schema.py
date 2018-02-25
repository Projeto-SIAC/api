import graphene

from questions.queries import DifficultyQuery, QuestionQuery
import questions.mutations


class Query(DifficultyQuery, QuestionQuery, graphene.ObjectType):
    pass

class Mutation(questions.mutations.Mutation, graphene.ObjectType):
    pass
