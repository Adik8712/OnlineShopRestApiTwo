from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser


class Address(models.Model):
    city = models.CharField(
        max_length=50, 
        verbose_name='Город', 
        help_text='Название города'
    )
    street = models.CharField(
        max_length=50, 
        verbose_name='Улица', 
        help_text='Название улицы'
    )
    house = models.CharField(
        max_length=50, 
        verbose_name='Дом', 
        help_text='Номер дома'
    )
    flat = models.CharField(
        max_length=50, 
        verbose_name='Квартира', 
        help_text='Номер квартиры'
    )

    other = models.CharField(
        max_length=100, 
        null=True, 
        blank=True, 
        verbose_name='Дополнительно',
        help_text='Дополнительная информация об адресе'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата создания', 
        help_text='Дата и время создания записи'
    )

    def __str__(self):
        return f'{self.city}, {self.street}, {self.house}, {self.flat}'
    
    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
        ordering = ['-created_at']


class Account(AbstractUser):
    image = models.ImageField(
        upload_to='users_images', 
        blank=True, 
        verbose_name='Изображение',
        help_text='Изображение пользователя'
    )
    birthday = models.DateField(
        null=True, 
        blank=True, 
        verbose_name='Дата рождения', 
        help_text='Дата рождения пользователя'
    )
    phone_number = models.CharField(
        max_length=12, 
        null=True, 
        blank=True, 
        verbose_name='Номер телефона',
        help_text='Номер телефона пользователя'
    )
    country = models.CharField(
        max_length=50, 
        null=True, 
        blank=True, 
        verbose_name='Страна',
        help_text='Название страны пользователя'
    )
    bonus = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0, 
        verbose_name='Бонусы',
        help_text='Количество бонусов у пользователя'
    )
    my_address = models.ManyToManyField(
        Address, 
        blank=True, 
        verbose_name='Мои адреса',
        help_text='Список адресов пользователя'
    )
    is_client = models.BooleanField(
        default=True,
        verbose_name="Клиент",
        help_text="Определение, является ли аккаунт клиентом"
    )
    is_delivery = models.BooleanField(
        default=False,
        verbose_name="Доставка",
        help_text="Определение, является ли аккаунт службой доставки"
    )
    is_support = models.BooleanField(
        default=False,
        verbose_name="Поддержка",
        help_text="Определение, является ли аккаунт службой поддержки"
    )

    def __str__(self) -> str:
        return self.username
