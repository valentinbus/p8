from django.db import models

from django.db import models
from django.utils import timezone


class Products(models.Model):
    product_name = models.CharField(max_length=50)
    nutriscore = models.CharField(max_length=1)
    category = models.CharField(max_length=50)
    url_op = models.CharField(max_length=200)
    url_image_recto = models.CharField(max_length=200)
    url_image_verso = models.CharField(max_length=200)

class Saves(models.Model):
    product_to_replace = models.ForeignKey(Products, on_delete=models.CASCADE)
    replace_product = models.ForeignKey(Products, on_delete=models.CASCADE)
