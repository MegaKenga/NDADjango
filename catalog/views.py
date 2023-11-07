from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from catalog.models import Brand, Unit, Group, Product, CategoryToGroup, UnitToCategory


def index(request):
    brands = Brand.objects.all().order_by('place')
    units = Unit.objects.all().order_by('place')
    context = {'brands': brands, 'units': units}
    return render(request, 'catalog/index.html', context=context)


def single_brand(request, brand_name):
    try:
        Brand.objects.get(name=brand_name)
    except Brand.DoesNotExist:
        raise Http404()
    return HttpResponse(f'<h1> {brand_name} </h1>')


def single_unit(request, unit_name):
    try:
        Unit.objects.get(name=unit_name)
    except Brand.DoesNotExist:
        raise Http404()
    return HttpResponse(f'<h1> {unit_name} </h1>')


def brand_groups(request, brand_name):
    pass


def page_not_found(request, exception):
    page404 = render(request, 'page404.html')
    return HttpResponseNotFound(page404)
