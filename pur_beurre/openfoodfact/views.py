from django.http import (
    HttpResponseRedirect,
    HttpResponse,
    JsonResponse
)
from django.core.paginator import Paginator
from django.core import serializers
from .models import Product, Save, User
from django.shortcuts import render, redirect
from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector
)
from django.contrib.auth.decorators import login_required
from .openfoodfact import OpenFoodFacts
from .forms import SearchForm

from pprint import pformat
import logging
import json


logging.basicConfig(level=logging.DEBUG)
op = OpenFoodFacts()


def list_all_products(request):
    """
    List all products from bdd
    """
    logging.info(f"REQUEST:::{pformat(request)}")
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 25)

    page = request.GET.get('page')
    products = paginator.get_page(page)

    #Return json result if json == 1 in request GET paramter
    if request.GET.get('json'):
        seriale_objects = serializers.serialize('json', products_list)
        return HttpResponse(seriale_objects)

    return render(
        request, 'op/list_products.html',
        {
            'products': products
        }
    )


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

    return render(
        request,
        'op/replace_products.html',
        {
            'id_product': ID,
            'replace_products': replace_products,
            'product_to_replace': product_to_replace
        }
    )


def search_product(request):
    """
    Use for user's search and return a list of products

    ToDo
    Comment utiliser une fonctionnolité
    d'openfoodfact si je ne peux pas l'importer
    """
    q = request.GET.get('q')

    if q:
        product_list = list()
        all_products = Product.objects.all()

        products_list = Product.objects.annotate(
                search=SearchVector('name')
        ).filter(search=q)

        paginator = Paginator(products_list, 25)
        page = request.GET.get('page')

        products = paginator.get_page(page)

        result = list()
        for product in products:
            d = dict()
            img_path = f"img/nutriscore/{product.nutriscore}.png"
            d['img_path'] = img_path
            d['product'] = product
            result.append(d)

        return render(
            request, 'op/list_products.html',
            {
                'q': q,
                'result': result,
                'products': products
            }
        )

    elif request.is_ajax():
        print('coucou')
        q = request.GET.get('term', '').capitalize()
        products = Product.objects.filter(name__startswith=q)
        results = []
        print(q)
        for name in products:
            name_json = name.name
            results.append(name_json)
        data = json.dumps(results)
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)

    else:
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

    return redirect('/openfoodfact/saves')


@login_required(login_url="/connexion")
def show_saves(request):
    """
    Show save replacement from user
    """

    username = request.user.username
    user = User.objects.get(
        username=username
    )

    saves = Save.objects.filter(
        user_id=user.id
    )

    results = list()

    #Only works if many saves
    if saves:
        for save in saves:
            product_to_replace = Product.objects.get(id=save.product_to_replace_id)
            replace_product = Product.objects.get(id=save.replace_product_id)
            d = dict()
            d["id_save"] = save.id
            d["product_to_replace"] = product_to_replace
            d["replace_product"] = replace_product

            results.append(d)
    else:
        return render(
            request,
            'op/show_saves.html',
            {
                'response': "Vous n'avez pas encore d'enregistrement"
            }
        )

    return render(request, 'op/show_saves.html', locals())


@login_required(login_url="/connexion")
def more_informations(request):
    """
    Get more informations for saves replacement
    """
    id_product = request.GET['id']
    logging.info(id_product)

    product = Product.objects.get(
        id=id_product
    )

    if product.url_op is None:
        product.url_op = "https://fr.openfoodfacts.org/"

    return render(request, "op/more_informations.html", {'product': product})
