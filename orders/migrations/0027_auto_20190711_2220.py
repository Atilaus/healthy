# Generated by Django 2.2.2 on 2019-07-11 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_productincart_image_path'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productincart',
            old_name='image_path',
            new_name='image_url',
        ),
        migrations.RenameField(
            model_name='productinorder',
            old_name='image_path',
            new_name='image_url',
        ),
    ]
