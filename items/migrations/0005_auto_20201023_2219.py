# Generated by Django 3.1.2 on 2020-10-23 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_equipments_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipments',
            name='Date',
            field=models.CharField(max_length=12),
        ),
    ]
