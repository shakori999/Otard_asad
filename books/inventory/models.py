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

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
