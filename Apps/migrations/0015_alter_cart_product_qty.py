# Generated by Django 4.2.3 on 2023-07-22 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0014_rename_product_cart_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product_qty',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
