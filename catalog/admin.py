from django.contrib import admin

from catalog.models import Product, Category

admin.site.register(Product)
admin.site.register(Category)