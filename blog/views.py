from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


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


def edit_post(request, slug):
    """ Edit an existing Post """

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(
                request, 'Failed to update blog post. Check if form is valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title} blog entry')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)
