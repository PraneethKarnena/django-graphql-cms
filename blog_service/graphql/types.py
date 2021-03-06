from graphene_django import DjangoObjectType
from blog_service import models


class PostType(DjangoObjectType):

    class Meta:
        model = models.PostModel


class CommentType(DjangoObjectType):

    class Meta:
        model = models.CommentModel