import graphene
from blog_service.graphql.schema import Query as AppQuery


class Query(AppQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)