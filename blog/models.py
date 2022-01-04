from django.db import models


"""
Blog class credit for inspiration:
(1) - https://dev.to/madhubankhatri/blog-website-using-django-55ji
    - Madhuban Khatri
(2) - https://www.youtube.com/watch?app=desktop&v=GcqURKYfv00
    - CodingWithMitch
"""


class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Post(models.Model):
    class Meta:
        ordering = ['-date_added']

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
