from django.urls import path
from rest_framework import routers

from .views import *
from search.views import SearchProductInventory

# urlpatterns = [
#     path("ordered-view/", OrderedViewList),
# path('snippets/<int:pk>/', views.snippet_detail),
# path("api/inventory/category/all/", CategoryList.as_view()),
# path("api/inventory/products/category/<str:query>/", ProductByCategory.as_view()),
# path("api/inventory/<int:query>/", ProductInventoryByWebId.as_view()),
# # API endpoints for order managment system
# # path("api/order/ordered-view/", OrderedViewList.as_view()),
# path("api/order/order-summary/", OrderSummary.as_view()),
# path("api/order/ordered-detail/<uuid:pk>", OrderSummary.as_view()),
# # ealsticsearch
# path("api/search/<str:query>/", SearchProductInventory.as_view()),
# ]

router = routers.DefaultRouter()
router.register(r"ordered-view", OrderedViewList, basename="ordered-view")
