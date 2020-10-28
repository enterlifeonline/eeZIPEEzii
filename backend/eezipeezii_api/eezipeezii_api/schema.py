import graphene
import graphql_jwt

import jobs.schema
import users.schema
import applications.schema
import profiles.schema


class Query(users.schema.Query, jobs.schema.Query, applications.schema.Query, profiles.schema.Query, graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, jobs.schema.Mutation, applications.schema.Mutation, profiles.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
