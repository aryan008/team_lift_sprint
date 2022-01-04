from django.contrib import admin
from .models import Category, Product, ReviewProduct

# Register your models here.


# Admin category name class
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


# Admin product display fields
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'area',
        'on_sale',
        'discount_on_product',
        'image',
    )

    # Ordering by sku
    ordering = ('sku',)


class ReviewProductAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'product', 'review_text_field',
        'review_star_rating', 'date_review')


admin.site.register(ReviewProduct, ReviewProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
