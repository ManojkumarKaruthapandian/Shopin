# Generated by Django 4.2.3 on 2023-07-18 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0013_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='Product',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='Product_qty',
            new_name='product_qty',
        ),
    ]
