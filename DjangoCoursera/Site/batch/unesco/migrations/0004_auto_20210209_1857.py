# Generated by Django 3.1.4 on 2021-02-09 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0003_auto_20210209_1847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='area_hec',
            new_name='area_hectares',
        ),
    ]
