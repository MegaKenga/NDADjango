from django.db import models
from catalog.models import Group, Product


class FilesToGroup(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Уникальный ID связи группы и её файлов')
    group = models.OneToOneField('Group', on_delete=models.SET_NULL, verbose_name='Уникальный ID каждой группы')
    group_image = models.ImageField(upload_to='images/group', blank=True, null=True, verbose_name='Изображение')
    group_banner = models.ImageField(upload_to='images/group', blank=True, null=True, verbose_name='Баннер')
    group_registration = models.FileField(upload_to='files/registration', blank=True, null=True, verbose_name='РУ')
    group_instruction = models.FileField(upload_to='files/registration', blank=True, null=True,
                                         verbose_name='Инструкция')

    class Meta:
        ordering = ['id']
        verbose_name = 'Связь группы и её файлов'
        verbose_name_plural = 'Связи групп и их файлов'

    def __str__(self):
        return self.group, self.group_image, self.group_banner, self.group_registration, self.group_instruction


class FilesToProduct(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Уникальный ID связи товара и его файлов')
    product = models.OneToOneField('Group', on_delete=models.SET_NULL, verbose_name='Уникальный ID каждого товара')
    product_image = models.ImageField(upload_to='images/product', blank=True, null=True, verbose_name='Изображение')
    product_tech_description = models.FileField(upload_to='files/tech_description', blank=True, null=True,
                                                verbose_name='Описание товара')

    class Meta:
        ordering = ['id']
        verbose_name = 'Связь товара и его файлов'
        verbose_name_plural = 'Связи товаров и их файлов'

    def __str__(self):
        return self.product, self.product_image, self.product_tech_description
