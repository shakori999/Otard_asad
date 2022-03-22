import uuid
from django.db import models
from django.forms import BooleanField
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField

# Create your models here.


class Category(MPTTModel):
    """
    Inventory Category  table implimented with MPTT
    """

    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("category name"),
        help_text=_("format: requied, max-100"),
    )
    slug = models.SlugField(
        max_length=150,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("category safe URL"),
        help_text=_("format: required letters, numbers, underscore, or hyphens"),
    )

    is_active = models.BooleanField(default=True)
    parent = TreeForeignKey(
        "self",
        blank=True,
        null=True,
        unique=False,
        related_name="childern",
        verbose_name=_("parent of category"),
        on_delete=models.PROTECT,
        help_text=_("format: not required"),
    )

    class Meta:
        verbose_name = _("product category")
        verbose_name_plural = _("product Categories")

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product details table
    """

    web_id = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("prodcut webist ID"),
        help_text=_("format: required, unique"),
    )
    slug = models.SlugField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product safe URL"),
        help_text=_("format: required, letters, numbers, underscores or hyphens"),
    )
    name = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product name"),
        help_text=_("format: required, max-255"),
    )
    description = models.TextField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product description"),
        help_text=_("format: required"),
    )
    category = TreeManyToManyField(Category)
    is_active = models.BooleanField(
        unique=False,
        null=False,
        blank=False,
        default=True,
        verbose_name=_("product visibility"),
        help_text=_("format: true=product visible"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("date product created"),
        help_text=_("format: Y-m-d H:M:S"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("date product last updated"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    def __str__(self):
        return self.name


class ProductType(models.Model):
    """
    Product type table
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("type of product"),
        help_text=_("format: required, unique, max-255"),
    )

    def __str__(self):
        return self.name


class Brand(models.Model):
    """
    Product brand table
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("brand name"),
        help_text=_("format: required, unique, max-255"),
    )


# class ProductAttribute(models.Model):
#     """
#     Product attribute table
#     """

#     name = models.CharField(
#         max_length=255,
#         unique=True,
#         null=False,
#         blank=False,
#         verbose_name=_("product attribute name"),
#         help_text=_("format: required, unique, max-255"),
#     )
#     description = models.TextField(
#         unique=False,
#         null=False,
#         blank=False,
#         verbose_name=_("product attribute description"),
#         help_text=_("format: required"),
#     )

#     def __str__(self):
#         return self.name


# class ProductAttributeValue(models.Model):
#     """
#     Product attribute value table
#     """

#     product_attribute = models.ForeignKey(
#         ProductAttribute,
#         related_name="product_attribute",
#         on_delete=models.PROTECT,
#     )
#     attribute_value = models.CharField(
#         max_length=255,
#         unique=False,
#         null=False,
#         blank=False,
#         verbose_name=_("attribute value"),
#         help_text=_("format: required, max-255"),
#     )

#     def __str__(self):
#         return f"{self.product_attribute.name} : {self.attribute_value}"


class ProductInventory(models.Model):
    """
    Product inventory table
    """

    sku = models.CharField(
        max_length=20,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("stock keeping unit"),
        help_text=_("format: required, unique, max-20"),
    )
    upc = models.CharField(
        max_length=12,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("universal product code"),
        help_text=_("format: required, unique, max-12"),
    )
    product_type = models.ForeignKey(
        ProductType, related_name="product_type", on_delete=models.PROTECT
    )
    product = models.ForeignKey(
        Product, related_name="product", on_delete=models.PROTECT
    )
    brand = models.ForeignKey(Brand, related_name="brand", on_delete=models.PROTECT)
    # attribute_values = models.ManyToManyField(
    #     ProductAttributeValue,
    #     related_name="product_attribute_values",
    #     through="ProductAttributeValues",
    # )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("product visibility"),
        help_text=_("format: true=product visible"),
    )
    retail_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("recommended retail price"),
        help_text=_("format: maximum price 999.99"),
        error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999.99."),
            },
        },
    )
    store_price = models.DecimalField(
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
    sale_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("sale price"),
        help_text=_("format: maximum price 999.99"),
        error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999.99."),
            },
        },
    )
    weight = models.FloatField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product weight"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("date sub-product created"),
        help_text=_("format: Y-m-d H:M:S"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("date sub-product updated"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    def __str__(self):
        return self.product.name
