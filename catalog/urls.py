from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import contacts_page, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, categories

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts_page, name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('categories/', categories, name='categories'),
]