from django.shortcuts import render
from django.http import HttpRequest
from catalog.models import Brand, Unit


def index(request):
    brands = Brand.objects.all().order_by('place')
    units = Unit.objects.all().order_by('place')
    context = {'brands': brands, 'units': units}
    return render(request, 'index.html', context=context)



