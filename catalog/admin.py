from django.contrib import admin

from catalog.models import Product, Category, Version

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category', 'user')
    search_fields = ('name', 'description',)
    readonly_fields = ('date_of_creation', 'date_modification')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_name','is_active')
    list_filter = ('product',)


