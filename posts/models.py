from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=1024)
    publish_date = models.DateTimeField('publish date')

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=1024)
    publish_date = models.DateTimeField('publish date')

    def __str__(self):
        return self.content