# Generated by Django 4.2.3 on 2023-07-18 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Apps', '0012_rename_quandity_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_qty', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Apps.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
