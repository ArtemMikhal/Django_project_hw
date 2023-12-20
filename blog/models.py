from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Blog(models.Model):
   title = models.CharField(max_length=150, verbose_name= 'заголовок')
   slug = models.CharField(max_length=100, verbose_name= 'slug', **NULLABLE)
   preview = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
   date_of_creation = models.DateField(auto_now_add=True, verbose_name='дата создания')
   is_published = models.BooleanField(default=True, verbose_name='опубликовано')
   views_count = models.IntegerField(default=0, verbose_name='просмотры' )

   def __str__(self):
       return self.title

   class Meta:
       verbose_name  = 'материал'
       verbose_name_plural = 'материалы'


