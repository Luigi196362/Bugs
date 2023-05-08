import graphene
import users.schema
import Insectos.schema


class Query(users.schema.Query, Insectos.schema.Query, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation,Insectos.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
