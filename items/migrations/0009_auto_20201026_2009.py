# Generated by Django 3.1.2 on 2020-10-26 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_auto_20201026_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipments',
            name='Name',
            field=models.CharField(max_length=100),
        ),
    ]
