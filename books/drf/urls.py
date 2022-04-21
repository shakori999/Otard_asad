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
router.register(
    r"order-summary",
    OrderSummary,
    basename="order-summary",
)
router.register(r"ordered-view", OrderedViewList, basename="order")
# Products API endpoints
router.register(r"category", CategoryList, basename="category")
router.register(r"inventory", ProductInventoryByWebId, basename="productinventory")
# Search API endpoint
