from rest_framework import serializers
from inventory.models import *


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

    class Meta:
        model = ProductInventory
        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            "brand",
            "product",
            "is_on_sale",
            "weight",
            "media",
            "attributes",
            "product_type",
        ]
        read_only = True


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
