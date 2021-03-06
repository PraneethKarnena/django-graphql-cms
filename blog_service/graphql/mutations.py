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


class UpdatePost(graphene.Mutation):

    post = graphene.Field(types.PostType)

    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String(required=False)
        description = graphene.String(required=False)
        author = graphene.String(required=False)
        publish_date = graphene.DateTime(required=False)

    def mutate(self, *args, **kwargs):
        post_id = kwargs.get('id')
        title = kwargs.get('title')
        description = kwargs.get('description')
        author = kwargs.get('author')
        publish_date = kwargs.get('publish_date')

        post = models.PostModel.objects.get(pk=post_id)

        if title is not None:
            post.title = title

        if description is not None:
            post.description = description

        if author is not None:
            post.author = author

        if publish_date is not None:
            post.publish_date = publish_date

        post.save()

        return CreatePost(post=post)


class CreateComment(graphene.Mutation):

    comment = graphene.Field(types.CommentType)

    class Arguments:
        post_id = graphene.ID(required=True)
        text = graphene.String(required=True)
        author = graphene.String(required=True)

    def mutate(self, *args, **kwargs):
        text = kwargs.get('text')
        author = kwargs.get('author')
        post_id = kwargs.get('post_id')

        post = models.PostModel.objects.get(pk=post_id)
        comment = models.CommentModel.objects.create(text=text, author=author)

        post.comments.add(comment)
        post.save()

        return CreateComment(comment=comment)


class DeleteComment(graphene.Mutation):

    comment = graphene.Field(types.CommentType)

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, *args, **kwargs):
        id = kwargs.get('id')
        _ = models.CommentModel.objects.get(pk=id).delete()

        return
