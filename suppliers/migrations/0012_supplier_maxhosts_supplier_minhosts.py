# Generated by Django 4.0.3 on 2022-03-15 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0011_supplier_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='maxhosts',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='minhosts',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]