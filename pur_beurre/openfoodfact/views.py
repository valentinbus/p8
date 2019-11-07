from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.core import serializers
from .models import Product
from django.shortcuts import render

from pprint import pprint


def list_all_products(request):
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 25)

    page = request.GET.get('page')
    products = paginator.get_page(page)
    
    """
    If i want a Json return i have to do this :
    seriale_objects = serializers.serialize('json', products_list)
    return HttpResponse(seriale_objects)
    """

    return render(request, 'op/list_products.html', {'products': products})


def purpose_replace(request):
    """
    Give replacement for product with better nutriscore
    ID Product is given in GET request parameter
    """

    ID = request.GET['id']
    product = Product.objects.get(pk=ID)
    nutriscore = product.nutriscore
    print(nutriscore)

    replace_products = Product.objects.filter(
        category__lte=nutriscore
    )

    paginator = Paginator(replace_products, 25)

    page = request.GET.get('page')
    replace_products = paginator.get_page(page)

    return render(request, 'op/replace_products.html', {'replace_products': replace_products})
