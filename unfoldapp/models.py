from django.db import models
from django.utils.translation import gettext_lazy as _


class PublishedStatus(models.TextChoices):
    YES = "True", _("Да")
    NO = "False", _("Нет")

# Create your models here.

class News(models.Model):
    image = models.ImageField(upload_to='News/',verbose_name='Изображение')
    title = models.CharField(max_length=256,verbose_name='Заголовка')
    description = models.TextField(verbose_name='Описание')
    content = models.TextField(verbose_name='Контент')
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True,verbose_name='Категория')
    is_published = models.CharField(max_length=5,choices=PublishedStatus.choices,default=PublishedStatus.NO,verbose_name='Опубликовано')    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата изменения")

    class Meta:
        db_table = 'News'
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
    

class Category(models.Model):
    image = models.ImageField(upload_to='Category/',verbose_name='Изображение')
    name = models.TextField(verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата изменения")

    class Meta:
        db_table = 'Category'
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name
    

