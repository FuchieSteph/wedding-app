# Generated by Django 4.0.3 on 2022-03-15 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0013_tag_suppliertag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suppliertag',
            name='level',
        ),
        migrations.RemoveField(
            model_name='suppliertag',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='suppliertag',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='suppliertag',
            name='tree_id',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='level',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='tree_id',
        ),
    ]