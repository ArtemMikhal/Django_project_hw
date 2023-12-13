from django.urls import path

from catalog.views import home_page, contacts_page, product

urlpatterns = [
    path('', home_page),
    path('contacts/', contacts_page),
    path('product/<int:id>/', product, name='product_detail'),
]