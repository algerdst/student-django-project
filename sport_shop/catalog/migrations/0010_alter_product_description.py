# Generated by Django 5.0.1 on 2024-01-17 07:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0009_brand_slug_itemtype_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Описание'),
        ),
    ]
