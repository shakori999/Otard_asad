from rest_framework import serializers
from inventory.models import *


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        exclude = ["id"]
        depth = 2


class AllProducts(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ["name"]
        rad_only = True
        editable = False


class ProductInventorySerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False, read_only=True)
    attribute = ProductAttributeValueSerializer(
        source="attribute_values",
        many=True,
        read_only=True,
    )

    class Meta:
        model = ProductInventory
        fields = [
            "sku",
            "store_price",
            "is_default",
            "product",
            "product_type",
            "brand",
            "attribute",
        ]
        read_only = True
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'
