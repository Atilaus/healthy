# Generated by Django 2.2.2 on 2019-07-04 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20190704_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='final_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]
