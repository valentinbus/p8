# Generated by Django 2.2.6 on 2019-10-25 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfoodfact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='product_name',
            new_name='name',
        ),
    ]
