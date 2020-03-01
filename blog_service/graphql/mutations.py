import graphene
from blog_service.graphql import types
from blog_service import models


class CreatePost(graphene.Mutation):

    post = graphene.Field(types.PostType)

    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        author = graphene.String(required=True)
        publish_date = graphene.DateTime(required=False)

    def mutate(self, *args, **kwargs):
        title = kwargs.get('title')
        description = kwargs.get('description')
        author = kwargs.get('author')
        publish_date = kwargs.get('publish_date')

        post = models.PostModel.objects.create(
            title=title,
            description=description,
            author=author,
        )

        if publish_date is not None:
            post.publish_date = publish_date
            post.save()

        return CreatePost(post=post)

