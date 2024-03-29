from django.contrib import admin
from apps.markets.models import Market, Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основная информация', {
            'fields': ('market', 'code', 'name', 'brand', 'category', 'price', 'stock')
        }),
        ('Пищевая ценность', {
            'fields': ('calories', 'fat', 'carbohydrates', 'protein', 'fiber'),
            'classes': ('collapse',)  # Это скроет этот раздел по умолчанию
        }),
        ('Дополнительно', {
            'fields': ('description', 'created_at'),
            'classes': ('collapse',)  # Это скроет этот раздел по умолчанию
        }),
    )

    list_display = ('name', 'brand', 'category', 'price', 'stock', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'brand')
    readonly_fields = ('created_at',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('created_at',)


@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description', 'address', 'phone_number')
        }),
        ('Время работы', {
            'fields': ('open_time', 'close_time')
        }),
        ('Доставка', {
            'fields': ('the_cost_of_delivery', 'minimum_order', 'maximum_distance_without_extra_charge')
        }),
        ('Дополнительно', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    list_display = ('name', 'open_time', 'close_time', 'the_cost_of_delivery', 'minimum_order', 'maximum_distance_without_extra_charge', 'created_at')
    search_fields = ('name', 'address', 'phone_number')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
