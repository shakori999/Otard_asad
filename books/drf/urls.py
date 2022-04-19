from unicodedata import name
from django.urls import path
from rest_framework import routers

from .views import *
from search.views import SearchProductInventory

urlpatterns = [
    # API endpoints for order managment system
    # ealsticsearch
    # path("api/search/<str:query>/", SearchProductInventory.as_view()),
]

router = routers.DefaultRouter()
# Orders API endpoints
router.register(r"ordered-view", OrderedViewList, basename="ordered-view")
router.register(r"order-summary", OrderSummary, basename="order-summary")
# Products API endpoints
router.register(r"category", CategoryList, basename="category-all")
router.register(r"inventory", ProductInventoryByWebId, basename="product-by-web-id")
# Search API endpoint
