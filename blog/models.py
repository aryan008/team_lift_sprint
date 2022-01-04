from django.db import models
from profiles.models import UserProfile


class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Post(models.Model):
    blog = models.ForeignKey(
        Blog, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    author = models.CharField(max_length=255)
    intro = models.TextField()
    article = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
