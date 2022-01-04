from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post


def blog(request):
    """ BLog page to display all available posts """

    template = 'blog/blog.html'

    return render(request, template)
