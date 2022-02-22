from django.urls import path
from .views import *

urlpatterns = [
    path('add-to-cart/<uuid:pk>/', add_to_cart, name='add-to-cart'),
]