from rest_framework import routers
from django.urls import path, include
from .views import *
from search.views import SearchProductInventory


router = routers.DefaultRouter()
# Orders API endpoints
router.register(r"ordered-view", OrderedViewList, basename="order")
# Products API endpoints
router.register(r"category", CategoryList, basename="category")
router.register(r"inventory", ProductInventoryByWebId, basename="productinventory")
# Search API endpoint
# router.register(r"search/<str:query>", SearchProductInventory, basename="search")

urlpatterns = [
    path("", include(router.urls)),
]
