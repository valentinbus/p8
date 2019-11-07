from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.core import serializers
from .models import Product
from django.shortcuts import render

from pprint import pprint


def list_all_products(request):
    products_list = Product.objects.all()
    seriale_objects = serializers.serialize('json', products_list)
    pprint(seriale_objects)
    paginator = Paginator(products_list, 25)

    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request, 'op/list_products.html', {'products': products})
