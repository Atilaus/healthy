# Generated by Django 2.2.2 on 2019-07-11 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20190706_1553'),
        ('orders', '0022_auto_20190708_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='productincart',
            name='image',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='products.ProductImage'),
        ),
    ]