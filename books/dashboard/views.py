from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from django.db.models import Count
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

    return render(request, "books/product_detail.html", {"data": data})
