# Generated by Django 3.1.7 on 2021-03-28 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='delivery_date',
        ),
    ]
