# Generated by Django 2.2.2 on 2019-07-04 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20190704_2210'),
        ('orders', '0013_productincart_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productincart',
            name='product_id',
        ),
        migrations.AddField(
            model_name='productincart',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.Product'),
        ),
    ]