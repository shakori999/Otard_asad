from django.urls import path
from .views import *

urlpatterns = [
    path('', CheckoutPageView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    # path('synic', sync_products_view, name='payment'),
    # path('create-checkout-session', StripeCheckoutView.create_checkout_session, ),
]