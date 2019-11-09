from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.core import serializers
from .models import Product
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .openfoodfact import OpenFoodFacts

from pprint import pprint


op = OpenFoodFacts()

def list_all_products(request):
    """
    List all products from bdd
    """
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 25)

    page = request.GET.get('page')
    products = paginator.get_page(page)
    
    #Return json result if json == 1 in request GET paramter
    if request.GET.get('json'):
        seriale_objects = serializers.serialize('json', products_list)
        return HttpResponse(seriale_objects)

    return render(request, 'op/list_products.html', {'products': products})

def purpose_replace(request):
    """
    Give replacement for product with better nutriscore
    ID Product is given in GET request parameter
    """

    ID = request.GET['id']
    product_to_replace = Product.objects.get(pk=ID)
    nutriscore = product_to_replace.nutriscore

    replace_products_list = Product.objects.filter(
        category__lte=nutriscore
    )

    paginator = Paginator(replace_products_list, 25)

    page = request.GET.get('page')
    replace_products = paginator.get_page(page)

    #Return json result if json == 1 in request GET paramter
    if request.GET.get('json'):
        seriale_objects = serializers.serialize('json', replace_products_list)
        return HttpResponse(seriale_objects)

    return render(
        request, 
        'op/replace_products.html', 
        {
            'replace_products': replace_products, 
            'product_to_replace': product_to_replace
        }
    )

@login_required(login_url="/connexion")
def save_replacement(request):
    """
    Feature to save a replacement if user want
    """
    
    #Have to get param for 
    ID_PRODUCT_TO_REPLACE = request.GET['id_product_to_replace']
    ID_REPLACE_PRODUCT = request.GET['id_replace_product']

    return None

def search_product(request):
    """
    Use for user's search and return a list of products

    ToDo
    Comment utiliser une fonctionnolité d'openfoodfact si je ne peux pas l'importer
    """

    return HttpResponse(op.test())