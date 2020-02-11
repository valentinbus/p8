import unittest
import logging

from pprint import pformat
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.core import mail
from django.core.paginator import Paginator
from openfoodfact.models import Product, Save
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector


logging.basicConfig(level=logging.DEBUG)
client = Client()
class ViewsTest(TestCase):

    def test_list_products(self):
        product1 = {
            "name": "name",
            "category": "category",
            "nutriscore": "a",
            "url_op": "url op",
            "url_image_recto": "url image recto",
            "url_image_verso": "url image verso",
        }
        product2 = {
            "name": "name",
            "category": "category",
            "nutriscore": "b",
            "url_op": "url op",
            "url_image_recto": "url image recto",
            "url_image_verso": "url image verso",
        }

        Product.objects.create(**product1)
        Product.objects.create(**product2)
        for product in Product.objects.all():
            logging.info(f"ID:::{product.id}")

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
        response = client.get(reverse('list'))
        self.assertEquals(response.status_code, 200)

    def test_list_products_json(self):
        response = client.get(reverse('list'), {'json': 1})
        self.assertEquals(response.status_code, 200)

    def test_purpose_replace(self):
        product1 = {
            "name": "name",
            "category": "category",
            "nutriscore": "a",
            "url_op": "url op",
            "url_image_recto": "url image recto",
            "url_image_verso": "url image verso",
        }
        product2 = {
            "name": "name",
            "category": "category",
            "nutriscore": "b",
            "url_op": "url op",
            "url_image_recto": "url image recto",
            "url_image_verso": "url image verso",
        }

        product1 = Product.objects.create(**product1)
        product2 = Product.objects.create(**product2)
        response = client.get(reverse('replace'), {'id': f"{product1.id}"})

        for product in Product.objects.all():
            logging.info(f"\nPURPOSE REPLACE:::{product.id}")
        
        self.assertEquals(response.status_code, 200)

    def test_search_product(self):
        response = client.get(reverse('search_product'), {'q': "name"})
        self.assertEquals(response.status_code, 200)
    
    def test_search_product2(self):
        response = client.get(reverse('search_product'))
        self.assertEquals(response.status_code, 200)

    def test_search_product3(self):
        response = client.get(
            reverse('search_product'), 
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEquals(response.status_code, 200)

    def test_save_replacement(self):
        product1 = {
            "name": "name",
            "category": "category",
            "nutriscore": "a",
            "url_op": "url op",
            "url_image_recto": "url image recto",
            "url_image_verso": "url image verso",
        }
        product2 = {
            "name": "name",
            "category": "category",
            "nutriscore": "b",
            "url_op": "url op",
            "url_image_recto": "url image recto",
            "url_image_verso": "url image verso",
        }

        product1 = Product.objects.create(**product1)
        product2 = Product.objects.create(**product2)
        for product in Product.objects.all():
            logging.info(f"\nPURPOSE REPLACE:::{product.id}")

        user = User.objects.create_user(
            username='valentin', 
            email='valentin@gmail.com',
            password='psswd'
        )
        logged_in = self.client.login(username='valentin', password='psswd')
        response = self.client.get(
            reverse('save_replacement'), 
            {
                'id_product_to_replace': f"{product1.id}",
                'id_replace_product': f"{product2.id}"
            }, 
        )

        self.assertEquals(response.status_code, 302)

    def test_show_saves(self):
        product1 = {
            "name": "name",
            "category": "category",
            "nutriscore": "a",
            "url_op": "url op",
            "url_image_recto": "url image recto",
            "url_image_verso": "url image verso",
        }
        product2 = {
            "name": "name",
            "category": "category",
            "nutriscore": "b",
            "url_op": "url op",
            "url_image_recto": "url image recto",
            "url_image_verso": "url image verso",
        }

        product1 = Product.objects.create(**product1)
        product2 = Product.objects.create(**product2)

        user = User.objects.create_user(
            username='valentin', 
            email='valentin@gmail.com',
            password='psswd'
        )

        Save.objects.create(
            user=user,
            product_to_replace=Product.objects.get(pk=f"{product1.id}"),
            replace_product=Product.objects.get(pk=f"{product2.id}")
        )
        client.login(username='valentin', password='psswd')
        response = client.get(reverse("saves"))
        self.assertEquals(response.status_code, 200)

    def test_more_informations(self):
        product1 = {
            "name": "name",
            "category": "category",
            "nutriscore": "a",
            "url_op": "url op",
            "url_image_recto": "url image recto",
            "url_image_verso": "url image verso",
        }
        user = User.objects.create_user(
            username='valentin', 
            email='valentin@gmail.com',
            password='psswd'
        )
        client.login(username='valentin', password='psswd')
        product1 = Product.objects.create(**product1)
        response = client.get(reverse('more_informations'), {'id': f"{product1.id}"})
        self.assertEquals(response.status_code, 200)

    def test_send_mail(self):
        # Use Django send_mail function to construct a message
        # Note that you don't have to use this function at all.
        # Any other way of sending an email in Django would work just fine. 
        mail.send_mail(
                'Subject here',
                'Here is the message.',
                'from@example.com',
                ['to@example.com']
            )

        # Now you can test delivery and email contents
        assert len(mail.outbox) == 1, "Inbox is not empty"
        assert mail.outbox[0].subject == 'Subject here'
        assert mail.outbox[0].body == 'Here is the message.'
        assert mail.outbox[0].from_email == 'from@example.com'
        assert mail.outbox[0].to == ['to@example.com']