import graphene
from blog_service.graphql import types
from blog_service import models


class Query(graphene.AbstractType):

    posts = graphene.List(types.PostType)
    post = graphene.Field(types.PostType, id=graphene.Int())

    comments = graphene.List(types.CommentType)


    def resolve_posts(self, info, **kwargs):
        return models.PostModel.objects.all()

    def resolve_post(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return models.PostModel.objects.get(pk=id)

        return

    def resolve_comments(self, info, **kwargs):
        return models.CommentModel.objects.all()
