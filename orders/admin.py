from django.contrib import admin

from orders.models import Order, OrderRow

admin.site.register(Order)
admin.site.register(OrderRow)
