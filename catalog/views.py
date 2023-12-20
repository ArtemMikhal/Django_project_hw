from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'

def contacts_page(request):
    return render(request, 'catalog/contacts.html')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'



