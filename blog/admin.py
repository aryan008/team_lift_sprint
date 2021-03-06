from django.contrib import admin
from .models import Blog, Post

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    """ Admin blog class """
    list_display = (
        'title',
    )


class PostAdmin(admin.ModelAdmin):
    """ Admin post class """
    list_display = (
        'title',
        'intro',
        'article',
        'date_added',
        'author'
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Blog, BlogAdmin)
