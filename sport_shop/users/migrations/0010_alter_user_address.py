# Generated by Django 5.0.1 on 2024-01-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0009_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(default='', max_length=200, verbose_name='Адрес доставки'),
        ),
    ]
