from django.db import models

NULLABLE = {'blank': True, 'null': True}
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование продукта')
    description = models.CharField(max_length=300, verbose_name='описание')
    preview = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    price = models.IntegerField(verbose_name='цена за штуку')
    date_of_creation = models.DateField(verbose_name='дата создания')
    date_modification = models.DateField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.description} {self.category} ' \
               f'{self.price} {self.date_of_creation} {self.date_modification}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)

class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='наименование категории')
    description = models.CharField(max_length=300, verbose_name='описание')

    def __str__(self):
        return f'{self.category_name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
