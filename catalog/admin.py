from django.contrib import admin

from catalog.models import Brand, Unit, Category, Typeclass, Group, Product

admin.site.register(Brand)
admin.site.register(Unit)
admin.site.register(Category)
admin.site.register(Typeclass)
admin.site.register(Group)
admin.site.register(Product)
