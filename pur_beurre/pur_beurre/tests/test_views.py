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
    def test_home(self):
        response = client.get(
            reverse('home')
        )

        self.assertEquals(response.status_code, 200)