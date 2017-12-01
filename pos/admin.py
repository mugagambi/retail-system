from django.contrib import admin
from pos.models import Receipt, ReceiptItem


class ReceiptInline(admin.TabularInline):
    model = ReceiptItem


class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('receipt_no', 'receipt_total', 'date')
    search_fields = ('receipt_no',)
    date_hierarchy = 'date'
    inlines = [ReceiptInline]


# Register your models here.
admin.site.register(Receipt, ReceiptAdmin)
