from django.urls import path
from .views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path(
        "product-by-category/<slug:category>/",
        product_by_category,
        name="product_by_category",
    ),
    path("<slug:slug>", product_detail, name="product_detail"),
]
