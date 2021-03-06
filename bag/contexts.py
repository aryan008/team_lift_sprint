from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    # Get bag if it exists or else initialise it
    bag = request.session.get('bag', {})
    # For loop to get the total price, product sum and savings made if on sale
    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        # If statement for products on sale
        if product.on_sale is True:
            total += quantity * Decimal(
                product.price * (
                    100 - product.discount_on_product) / 100).quantize(
                        Decimal('0.00'))
            product_total = quantity * Decimal(
                product.price * (
                    100 - product.discount_on_product) / 100).quantize(
                        Decimal('0.00'))
            product_saving = Decimal(product.price * (
                product.discount_on_product / 100)).quantize(
                        Decimal('0.00')) * quantity
        else:
            # Else block if product not on sale
            total += quantity * product.price
            product_total = quantity * product.price
            product_saving = 0

        product_count += quantity
        # Appendation of above items to initialised/ready bag
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'product_total': product_total,
            'product_saving': product_saving,
        })

    # If statement to determine if customer is entitled to free shipping
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
