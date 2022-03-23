from itertools import product
from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

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
        "id", "name", "slug", "category__name", "product__store_price"
    )

    return render(request, "category/product_by_category.html", {"data": data})


# class product_detail(DetailView):
#     model = Product
#     context_object_name = "book"
#     template_name = "books/product-page.html"
#     login_url = "account_login"
def product_detail(request, slug):

    data = ProductInventory.objects.filter(product__slug=slug).values(
        "id",
        "sku",
        "product__name",
        "store_price",
        "product_inventory__units",
    )

    return render(request, "books/product_detail.html", {"data": data})
