# Generated by Django 2.2.6 on 2019-10-22 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('nutriscore', models.CharField(max_length=1)),
                ('category', models.CharField(max_length=50)),
                ('url_op', models.CharField(max_length=200)),
                ('url_image_recto', models.CharField(max_length=200)),
                ('url_image_verso', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Saves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_to_replace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_to_replace', to='openfoodfact.Products')),
                ('replace_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replace_product', to='openfoodfact.Products')),
            ],
        ),
    ]
