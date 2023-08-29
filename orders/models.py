from django.core.validators import MinValueValidator
from django.db import models
from catalog.models import Product


class Order(models.Model):
    customer_organization = models.CharField(max_length=240, blank=False, verbose_name='Название организации')
    customer_name = models.CharField(max_length=240, blank=False,verbose_name='Ваше имя')
    customer_phone = models.CharField(max_length=240, blank=False,verbose_name='Номер телефона')
    customer_email = models.CharField(max_length=240, blank=False,verbose_name='Email')
    customer_comment = models.TextField(blank=True, verbose_name='Комментарий')
    order_date = models.DateTimeField(auto_now=True, verbose_name='Дата запроса')

    class Meta:
        ordering =['-order_date']
        verbose_name = "Запрос"
        verbose_name_plural = "Запросы"

    def __str__(self):
        return "Запрос #{0}".format(str(self.id))


class OrderRow(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_ref = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(validators=[MinValueValidator(1)], default=1, verbose_name='Количество')

    class Meta:
        verbose_name = 'Строка запроса'
        verbose_name_plural = 'Строки запроса'

    def __str__(self):
        return "Запрос #{0}: {1} - количество {2}".format(str(self.order_id, self.product_ref, self.quantity))
