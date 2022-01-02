from django import forms
from .models import Product, Category, ReviewProduct
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    """ Product form class based on product model
    used for adding/editing products where
    user is identified as a superuser"""

    class Meta:
        """ Meta class for ProductForm"""
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border border-dark'


# Review Form
class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewProduct
        exclude = ('user', 'product', 'date_review')
