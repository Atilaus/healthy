# Generated by Django 2.2.2 on 2019-07-27 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_maincarousel'),
    ]

    operations = [
        migrations.AddField(
            model_name='maincarousel',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
