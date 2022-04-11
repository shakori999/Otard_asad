from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers
from inventory.models import *
from promotion.models import Promotion
from order.models import *


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]
        read_only = True


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        exclude = ["id"]
        depth = 2
        read_only = True


class ProductMediaSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = [
            "img_url",
            "alt_text",
        ]
        read_only = True
        editable = False

    def get_img_url(self, obj):
        return obj.img_url.url


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug", "is_active"]
        read_only = True


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "web_id",
        ]
        read_only = True
        editable = False


class ProductInventorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    brand = BrandSerializer(many=False, read_only=True)
    attributes = ProductAttributeValueSerializer(
        source="attribute_values",
        many=True,
        read_only=True,
    )
    media = ProductMediaSerializer(
        source="media_product_inventory",
        many=True,
        read_only=True,
    )
    promotion_price = serializers.SerializerMethodField()

    class Meta:
        model = ProductInventory
        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            "brand",
            "product",
            "weight",
            "media",
            "attributes",
            "product_type",
            "promotion_price",
        ]
        read_only = True

    def get_promotion_price(self, obj):
        try:
            x = Promotion.products_on_promotion.through.objects.get(
                Q(promotion_id__is_active=True) & Q(product_inventory_id=obj.id)
            )
            return x.promo_price
        except ObjectDoesNotExist:
            return None


class ProductInventorySearchSerializer(serializers.ModelSerializer):

    product = ProductSerializer(many=False, read_only=True)
    brand = BrandSerializer(many=False, read_only=True)

    class Meta:
        model = ProductInventory
        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            "product",
            "brand",
        ]


class OrderItemSerializer(serializers.ModelSerializer):

    item = ProductInventorySerializer(many=False, read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            # "user",
            "ordered",
            "item",
            "quantity",
        ]


class OrderedViewSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            "items",
            "ordered_date",
            "ordered",
            "name",
            "phone_number",
            "address",
            "address_2",
            "price",
        ]


class OrderSummarySerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            "items",
            "ordered",
            "name",
            "phone_number",
            "address",
            "address_2",
            "price",
        ]
