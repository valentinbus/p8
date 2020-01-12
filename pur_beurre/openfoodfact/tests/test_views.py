import unittest
import logging

from pprint import pformat
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from openfoodfact.models import Product


logging.basicConfig(level=logging.DEBUG)
client = Client()
class ViewsTest(TestCase):

    def test_list_products(self):
        response = client.get('/openfoodfact/list/')

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'op/list_products.html')

    def test_list_product_json(self):
        response = client.get('/openfoodfact/list/?json=1')
        products_list = Product.objects.all()

        logging.info(f"RESPONSE:::{pformat(response.content)}")
        self.assertEquals(response.status_code, 200)
        #Il faudra faire les tests pour le contenu de la réponse Json

    def test_search_product(self):
        response = client.get('/openfoodfact/search_product/')

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'op/search_product.html')

    def test_search_product2(self):
        response = client.get('/openfoodfact/search_product/?q=pizza')

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'op/search_product.html')
