from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf.views import *
from search.views import SearchProductInventory


urlpatterns = [
    # Djago admin
    path("bingo/", admin.site.urls),
    # User management
    path("accounts/", include("allauth.urls")),
    # Local apps
    path("", include("dashboard.urls")),
    path("books/", include("books.urls")),
    path("order/", include("order.urls")),
    path("checkout/", include("checkout.urls")),
    # API endponts
    path("api/inventory/category/all/", CategoryList.as_view()),
    path("api/inventory/products/category/<str:query>/", ProductByCategory.as_view()),
    path("api/inventory/<int:query>/", ProductInventoryByWebId.as_view()),
    path("api/order/order-summary/", OrderView.as_view()),
    # ealsticsearch
    path("api/search/<str:query>/", SearchProductInventory.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__", include(debug_toolbar.urls)),
    ] + urlpatterns
