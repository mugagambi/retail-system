from django.contrib import admin
from commerce import models


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_first_name', 'get_last_name', 'get_email', 'get_date_joined', 'get_last_login',
                    'shipping_address')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')

    def get_username(self, obj):
        return obj.user.username

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_email(self, obj):
        return obj.user.email

    def get_date_joined(self, obj):
        return obj.user.date_joined

    def get_last_login(self, obj):
        return obj.user.last_login

    get_username.short_description = 'Username'
    get_username.admin_order_field = 'user__username'
    get_first_name.short_description = 'First Name'
    get_first_name.admin_order_field = 'user__first_name'
    get_last_name.short_description = 'Last Name'
    get_last_name.admin_order_field = 'user__last_name'
    get_email.short_description = 'Email'
    get_email.admin_order_field = 'user__email'
    get_date_joined.short_description = 'Date Joined'
    get_date_joined.admin_order_field = 'user__date_joined'
    get_last_login.short_description = 'Last Log In'
    get_last_login.admin_order_field = ('user__last_login',)


class OrderAdmin(admin.ModelAdmin):
    fields = ('customer', 'item', 'quantity', 'processed')
    list_display = ('customer', 'item', 'quantity', 'processed')
    list_filter = ('processed',)


# Register your models here.


admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Order, OrderAdmin)
