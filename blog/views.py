from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


def blog(request):
    """ Display all blog posts """

    # Grab all the blog posts
    blog_posts = Post.objects.all()
    template = 'blog/blog.html'
    context = {
        'blog_posts': blog_posts,
    }
    return render(request, template, context)


def post_detail(request, slug):
    """ Show the full post including intro and article """
    # Get the specific post with id of slug
    post = Post.objects.get(slug=slug)

    template = 'blog/post_detail.html'
    context = {
        'post': post,
    }

    return render(request, template, context)


@login_required
def add_post(request):
    """ Add blog post """
    # Superuser requirement
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the storeowner can do this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        # Grab the postform
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Save on validity
            post = form.save()
            messages.success(request, 'Successfully added a blog entry!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(
                request, 'Post failure, ensure your entry is correct.')
    else:
        form = PostForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, slug):
    """ Edit an existing blog entry """
    # Superuser requirement
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the storeowner can do this.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        # Grab the postform
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            # Save on validity
            form.save()
            messages.success(request, 'Successfully updated blog post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(
                request, 'Blog edit failure, ensure your entry is correct.')
    else:
        form = PostForm(instance=post)
        messages.info(
            request, f'You are editing the "{post.title}" blog entry')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, slug):
    """ Delete blog post """
    # Superuser requirement
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the storeowner can do this.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    # Delete the entry
    post.delete()
    messages.success(request, 'entry deleted!')
    return redirect(reverse('blog'))
