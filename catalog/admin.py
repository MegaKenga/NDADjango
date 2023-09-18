from django.contrib import admin

from catalog.models import Brand, Group, Product, CategoryToGroup, Unit, UnitToCategory

admin.site.register(Brand)
admin.site.register(Group)
admin.site.register(Product)
admin.site.register(CategoryToGroup)
admin.site.register(Unit)
admin.site.register(UnitToCategory)
