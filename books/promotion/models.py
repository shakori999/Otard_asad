from decimal import Decimal
from django.db import models
from inventory.models import ProductInventory
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from django.utils.translation import gettext_lazy as _

# Create your models here.


class PromoType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Coupon(models.Model):
    name = models.CharField(max_length=255)
    coupon_code = models.CharField(max_length=20)


class Promotion(models.Model):
    name = models.CharField(max_length=255, unique=True)
    discription = models.TextField(blank=True)
    promo_reduction = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    is_schedule = models.BooleanField(default=False)
    promo_start = models.DateField()
    promo_end = models.DateField()

    products_on_promotion = models.ManyToManyField(
        ProductInventory,
        related_name="products_on_promotion",
        through="ProductsOnPromotion",
    )

    promo_type = models.ForeignKey(
        PromoType,
        related_name="promotype",
        on_delete=models.PROTECT,
    )

    coupon = models.ForeignKey(
        Coupon,
        related_name="coupon",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    def clean(self):
        if self.promo_start > self.promo_end:
            raise ValidationError(_("end data befor the start date"))

    def __str__(self):
        return self.name


class ProductsOnPromotion(models.Model):
    product_inventory_id = models.ForeignKey(
        ProductInventory,
        related_name="productInventoryOnPromotion",
        on_delete=models.PROTECT,
    )
    promotion_id = models.ForeignKey(
        Promotion,
        related_name="promotion",
        on_delete=models.CASCADE,
    )
    promo_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=Decimal("0.00"),
        validators=[
            MinValueValidator(Decimal("0.00")),
        ],
    )
    price_override = models.BooleanField(default=True)

    class Meta:
        unique_together = ("product_inventory_id", "promotion_id")
