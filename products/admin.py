from django.contrib import admin
from .models import Category, Product

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


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
