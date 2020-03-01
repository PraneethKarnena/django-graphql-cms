from django.db import models


class PostModel(models.Model):

    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    publish_date = models.DateTimeField(auto_now_add=True)

    author = models.TextField(null=False, blank=False)

    def __str__(self):
        return f'{self.title} - {self.author}'