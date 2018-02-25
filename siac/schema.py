import graphene

import management.schema
import subjects.schema
import questions.schema


class Query(management.schema.Query, subjects.schema.Query, questions.schema.Query, graphene.ObjectType):
    pass


class Mutation(management.schema.Mutation, questions.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
