# Generated by Django 4.2.3 on 2023-07-09 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_id',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]