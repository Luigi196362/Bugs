import graphene
import graphene
import graphql_jwt

# ...code
import users.schema
import Insectos.schema


class Query(users.schema.Query, Insectos.schema.Query, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation,Insectos.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
