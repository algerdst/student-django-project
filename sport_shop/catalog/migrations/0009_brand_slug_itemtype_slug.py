# Generated by Django 5.0.1 on 2024-01-16 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_product_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='itemtype',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]