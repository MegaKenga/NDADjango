from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=240, primary_key=True)
    description = models.CharField(max_length=240)
    place = models.IntegerField(unique=True)

    class Meta:
        ordering = ['place']
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return '{0} {1}', format(self.name, self.description)


class Unit(models.Model):
    name = models.CharField(max_length=240, primary_key=True)
    description = models.CharField(max_length=240)

    class Meta:
        ordering = ['name']
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'

    def __str__(self):
        return '{0} {1}', format(self.name, self.description)


class Category(models.Model):
    name = models.CharField(max_length=240, primary_key=True)
    description = models.CharField(max_length=240, null=True)
    unit_name = models.ForeignKey(Unit, on_delete=models.CASCADE)
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return '{0} {1}', format(self.name, self.brand_name.name)


class Typeclass(models.Model):
    name = models.CharField(max_length=240, primary_key=True)
    description = models.CharField(max_length=240, null=True)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return '{0} {1}', format(self.name, self.description)


class Group(models.Model):
    name = models.CharField(max_length=240, primary_key=True)
    description = models.CharField(max_length=240, null=True)
    type_name = models.ForeignKey(Typeclass, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return '{0} {1}', format(self.name, self.description)


class Product(models.Model):
    ref = models.CharField(max_length=240)
    description = models.CharField(max_length=240)
    group_name = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        ordering = ['ref']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return '{0} {1}', format(self.ref, self.description)
