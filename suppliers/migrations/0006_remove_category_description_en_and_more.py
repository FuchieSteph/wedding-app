# Generated by Django 4.0.3 on 2022-03-13 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0005_alter_supplier_price_range'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description_fr',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_fr',
        ),
    ]
