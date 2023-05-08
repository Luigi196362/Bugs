import graphene

import Insectos.schema


class Query(Insectos.schema.Query, graphene.ObjectType):
    pass

class Mutation(Insectos.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
