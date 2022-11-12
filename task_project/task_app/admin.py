from django.contrib import admin

from .models import (
    BShop,
    Record,
)


class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'barber_name', 'record_date', 'bshop')
    search_fields = ('name', 'record_date')


class BShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name',)


admin.site.register(BShop, BShopAdmin)
admin.site.register(Record, RecordAdmin)
