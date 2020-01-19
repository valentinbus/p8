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
    def test_connexion(self):
        User.objects.create_user(
            username='valentin',
            email='a@a.com',
            password='valentin'
        )

        response = client.post(
            reverse('connexion'),
            {
                'username': 'valentin',
                'password': 'valentin'
            } 
        )

        self.assertEquals(response.status_code, 200)

    def test_registration(self):
        response = client.post(
            reverse('registration'),
            {
                'username': 'test',
                'email': 'test@test.com',
                'password': 'password',
                'confirm_password': 'password'
            }
        )

        self.assertEquals(response.status_code, 200)

    def test_deconnexion(self):
        user = User.objects.create_user(
            username='valentin',
            email='a@a.com',
            password='valentin'
        )

        client.login(username='valentin', password='valentin')

        response = client.get(
            reverse('deconnexion')
        )

        self.assertEquals(response.status_code, 200)