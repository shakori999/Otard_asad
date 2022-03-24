from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from django.db.models import Count
from django.contrib.postgres.aggregates import ArrayAgg

from inventory.models import *

# Create your views here.


class HomePageView(ListView):
    def get(self, *args, **kwargs):
        category = Category.objects.all()
        # item = ProductInventory.objects.all()
        context = {
            "category": category,
            # "items": item,
        }

        return render(self.request, "home-page.html", context)


def product_by_category(request, category):
    data = Product.objects.filter(category__name=category).values(
        "id",
        "name",
        "slug",
        "category__name",
        "product__store_price",
    )

    return render(request, "category/product_by_category.html", {"data": data})


def product_detail(request, slug):

    filter_arguments = []

    if request.GET:
        for value in request.GET.values():
            filter_arguments.append(value)

        data = (
            ProductInventory.objects.filter(product__slug=slug)
            .filter(attribute_values__attribute_value__in=filter_arguments)
            .annotate(num_tags=Count("attribute_values"))
            .filter(num_tags=len(filter_arguments))
            .values(
                "id",
                "sku",
                "product__name",
                "store_price",
                "product_inventory__units",
            )
        )
    else:
        data = (
            ProductInventory.objects.filter(product__slug=slug)
            .filter(is_default=True)
            .values(
                "id",
                "sku",
                "product__name",
                "store_price",
                "product_inventory__units",
            )
            .annotate(field_a=ArrayAgg("attribute_values__attribute_value"))
            .get()
        )

    productTypeAttributes = (
        ProductInventory.objects.filter(product__slug=slug)
        .distinct()
        .values(
            "attribute_values__product_attribute__name",
            "attribute_values__attribute_value",
        )
    )
    ProductAttributeNames = (
        ProductTypeAttribute.objects.filter(
            product_type__product_type__product__slug=slug
        )
        .values("product_attribute__name")
        .distinct()
    )
    context = {
        "data": data,
        "productTypeAttributes": productTypeAttributes,
        "ProductAttributeNames": ProductAttributeNames,
    }

    return render(request, "books/product_detail.html", context)
