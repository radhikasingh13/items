# Generated by Django 3.1.2 on 2020-10-23 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20201022_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipments',
            name='Name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='equipments',
            name='Price',
            field=models.FloatField(max_length=20),
        ),
    ]
