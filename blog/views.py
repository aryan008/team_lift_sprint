from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post


def blog(request):
    """ BLog page to display all available posts """

    posts = Post.objects.all()
    template = 'blog/blog.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def post_detail(request, slug):
    """ Display each Post in detail along with its comments """
    post = Post.objects.get(slug=slug)

    template = 'blog/post_detail.html'
    context = {
        'post': post,
    }

    return render(request, template, context)