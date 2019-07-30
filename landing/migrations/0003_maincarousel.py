# Generated by Django 2.2.2 on 2019-07-27 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20190622_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='mainCarousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, default=None, max_length=64, null=True)),
                ('image', models.ImageField(upload_to='static/main_carousel')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Carousel Image',
                'verbose_name_plural': 'Main Carousel Images',
            },
        ),
    ]