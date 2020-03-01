from django.db import models


class CommentModel(models.Model):

    author = models.CharField(max_length=255, null=False, blank=False)
    text = models.TextField(null=False, blank=False)

    def __str__(self):
        return f'{self.author}'


class PostModel(models.Model):

    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    publish_date = models.DateTimeField(auto_now_add=True)

    author = models.CharField(max_length=255, null=False, blank=False)

    comments = models.ManyToManyField(CommentModel, blank=True)

    def __str__(self):
        return f'{self.title} - {self.author}'