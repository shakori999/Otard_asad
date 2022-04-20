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


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug", "is_active"]
        read_only = True


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "web_id",
        ]
        read_only = True
        editable = False


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductType
        fields = [
            "name",
        ]
        read_only = True
        editable = False


class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = [
            "id",
            "sku",
            "upc",
            "product_type",
            "product",
            "brand",
            "is_active",
            "is_default",
            "retail_price",
            "store_price",
            "is_digital",
            "weight",
        ]


class ProductInventoryReadSerializer(ProductInventorySerializer):
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
    product_type = ProductTypeSerializer(many=False, read_only=True)
    promotion_price = serializers.SerializerMethodField()

    class Meta:
        model = ProductInventory
        fields = [
            "id",
            "sku",
            "store_price",
            "retail_price",
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


class OrderedViewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = (
            # "id",
            "ordered_date",
            "name",
            "phone_number",
            "price",
            "address",
            "address_2",
        )


class OrderItemSummarySerializer(serializers.ModelSerializer):

    item_name = serializers.CharField(source="get_product_name", read_only=True)
    individual_price = serializers.CharField(
        source="get_individual_price", read_only=True
    )
    total_price = serializers.CharField(source="get_final_price", read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            "item_name",
            "quantity",
            "individual_price",
            "total_price",
        ]


class OrderSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "items",
            "start_date",
            "ordered_date",
            "ordered",
            "name",
            "phone_number",
            "address",
            "address_2",
            "price",
        ]


class OrderSummaryReadSerializer(OrderSummarySerializer):
    items = OrderItemSummarySerializer(many=True, read_only=True)
    order = Order.objects.get(ordered=False)
    order.price = order.get_total()
    order_total_price = serializers.CharField(source="get_total", read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "items",
            "order_total_price",
            # "start_date",
            # "ordered_date",
            # "ordered",
            # "name",
            # "phone_number",
            # "address",
            # "address_2",
            # "price",
        ]


class OrderedDetailSerializer(serializers.HyperlinkedModelSerializer):

    items = OrderItemSummarySerializer(many=True, read_only=True)
    order_total_price = serializers.CharField(source="get_total", read_only=True)

    class Meta:
        model = Order
        fields = [
            "name",
            "phone_number",
            "address",
            "items",
            "order_total_price",
        ]
