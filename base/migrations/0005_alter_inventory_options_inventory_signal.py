# Generated by Django 4.0.4 on 2022-09-24 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_inventory_delete_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name_plural': 'Inventories'},
        ),
        migrations.AddField(
            model_name='inventory',
            name='signal',
            field=models.BooleanField(default=False),
        ),
    ]
