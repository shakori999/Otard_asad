from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from drf.views import *
from drf.urls import *
from accounts.views import *

from search.views import SearchProductInventory


urlpatterns = [
    # Djago admin
    path("bingo/", admin.site.urls),
    # User management
    # path("accounts/", include("allauth.urls")),
    path("api/token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
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
