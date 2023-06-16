import graphene
import graphql_jwt
import Insectos.schema
import users.schema
import myapp.schema


class Query(myapp.schema.Query,users.schema.Query, Insectos.schema.Query, graphene.ObjectType):
    pass

class Mutation(myapp.schema.Mutation,users.schema.Mutation,Insectos.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
