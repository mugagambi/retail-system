from django.contrib import admin
from accounts import models


class IncomeAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'created_at')
    date_hierarchy = 'created_at'


class ExpenditureAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'created_at')
    date_hierarchy = 'created_at'


# Register your models here.
admin.site.register(models.IncomeAccount, IncomeAccountAdmin)
admin.site.register(models.ExpenditureAccount, ExpenditureAccountAdmin)
