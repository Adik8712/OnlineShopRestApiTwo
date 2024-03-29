from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.accounts.models import Address, Account


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('city', 'street', 'house', 'flat', 'created_at')
    search_fields = ('city', 'street', 'house', 'flat')
    list_filter = ('city',)
    readonly_fields = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('city', 'street', 'house', 'flat')
        }),
        ('Дополнительная информация', {
            'fields': ('other',),
            'classes': ('collapse',)
        }),
        ('Важные даты', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Account)
class AccountAdmin(UserAdmin):
    model = Account
    list_display = ('username', 'email', 'phone_number', 'country', 'bonus')
    search_fields = ('username', 'email', 'phone_number', 'country')
    list_filter = ('is_client', 'is_delivery', 'is_support', 'country',)
    readonly_fields = ('date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Личная информация', {'fields': ('email', 'first_name', 'last_name', 'image', 'birthday', 'phone_number', 'country')}),
        ('Разрешения', {'fields': ('is_client', 'is_delivery', 'is_support', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    filter_horizontal = ('groups', 'user_permissions', 'my_address')

