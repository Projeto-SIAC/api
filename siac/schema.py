import graphene

import management.schema
import subjects.schema


class Query(management.schema.Query, subjects.schema.Query, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
