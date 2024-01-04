from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

        #fields = ('name', 'description' ) определенные атрибуты
        #exclude = ('preview') для исключения какого-либо атрибута


