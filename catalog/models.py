from django.db import models
from django.contrib.auth import get_user_model


NULLABLE = {'blank': True, 'null': True}
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование продукта')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    price = models.PositiveIntegerField(verbose_name='цена за штуку')
    date_of_creation = models.DateField(auto_now_add=True, verbose_name='дата создания')
    date_modification = models.DateField(auto_now=True, verbose_name='дата последнего изменения')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=None, null=True, verbose_name='пользователь')
    is_published = models.BooleanField(default=False, verbose_name='статус публикации')

    class Meta:
        permissions = [
            ('set_published', 'Can publish posts'),
            ('change_product_description', 'Can change product description'),
            ('change_product_category', 'Can change product category'),
        ]

        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'

    def get_active_version(self):
        try:
            return self.version_set.get(is_active=True)
        except Version.DoesNotExist:
            return None



class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование категории')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    version_number = models.IntegerField(**NULLABLE, verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Наименование версии')
    is_active = models.BooleanField(default=True, verbose_name='Текущая версия')

    def __str__(self):
        return f"Версия {self.version_number} - {self.version_name} для продукта {self.product}"

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'