# Generated by Django 4.0.3 on 2022-04-17 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0019_alter_supplier_price_range'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.CharField(blank=True, choices=[('caterer', 'Caterer'), ('reception', 'Reception'), ('other', 'Other')], max_length=200),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='price_range',
            field=models.IntegerField(blank=True, choices=[(1, '€'), (2, '€€'), (3, '€€€')]),
        ),
    ]
