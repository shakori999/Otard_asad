from django.contrib import admin
from .models import *
# Register your models here.

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('user','ordered_date',)


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address',)
admin.site.register(OrderItem)
admin.site.register(Order, OrderItemAdmin)
admin.site.register(Invoice, InvoiceAdmin)