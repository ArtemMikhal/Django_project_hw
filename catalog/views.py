from django.shortcuts import render, get_object_or_404
from catalog.models import Product

def home_page(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/home.html', context)


def contacts_page(request):
    return render(request, 'catalog/contacts.html')

def product(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'catalog/product.html', {'product': product})

