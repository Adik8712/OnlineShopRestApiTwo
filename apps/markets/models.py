from django.db import models

class Market(models.Model):
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
        verbose_name = "Маркет"
        verbose_name_plural = "Маркеты"
        ordering = ['-created_at']


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Название категории"
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Описание категории",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата и время создания записи"
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['-created_at']


class Product(models.Model):
    market = models.ForeignKey(
        Market,
        on_delete=models.CASCADE,
        verbose_name='Магазин',
        help_text='Магазин продукта'
    )
    image = models.ImageField(
        upload_to='products/',
        verbose_name='Изображение',
        help_text='Изображение продукта'
    )
    code = models.CharField(
        max_length=255,
        verbose_name="Код",
        help_text="Код продукта"
    )
    name = models.CharField(
        max_length=255, 
        verbose_name="Название", 
        help_text="Название продукта"
    )
    brand = models.CharField(
        max_length=255, 
        verbose_name="Бренд", 
        help_text="Бренд продукта",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        help_text='Категория продукта'
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Цена", 
        help_text="Цена продукта"
    )
    stock = models.IntegerField(
        verbose_name="Остаток на складе", 
        help_text="Доступное количество продукта на складе",
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name="Описание", 
        help_text="Описание продукта",
        blank=True,
        null=True,
    )
    calories = models.FloatField(
        verbose_name="Калории", 
        help_text="Количество калорий в порции продукта",
        blank=True,
        null=True,
    )
    fat = models.FloatField(
        verbose_name="Жиры", 
        help_text="Количество жиров в порции продукта",
        blank=True,
        null=True,
    )
    carbohydrates = models.FloatField(
        verbose_name="Углеводы", 
        help_text="Количество углеводов в порции продукта",
        blank=True,
        null=True,
    )
    protein = models.FloatField(
        verbose_name="Белки", 
        help_text="Количество белков в порции продукта",
        blank=True,
        null=True,
    )
    fiber = models.FloatField(
        verbose_name="Пищевые волокна", 
        help_text="Количество пищевых волокон в порции продукта",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата и время создания записи"
    )

    def __str__(self) -> str:
        return f"{self.pk}. {self.name} | {self.category.name} | {self.price}"
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['-created_at']
