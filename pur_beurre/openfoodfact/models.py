from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    nutriscore = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=200, null=True)
    url_op = models.CharField(max_length=1024, null=True)
    url_image_recto = models.CharField(max_length=500, null=True)
    url_image_verso = models.CharField(max_length=500, null=True)

class Save(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_save")
    product_to_replace = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_to_replace")
    replace_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="replace_product") 

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saves = models.ForeignKey(Save, on_delete=models.CASCADE)
