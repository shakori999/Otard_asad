from typing import List

from inventory.models import *
from ninja import Field, ModelSchema


class CategorySchema(ModelSchema):
    class Config:
        model = Category
        model_fields = ["name", "slug"]


class ProductSchema(ModelSchema):
    class Config:
        model = Product
        model_fields = ["name", "web_id"]


class BrandSchema(ModelSchema):
    class Config:
        model = Brand
        model_fields = ["name"]


class MediaSchema(ModelSchema):

    img_url: str

    class Config:
        model = Media
        model_fields = ["img_url", "alt_text"]


class ProductTypeSchema(ModelSchema):
    class Config:
        model = ProductType
        model_fields = ["name"]


class ProductAttributeValueSchema(ModelSchema):
    class Config:
        model = ProductAttributeValue
        model_fields = "__all__"


class InventorySchema(ModelSchema):

    brand: BrandSchema
    product: ProductSchema
    media: List[MediaSchema] = Field(
        # alias refere to related_name on a model
        alias="media_product_inventory",
    )
    product_type: ProductTypeSchema
    attributes: List[ProductAttributeValueSchema] = Field(
        alias="attribute_values",
    )

    class Config:
        model = ProductInventory
        model_fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            "weight",
        ]
