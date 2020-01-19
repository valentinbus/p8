import unittest
import logging

from pprint import pformat
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.paginator import Paginator
from openfoodfact.models import Product, Save
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector


logging.basicConfig(level=logging.DEBUG)
client = Client()
class ViewsTest(TestCase):
    @classmethod
    def setUp(self):
        # Set up data for the whole TestCase

        product = {
            "name": "name",
            "category": "category",
            "nutriscore": "nutriscore",
            "url_op": "url op",
            "url_image_recto": "url image recto",
            "url_image_verso": "url image verso",
        }

        for i in range(1, 10):
            products = Product.objects.create(**product)
            logging.info(f"ID:::{products.id}")


        user = User.objects.create_user(
            username='valentin', 
            email='valentin@gmail.com',
            password='psswd'
        )

        Save.objects.create(
            user=user,
            product_to_replace=Product.objects.get(pk=2),
            replace_product=Product.objects.get(pk=3)
        )

    def test_list_products(self):
        response = client.get(reverse('list'))
        self.assertEquals(response.status_code, 200)

    def test_list_products_json(self):
        response = client.get(reverse('list'), {'json': 1})
        self.assertEquals(response.status_code, 200)

    def test_purpose_replace(self):
        response = client.get(reverse('replace'), {'id': 31})
        self.assertEquals(response.status_code, 200)

    def test_search_product(self):
        response = client.get(reverse('search_product'), {'q': "name"})
        self.assertEquals(response.status_code, 200)
    
    def test_search_product2(self):
        response = client.get(reverse('search_product'))
        self.assertEquals(response.status_code, 200)


    # #TODO test redirection
    # def test_save_replacement(self):
    #     response = client.get(reverse('save_replacement'), {'id_product_to_replace': 30}, {'id_replace_product': 33})
    #     self.assertEquals(response.status_code, 302)

    # def test_show_saves(self):
    #     response = client.get(reverse("saves"))
    #     self.assertEquals(response.status_code, 200)
    # def test_purpose_replace(self):

    def test_more_informations(self):
        response = client.get(reverser('more_informations'), {'id': 22})
        self.assertEquals(response.status_code, 200)
