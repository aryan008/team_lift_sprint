from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from products.models import Product

from django.contrib import messages
from .models import Wishlist

# Create your views here.


def wishlist(request):
    """
    A view to render the user's wishlist
    """

    return render(request, 'wishlist/wishlist.html')
