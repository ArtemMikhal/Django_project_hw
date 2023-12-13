# Generated by Django 4.2.7 on 2023-12-11 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_modification',
            field=models.DateField(auto_now=True, verbose_name='дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_of_creation',
            field=models.DateField(auto_now_add=True, verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(verbose_name='цена за штуку'),
        ),
    ]