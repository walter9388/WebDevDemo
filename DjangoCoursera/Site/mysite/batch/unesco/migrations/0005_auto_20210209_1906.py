# Generated by Django 3.1.4 on 2021-02-09 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0004_auto_20210209_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='iso',
        ),
        migrations.AddField(
            model_name='site',
            name='iso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='unesco.iso'),
        ),
    ]
