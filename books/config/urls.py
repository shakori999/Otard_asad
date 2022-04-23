from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf.views import *
from search.views import SearchProductInventory
from drf.urls import *


urlpatterns = [
    # Djago admin
    path("bingo/", admin.site.urls),
    # User management
    # path("accounts/", include("allauth.urls")),
    # Local apps
    # path("", include("dashboard.urls")),
    # path("books/", include("books.urls")),
    # path("order/", include("order.urls")),
    # path("checkout/", include("checkout.urls")),
    # API endponts
    path("", include("drf.urls")),
    path("api-auth", include("rest_framework.urls")),
    path("search/<str:query>", SearchProductInventory.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__", include(debug_toolbar.urls)),
    ] + urlpatterns
