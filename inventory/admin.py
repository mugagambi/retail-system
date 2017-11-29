from django.contrib import admin
from inventory import models


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_units', 'remaining_units', 'unit_price', 'description', 'account')
    list_select_related = True


# Register your models here.,
admin.site.register(models.Item, ItemAdmin)
