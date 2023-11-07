from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='main'),
    path('brands/<str:brand_name>', views.single_brand, name='brand_name'),
    # при редиректе с помощью name надо обязательно указать через запятую параметр brand_name. e.g. medtronic
    path('units/<str:unit_name>', views.single_unit, name='unit_name')
]

if settings.DEBUG:
    static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
