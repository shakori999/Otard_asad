from django.contrib import admin
from .models import *

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "ordered_date",
    )

    def save_model(self, request, obj, form, change):
        obj.price = obj.get_total()

        super().save_model(request, obj, form, change)


class OrderItemAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.price = obj.get_final_price()

        super().save_model(request, obj, form, change)


admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
