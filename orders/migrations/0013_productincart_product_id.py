# Generated by Django 2.2.2 on 2019-07-04 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20190704_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='productincart',
            name='product_id',
            field=models.IntegerField(default=0),
        ),
    ]
