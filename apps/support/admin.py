from django.contrib import admin
from apps.support.models import ChatSupport, MarketSupport, NotificationSupport


@admin.register(ChatSupport)
class ChatSupportAdmin(admin.ModelAdmin):
    list_display = ('account', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('account__username', 'message')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('account', 'message')
        }),
        ('Дата создания', {
            'fields': ('created_at',),
            'classes': ('collapse',) 
        }),
    )


@admin.register(MarketSupport)
class MarketSupportAdmin(admin.ModelAdmin):
    list_display = ('name', 'open_time', 'close_time', 'the_cost_of_delivery', 'minimum_order', 'maximum_distance_without_extra_charge', 'address', 'phone_number', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'address')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description', 'open_time', 'close_time', 'the_cost_of_delivery', 'minimum_order', 'maximum_distance_without_extra_charge', 'address', 'phone_number')
        }),
        ('Дата создания', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(NotificationSupport)
class NotificationSupportAdmin(admin.ModelAdmin):
    list_display = ('support_account', 'chat_support', 'support_is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('support_account__username', 'chat_support__message')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('support_account', 'chat_support', 'is_read')
        }),
        ('Дата создания', {
            'fields': ('created_at',),
            'classes': ('collapse',) 
        }),
    )