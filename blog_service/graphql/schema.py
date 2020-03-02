import graphene
from blog_service.graphql import types, mutations
from blog_service import models


class Query(graphene.ObjectType):

    posts = graphene.List(types.PostType)
    post = graphene.Field(types.PostType, id=graphene.ID())

    comments = graphene.List(types.CommentType)


    def resolve_posts(self, *args, **kwargs):
        return models.PostModel.objects.all()

    def resolve_post(self, *args, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return models.PostModel.objects.get(pk=id)

        return

    def resolve_comments(self, *args, **kwargs):
        return models.CommentModel.objects.all()


class Mutation(graphene.ObjectType):
    create_post = mutations.CreatePost.Field()
    update_post = mutations.UpdatePost.Field()
    create_comment = mutations.CreateComment.Field()
