import graphene
from blog_service.graphql import types
from blog_service import models


class Query(graphene.AbstractType):

    posts = graphene.List(types.PostType)
    comments = graphene.List(types.CommentType)


    def resolve_posts(self, info, **kwargs):
        return models.PostModel.objects.all()

    def resolve_comments(self, info, **kwargs):
        return models.CommentModel.objects.all()
