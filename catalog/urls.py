from django.urls import path

from catalog.views import contacts_page, ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts_page, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]