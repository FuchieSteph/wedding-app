# Generated by Django 4.0.3 on 2022-03-13 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0009_category_description_en_category_description_fr_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='category_id',
            new_name='category',
        ),
    ]
