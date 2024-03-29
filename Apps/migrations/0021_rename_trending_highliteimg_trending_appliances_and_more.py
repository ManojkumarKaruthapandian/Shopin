# Generated by Django 4.2.3 on 2023-07-30 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0020_rename_mainproductimg_highliteimg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='highliteimg',
            old_name='trending',
            new_name='trending_Appliances',
        ),
        migrations.AddField(
            model_name='highliteimg',
            name='trending_Electronics',
            field=models.BooleanField(default=False, help_text='0-default,1-trending'),
        ),
        migrations.AddField(
            model_name='highliteimg',
            name='trending_Fashion',
            field=models.BooleanField(default=False, help_text='0-default,1-trending'),
        ),
        migrations.AddField(
            model_name='highliteimg',
            name='trending_Mobiles',
            field=models.BooleanField(default=False, help_text='0-default,1-trending'),
        ),
    ]
