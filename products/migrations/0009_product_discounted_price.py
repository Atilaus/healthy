# Generated by Django 2.2.2 on 2019-06-29 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20190629_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discounted_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]
