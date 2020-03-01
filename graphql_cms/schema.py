import graphene
from blog_service.graphql.schema import Query as AppQuery
from blog_service.graphql.schema import Mutation as AppMutation


class Query(AppQuery, graphene.ObjectType):
    pass


class Mutation(AppMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)