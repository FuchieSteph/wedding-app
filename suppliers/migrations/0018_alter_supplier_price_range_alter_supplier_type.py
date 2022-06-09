# Generated by Django 4.0.3 on 2022-04-16 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0017_rename_supplier_supplier_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='price_range',
            field=models.CharField(blank=True, choices=[(1, '€'), (2, '€€'), (3, '€€€')], max_length=200),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='type',
            field=models.CharField(blank=True, choices=[('caterer', 'Caterer'), ('reception', 'Reception'), ('other', 'Other')], max_length=200),
        ),
    ]