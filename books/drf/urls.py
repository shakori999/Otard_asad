from rest_framework import routers
from django.urls import path, include
from .views import *
from search.views import SearchProductInventory


router = routers.DefaultRouter()
# Orders API endpoints
router.register(r"ordered-view", OrderedView, basename="order")
# Products API endpoints
router.register(r"category", Category, basename="category")
router.register(r"inventory", ProductInventoryByWebId, basename="productinventory")
# User API endpoint
router.register(r"user", User, basename="customuser")

urlpatterns = [
    path("", include(router.urls)),
]
