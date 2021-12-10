from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "No bag items present!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': "pk_test_51JM7mPDe72c6JjEfoZgon625e1JTEK1nlpZgMqySjU0cWxN0T6qwTf7o5HHPdFr9js91ywP1dViwnCW9pJXYYRZf00avZVLRdD",
        'client_secret': "test client secret",
    }

    return render(request, template, context)
