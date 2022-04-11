import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from inventory.models import *

# from books.models import *
from checkout.models import *

# Create your models here.


class OrderItem(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(ProductInventory, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("regular store price"),
        help_text=_("format: maximum price 999.99"),
        error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999.99."),
            },
        },
    )

    def __str__(self):
        return f"{self.quantity} of {self.item.product.name}"

    def get_product_name(self):
        return f"{self.item.product.name}"

    def get_individual_price(self):
        return self.item.store_price

    def get_final_price(self):
        price = self.quantity * self.item.store_price
        return price


class Order(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    address_2 = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["id"], name="id_order"),
        ]

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("order_detail", args=[str(self.id)])

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return str(total)
