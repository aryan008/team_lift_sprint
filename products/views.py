from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import F, Q
from django.db.models.functions import Lower

from .models import Product, Category, ReviewProduct
from .forms import ProductForm, ReviewForm

# Create your views here.


def all_products(request):
    """ A view to show all products including search queries """
    products = Product.objects.all()
    # set initial query and categories to None
    query = None
    categories = None
    sort = None
    direction = None

    # If a get request, sort by name and direction
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # set up category dropdown for navbar
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # set up search request for search bar
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria")
                return redirect(reverse('products'))

            # set up queries variable to handle name or description
            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
        }
    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm()
    # Set the automatic availability of product review to true
    can_add_review = True

    """ Help with product review sourced through:
    https://www.youtube.com/watch?app=desktop&v=Y5vvGQyHtpM
    """
    # The users product review
    if request.user.is_authenticated:
        # Count how many reviews this person has left on this product
        check_review = ReviewProduct.objects.filter(
            user=request.user, product=product).count()
        # If above 0, they cant add a review but old review shown
        if check_review > 0:
            can_add_review = False
            review = get_object_or_404(
                ReviewProduct, product=product, user=request.user)
            form = ReviewForm(instance=review)

    if request.method == 'POST' and request.user.is_authenticated:
        # Grab the variables
        review_star_rating = request.POST.get('review_star_rating', '')
        review_text_field = request.POST.get('review_text_field', '')
        # Create the review object
        review = ReviewProduct.objects.create(
            product=product, user=request.user,
            review_star_rating=review_star_rating,
            review_text_field=review_text_field)

        messages.success(request, f"{ review.user }'s review of { review.product} has been \
        successful.")
        return redirect(reverse('product_detail', args=[product.id]))

    # Get the reviews of this product
    reviews = ReviewProduct.objects.filter(product=product)

    # Get number of reviews
    number_of_reviews = ReviewProduct.objects.filter(product=product).count()

    context = {
        'product': product,
        'form': form,
        'can_add_review': can_add_review,
        'reviews': reviews,
        'number_of_reviews': number_of_reviews,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def delete_review(request, review_id):
    """ Delete a review """
    if not request.user.is_authenticated:
        # Error message if not superuser
        messages.error(request, 'Sorry, only logged in users can do that.')
        return redirect(reverse('home'))

    elif request.user.is_authenticated:
        review = ReviewProduct.objects.filter(pk=review_id).last()
        product_id = review.product_id
        # Delete the review
        review.delete()
        messages.success(request, f"{ review.user }'s review of { review.product} has been \
        deleted.")
        return redirect(reverse('product_detail', args=[product_id]))


def on_sale(request):
    """ A view to show products that are on sale. """
    products = Product.objects.filter(on_sale=True)
    sort = None
    direction = None

    # If a get request, sort by name and direction
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/on_sale.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    # Error message if not superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    # Post request if statement
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form is valid and redirect
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            # Error message if post action fails
            messages.error(request, 'Failed to add product.\
                Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        # Error message if not superuser
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            # Save the form is valid and redirect
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            # Error message if post action fails
            messages.error(request, 'Failed to update product.\
                Please ensure the form is valid.')
    else:
        # Form var for product form model for specific product
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        # Error message if not superuser
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    # Delete the product
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
