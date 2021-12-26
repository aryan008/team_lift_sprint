from django.shortcuts import render, redirect,\
    reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product
# Create your views here.


def view_bag(request):
    """ Render the shopping bag """

    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """ Add item and quantity to the shopping bag """

    # Get the product by the item ID
    product = get_object_or_404(Product, pk=item_id)
    # Integer request to get the quantity
    quantity = int(request.POST.get('quantity'))
    # Grab the form redirect URL
    redirect_url = request.POST.get('redirect_url')
    # Get the bag if it exists or initialise if not
    bag = request.session.get('bag', {})

    # If theres a key in the bag that matches the item ID
    if item_id in list(bag.keys()):
        # Increment the item ID quanitity to quantity
        bag[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        # The quantity is created as first instance
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    # Overwrite the session variable with bag and redirect
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Change quantity of the bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    # If quantity is above 0 set the item quantity
    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        # Remove the item from the bag
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """User can delete items from the bag"""
    bag = request.session.get('bag', {})
    product = get_object_or_404(Product, pk=item_id)

    try:
        # Try and remove the item from the bag and return status 200 response
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        # Error message that cannot remove item and 500 response
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
