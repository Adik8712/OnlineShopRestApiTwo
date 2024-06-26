# Generated by Django 5.0.3 on 2024-03-21 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_client',
            field=models.BooleanField(default=True, help_text='Определение, является ли аккаунт клиентом', verbose_name='Клиент'),
        ),
        migrations.AddField(
            model_name='account',
            name='is_delivery',
            field=models.BooleanField(default=False, help_text='Определение, является ли аккаунт службой доставки', verbose_name='Доставка'),
        ),
        migrations.AddField(
            model_name='account',
            name='is_support',
            field=models.BooleanField(default=False, help_text='Определение, является ли аккаунт службой поддержки', verbose_name='Поддержка'),
        ),
    ]
