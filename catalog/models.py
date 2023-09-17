from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Уникальный ID бренда')
    name = models.CharField(max_length=4000, verbose_name='Бренд')
    description = models.CharField(max_length=240, blank=True, null=True, verbose_name='Описание')
    place = models.IntegerField(blank=True, null=True, verbose_name='Место в списке')
    brand_image = models.ImageField(upload_to='images/brand', blank=True, null=True, verbose_name='Изображение')
    brand_banner = models.ImageField(upload_to='images/brand', blank=True, null=True, verbose_name='Баннер')

    class Meta:
        ordering = ['place']
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name, self.description, self.place


class Group(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Уникальный ID каждой группы')
    name = models.CharField(max_length=4000, verbose_name='Имя группы')
    description = models.CharField(max_length=4000, blank=True, null=True, verbose_name='Описание')
    group_brand = models.ForeignKey('Brand', null=True, on_delete=models.SET_NULL, verbose_name='ID Бренда, \
                                                                                    к которому относится группа')
    place = models.IntegerField(blank=True, null=True, verbose_name='Место в списке')

    class Meta:
        ordering = ['place']
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name, self.group_brand, Brand.name, self.place


class Product(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Уникальный ID каждого товара')
    ref = models.CharField(max_length=4000, verbose_name='Код товара')
    name = models.CharField(max_length=4000, verbose_name='Имя товара')
    place = models.IntegerField(blank=True, null=True, verbose_name='Место в списке')

    class Meta:
        ordering = ['place']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.ref, self.name, self.place


class ProductToGroup(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Уникальный ID каждой связи товара и группы')
    product = models.OneToOneField('Product', null=True, on_delete=models.SET_NULL, verbose_name='Уникальный ID товара')
    group = models.ForeignKey('Group', null=True, on_delete=models.SET_NULL, verbose_name='Уникальный ID группы, \
                                                                                    к которой принадлежит товар')

    class Meta:
        ordering = ['id']
        verbose_name = 'Связь продукта и его группы'
        verbose_name_plural = 'Связь продуктов и их групп'

    def __str__(self):
        return self.id, self.product, self.group


class CategoryToGroup(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Уникальный ID каждой связи групп между собой')
    group = models.OneToOneField('Group', related_name='descendant', null=True, on_delete=models.SET_NULL,
                              verbose_name='ID группы')
    parent_group = models.ForeignKey('Group', related_name='ancestor', null=True, on_delete=models.SET_NULL,
                                     verbose_name='ID группы-родителя. Если указать 0, то группа будет отображаться\
                                         как начальная в категории Бренда')
    final = models.BooleanField(default=False, verbose_name='Отметка о том, что это группа последняя в категории \
                                                            и при переходе в группу будут отображаться уже товары')

    class Meta:
        ordering = ['id']
        verbose_name = 'Связь группы и её родителя'
        verbose_name_plural = 'Связь групп и их родителей'

    def __str__(self):
        return self.id, self.group, self.parent_group, self.final


class Unit(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Уникальный ID бренда')
    name = models.CharField(max_length=4000, verbose_name='Бренд')
    description = models.CharField(max_length=4000, blank=True, null=True, verbose_name='Описание')
    unit_image = models.ImageField(upload_to='images/unit', blank=True, null=True, verbose_name='Изображение')
    place = models.IntegerField(blank=True, null=True, verbose_name='Место в списке')

    class Meta:
        ordering = ['place']
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'

    def __str__(self):
        return self.id, self.name, self.description, self.place


class UnitToCategory(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Уникальный ID каждой связи направления и группы')
    group = models.OneToOneField('Group', null=True, on_delete=models.SET_NULL, verbose_name='Уникальный ID группы,\
                                                                                         принадлежащей направлению')
    unit = models.ForeignKey('Unit', null=True, on_delete=models.SET_NULL, verbose_name='Уникальный ID направления')

    class Meta:
        ordering = ['id']
        verbose_name = 'Связь группы и направления'
        verbose_name_plural = 'Связь групп и направлений'

    def __str__(self):
        return self.id, self.group, self.unit
