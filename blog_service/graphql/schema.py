import graphene
from blog_service.graphql import types
from blog_service import models


class Query(graphene.AbstractType):

    posts = graphene.List(types.PostType)


    def resolve_posts(self, **kwargs):
        return models.PostModel.objects.all()

