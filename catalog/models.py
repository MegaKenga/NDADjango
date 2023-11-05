from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=4000, verbose_name='Бренд')
    description = models.TextField(max_length=240, blank=True, null=True, verbose_name='Описание')
    place = models.IntegerField(blank=True, null=True, verbose_name='Место в списке')
    brand_image = models.ImageField(upload_to='catalog/images/image', blank=True, null=True, verbose_name='Изображение')
    brand_banner = models.ImageField(upload_to='catalog/images/banner', blank=True, null=True, verbose_name='Баннер')
    hide = models.BooleanField(default=False, verbose_name='Скрыть')

    class Meta:
        ordering = ['place']
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=4000, verbose_name='Имя группы')
    description = models.TextField(max_length=4000, blank=True, null=True, verbose_name='Описание')
    group_brand = models.ForeignKey('Brand', null=True, on_delete=models.SET_NULL, verbose_name='ID Бренда, к которому относится группа')
    group_image = models.ImageField(upload_to='catalog/images/image', blank=True, null=True, verbose_name='Изображение')
    group_banner = models.ImageField(upload_to='catalog/images/banner', blank=True, null=True, verbose_name='Баннер')
    place = models.IntegerField(blank=True, null=True, verbose_name='Место в списке')
    hide = models.BooleanField(default=False, verbose_name='Скрыть')

    class Meta:
        ordering = ['place']
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name


class Product(models.Model):
    ref = models.CharField(max_length=4000, verbose_name='Код товара')
    name = models.TextField(max_length=4000, verbose_name='Название товара')
    product_image = models.ImageField(upload_to='catalog/images/image', blank=True, null=True, verbose_name='Изображение')
    place = models.IntegerField(blank=True, null=True, verbose_name='Место в списке')
    group = models.ForeignKey('Group', null=True, related_name='ancestor_for_product', on_delete=models.SET_NULL,
                              verbose_name='Уникальный ID группы, к которой принадлежит товар')
    hide = models.BooleanField(default=False, verbose_name='Скрыть')

    class Meta:
        ordering = ['place']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.ref


class Unit(models.Model):
    name = models.CharField(max_length=4000, verbose_name='Бренд')
    description = models.TextField(max_length=4000, blank=True, null=True, verbose_name='Описание')
    unit_image = models.ImageField(upload_to='catalog/images/image', blank=True, null=True, verbose_name='Изображение')
    place = models.IntegerField(blank=True, null=True, verbose_name='Место в списке')
    hide = models.BooleanField(default=False, verbose_name='Скрыть')

    class Meta:
        ordering = ['place']
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'

    def __str__(self):
        return self.name


class CategoryToGroup(models.Model):
    group = models.OneToOneField('Group', related_name='descendant', null=True, on_delete=models.SET_NULL,
                                 verbose_name='ID группы')
    parent_group = models.ForeignKey('Group', related_name='ancestor', null=True, on_delete=models.SET_NULL,
                                     verbose_name='ID группы-родителя. Если указать 0, то группа будет отображаться\
                                         как начальная в категории Бренда')
    final = models.BooleanField(default=False, verbose_name='Отметка о том, что это группа последняя в категории \
                                                            и при переходе в группу будут отображаться уже товары')
    group_brand = models.ForeignKey('Brand', null=True, on_delete=models.SET_NULL, verbose_name='ID Бренда, \
                                                                                    к которому относится группа')

    class Meta:
        ordering = ['id']
        verbose_name = 'Связь группы и её родителя'
        verbose_name_plural = 'Связь групп и их родителей'

    def __str__(self):
        return str(self.id)


class UnitToCategory(models.Model):
    group = models.OneToOneField('Group', null=True, on_delete=models.SET_NULL, verbose_name='Уникальный ID группы,\
                                                                                         принадлежащей направлению')
    unit = models.ForeignKey('Unit', null=True, on_delete=models.SET_NULL, verbose_name='Уникальный ID направления')
    group_brand = models.ForeignKey('Brand', null=True, on_delete=models.SET_NULL, verbose_name='ID Бренда, \
                                                                                        к которому относится группа')

    class Meta:
        ordering = ['id']
        verbose_name = 'Связь группы и направления'
        verbose_name_plural = 'Связь групп и направлений'

    def __str__(self):
        return str(self.id), self.group, self.unit, self.group_brand
