from django.db import models
from apps.accounts.models import Account


class ChatSupport(models.Model):
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name="Аккаунт",
        help_text="Аккаунт, к которому относится чат"
    )
    message = models.TextField(
        verbose_name="Сообщение",
        help_text="Текст сообщения в чате"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата и время создания записи"
    )

    def __str__(self) -> str:
        return f"{self.account.username} - {self.created_at}"

    class Meta:
        verbose_name = "Чат поддержки"
        verbose_name_plural = "Чаты поддержки"
        ordering = ["created_at"]


class MarketSupport(models.Model):
    name = models.CharField(
        max_length=50, 
        verbose_name='Название', 
        help_text='Название магазина'
    )
    description = models.TextField(
        verbose_name='Описание', 
        help_text='Описание магазина'
    )
    open_time = models.TimeField(
        verbose_name='Время открытия', 
        help_text='Время начала работы магазина'
    )
    close_time = models.TimeField(
        verbose_name='Время закрытия', 
        help_text='Время окончания работы магазина'
    )

    the_cost_of_delivery = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name='Стоимость доставки', 
        help_text='Стоимость доставки заказа'
    )
    minimum_order = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name='Мин заказ', 
        help_text='Минимальная сумма заказа'
    )

    maximum_distance_without_extra_charge = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name='Мак расстояние без платы', 
        help_text='Максимальное расстояние для бесплатной доставки'
    )

    address = models.CharField(
        max_length=255, 
        verbose_name='Адрес', 
        help_text='Адрес магазина'
    )
    phone_number = models.CharField(
        max_length=12, 
        null=True, 
        blank=True, 
        verbose_name='Номер телефона',
        help_text='Номер телефона магазина'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата создания', 
        help_text='Дата и время создания записи'
    )

    def __str__(self) -> str:
        return f"{self.pk}. {self.name} | {self.open_time} - {self.close_time}"
    
    class Meta:
        verbose_name = "Регистрация Маркета"
        verbose_name_plural = "Регистрация Маркетов"
        ordering = ['-created_at']


class NotificationSupport(models.Model):
    support_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name="Аккаунт поддержки",
        help_text="Аккаунт службы поддержки, к которому относится уведомление"
    )

    chat_support = models.ForeignKey(
        ChatSupport,
        on_delete=models.CASCADE,
        verbose_name="Чат поддержки",
        help_text="Чат поддержки, откуда пришло уведомление"
    )

    is_read = models.BooleanField(
        default=False,
        verbose_name="Прочитано",
        help_text="Статус прочтения уведомления"
    )

    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата создания', 
        help_text='Дата и время создания записи'
    )

    def support_is_read(self, *args, **kwargs):
        if self.is_read:
            return "Прочитано"
        
        return "Не прочитано"

    def __str__(self) -> str:
        return f"Для {self.support_account.username} - {self.chat_support.pk} - "

    class Meta:
        verbose_name = "Уведомление поддержки"
        verbose_name_plural = "Уведомления поддержки"
        ordering = ['-created_at']


