import requests
import urllib.parse
from .categories import CATEGORIES
from .models import Product, Save
from django.contrib.auth.models import User

from pprint import pprint


SEARCH_URL = 'https://fr.openfoodfacts.org/cgi/search.pl'


class OpenFoodFacts:
    def __init__(self):
        self.categories = list()
        self.product_id = list()

    def product_informations(self, categories):
        """
        Get all products informations
        """
        products = list()

        for categorie in categories:
            params = {
                "json": 1,
                "action": "process",
                "page_size": 1000,
                "tagtype_0": "categories",
                "tag_contains_0": "contains",
                "tag_0": categorie
            }

            request = requests.get(url=SEARCH_URL, params=params).json()

            for product in request.get('products'):
                if product.get("nutrition_grades_tags")[0] != 'unknown':
                    products.append(
                        {
                            "name": product.get("product_name"),
                            "category": product.get("categories_hierarchy")[0][3:],
                            "nutriscore": product.get("nutrition_grades_tags")[0],
                            "url_op": product.get("url"),
                            "url_image_recto": product.get("image_front_url"),
                            "url_image_verso": product.get("image_nutrition_url"),
                        }
                    )

        return products

    def init_db(self):
        """
        Runs all methods to init db
        """
        for product in self.product_informations(CATEGORIES):
            p = Product.objects.create(**product)
            p.save()

    def create_user(self):
        """
        Create user for simple test
        """
        prenom = input('prenom: \n')
        mail = input('mail: \n')
        password = input('passwd: \n')
        user = User.objects.create_user(
            prenom,
            mail,
            password
        )
