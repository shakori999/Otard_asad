from django.contrib import admin

# Register your models here.

from .models import *


class ProductOnPromotion(admin.StackedInline):
    model = Promotion.products_on_promotion.through
    extra = 2
    raw_id_fields = ("product_inventory_id",)


class ProductInventoryList(admin.ModelAdmin):
    model = Promotion
    inlines = (ProductOnPromotion,)
    list_display = (
        "name",
        "is_active",
        "promo_start",
        "promo_end",
    )


admin.site.register(Promotion, ProductInventoryList)
admin.site.register(PromoType)
admin.site.register(Coupon)
