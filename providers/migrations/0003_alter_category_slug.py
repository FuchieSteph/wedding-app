# Generated by Django 4.0.2 on 2022-02-19 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0002_remove_category_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
