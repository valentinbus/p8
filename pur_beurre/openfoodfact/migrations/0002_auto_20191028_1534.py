# Generated by Django 2.2.6 on 2019-10-28 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openfoodfact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='nutriscore',
            field=models.CharField(max_length=10),
        ),
    ]
