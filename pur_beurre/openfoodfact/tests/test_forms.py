from django.test import TestCase
from openfoodfact.forms import SearchForm
from openfoodfact.models import Product


class FormsTest(TestCase):

    def test_valid_form(self):
		data = {'q': 'pizza'}
		form = SearchForm(data=data)
		self.assertTrue(form.is_valid())