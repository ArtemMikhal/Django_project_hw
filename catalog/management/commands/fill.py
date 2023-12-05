import json
from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        with open('data.json', "r", encoding="UTF-8") as file:
            data = json.load(file)
            products = []
            category = []
            for item in data:
                if item["model"] == "catalog.product":
                    products.append(Product(**item['fields']))
                else:
                    category.append(Category(**item['fields']))

        Product.objects.bulk_create(products)
        Category.objects.bulk_create(category)