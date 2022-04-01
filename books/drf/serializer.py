from rest_framework import serializers
from inventory.models import *


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        exclude = ["id"]
        depth = 2


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ["name"]


class MediaSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = [
            "image",
            "alt_text",
        ]
        read_only = True
        editable = False

    def get_image(self, obj):
        return self.context["request"].build_absolute_uri(obj.image.url)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
        ]
        read_only = True
        editable = False


class AllProducts(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only = True
        editable = False


class ProductInventorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    # brand = BrandSerializer(many=False, read_only=True)
    # attribute = ProductAttributeValueSerializer(
    #     source="attribute_values",
    #     many=True,
    #     read_only=True,
    # )
    # image = MediaSerializer(
    #     source="media_product_inventory",
    #     many=True,
    # )
    # type = ProductTypeSerializer(
    #     source="product_type",
    #     many=False,
    #     read_only=True,
    # )

    # price = serializers.DecimalField(
    #     source="retail_price", max_digits=5, decimal_places=2
    # )

    class Meta:
        model = ProductInventory
        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            "product",
        ]
        read_only = True
