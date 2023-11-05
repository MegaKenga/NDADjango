from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter #необходимо для отображения только объектов, имеющих foreign key, с конкретными related_names

from catalog.models import Brand, Group, Product, CategoryToGroup, Unit, UnitToCategory


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'place')
    actions_on_bottom = True
    list_per_page = 25
    search_fields = ['name']


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'group_brand', 'place')
    list_filter = ('group_brand', )
    actions_on_bottom = True
    list_per_page = 25
    search_fields = ('name', 'group_brand')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('ref', 'name', 'group', 'place')
    list_filter = (('group', RelatedOnlyFieldListFilter),) #без RelatedOnlyFieldListFilter будут выводиться абсолютно
                                                    # все группы, даже не являющиеся родительскими именно для продукта
    actions_on_bottom = True
    list_per_page = 25
    search_fields = ('ref', 'name', 'group')


class CategoryToGroupAdmin(admin.ModelAdmin):
    list_display = ('group', 'parent_group', 'final', 'group_brand')
    list_filter = ('group_brand', ('parent_group', RelatedOnlyFieldListFilter)) #без RelatedOnlyFieldListFilter
                                                            # будут выводиться абсолютно все группы, даже не имеющие потомков
    actions_on_bottom = True
    list_per_page = 25
    search_fields = ('group', 'parent_group', 'final')


class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'place')
    actions_on_bottom = True
    list_per_page = 25
    search_fields = ('name', 'description')


class UnitToCategoryAdmin(admin.ModelAdmin):
    list_display = ('group', 'unit', 'group_brand')
    list_filter = ('unit', 'group_brand')
    actions_on_bottom = True
    list_per_page = 25
    search_fields = ('group', 'unit')


admin.site.register(Brand, BrandAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CategoryToGroup, CategoryToGroupAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(UnitToCategory, UnitToCategoryAdmin)
