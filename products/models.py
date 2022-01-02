from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User

# Create your models here.


# Category model
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Product model
class Product(models.Model):
    AREA = (
        ('individual', 'Individual'),
        ('team', 'Team'),
        ('universal', 'Universal'),
        )

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    area = models.CharField(max_length=200, null=True, choices=AREA)
    on_sale = models.BooleanField(default=False)
    discount_on_product = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    # Sales price calculation where product is on sale
    def sales_price(self):
        '''Calculate the new price after applying the product discount
        Source of help: https://helperbyte.com/questions/77886/
        django-how-to-make-a-discount-for-the-item
        '''
        on_sale_price = Decimal(self.price * (
            100 - self.discount_on_product) / 100).quantize(Decimal('0.00'))
        return on_sale_price


class ReviewProduct(models.Model):
    STARS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='reviews', on_delete=models.CASCADE)
    review_text_field = models.TextField(blank=True, null=True, max_length=300)
    review_star_rating = models.IntegerField(choices=STARS)
    date_review = models.DateTimeField(auto_now_add=True)
