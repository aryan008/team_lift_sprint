from django.contrib import admin
from .models import Wishlist, AddToWishlist

# Register your models here.
admin.site.register(Wishlist)
admin.site.register(AddToWishlist)
