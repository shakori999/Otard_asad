from django.urls import path
from .views import *

urlpatterns = [
    path('', CheckoutPageView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
]