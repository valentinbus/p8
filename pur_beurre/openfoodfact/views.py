from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.core import serializers
from .models import Product, Save, User
from django.shortcuts import render
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.contrib.auth.decorators import login_required
from .openfoodfact import OpenFoodFacts
from .forms import SearchForm

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
    category = product_to_replace.category

    replace_products_list = Product.objects.filter(
        nutriscore__lte=nutriscore,
        category=category
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

def search_product(request):
    """
    Use for user's search and return a list of products

    ToDo
    Comment utiliser une fonctionnolité d'openfoodfact si je ne peux pas l'importer
    """
    if request.method == "POST":
        product_list = list()
        all_products = Product.objects.all()

        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data["search"]

            products_list = Product.objects.annotate(
                search = SearchVector('name')
            ).filter(search=search)

            paginator = Paginator(products_list, 25)
            page = request.GET.get('page')
            products = paginator.get_page(page)

            #Return json result if json == 1 in request GET paramter
            if request.GET.get('json'):
                seriale_objects = serializers.serialize('json', products_list)
                return HttpResponse(seriale_objects)

            return render(request, "op/list_products.html", {'products': products})

    else:
        form = SearchForm()
    return render(request, "op/search_product.html", locals())

@login_required(login_url="/connexion")
def save_replacement(request):
    """
    Feature to save a replacement if user want
    """
    
    #Have to get param for 
    ID_PRODUCT_TO_REPLACE = request.GET['id_product_to_replace']
    ID_REPLACE_PRODUCT = request.GET['id_replace_product']

    product_to_replace = Product.objects.get(pk=ID_PRODUCT_TO_REPLACE)
    replace_product = Product.objects.get(pk=ID_REPLACE_PRODUCT)
    username = request.user.username
    user = User.objects.get(
        username=username
    )

    save = Save.objects.create(
        user=user,
        product_to_replace=product_to_replace,
        replace_product=replace_product
    )

    return HttpResponse("Enregistrement réussi", status=200)
