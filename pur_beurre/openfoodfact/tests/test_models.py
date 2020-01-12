from django.test import TestCase
from openfoodfact.models import Product
from django.utils import timezone
#from django.core.urlresolvers import reverse

# models test
class ProductTest(TestCase):

    def create_product(
        self, 
        name="only a test", 
        nutriscore="e", 
        category="soda",
        url_op="http://url_op",
        url_image_recto="http://url_image_recto",
        url_image_verso="http://url_image_verso"
    ):
        """
        Creation product test
        """
        return Product.objects.create(
            name=name, 
            nutriscore=nutriscore,
            category=category,
            url_op=url_op,
            url_image_recto=url_image_recto,
            url_image_verso=url_image_verso
        )

    def test_product_creation(self):
        product = self.create_product()
        self.assertTrue(isinstance(product, Product))
