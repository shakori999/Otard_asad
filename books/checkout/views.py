from django.http.response import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from .forms import CheckoutForm
from django.contrib import messages
from django.conf import settings
from .models import *
from order.models import * 
import stripe

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

products = stripe.Product.list()
prices = stripe.Price.list()
class CheckoutPageView(View):
    
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        user = get_user_model()
        context = {
            'form': form,
            'user': user
        }
        return render(self.request, 'checkout/checkout-page.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        order = Order.objects.get(user=self.request.user, ordered=False)
        try:
            if form.is_valid():
                name = form.cleaned_data.get('name')
                phone = form.cleaned_data.get('number')
                address = form.cleaned_data.get('street_address')
                address_2 = form.cleaned_data.get('apartment_address')
                state = form.cleaned_data.get('state')
                # TODO: add functinoality for these fields
                # same_shipping_address = form.cleaned_data.get(
                #     'same_shipping_address')
                # save_info =  form.cleaned_data.get('save_info')
                # payment_option = form.cleaned_data.get('payment_option')

                order_items = order.items.all()
                order_items.update(ordered=True)
                for item in order_items:
                    item.save()
                order.ordered = True
                order.save()

                print(state)
                invoice = Invoice.objects.create(
                    user = self.request.user,
                    name = name,
                    phone_number = phone,
                    address = address,
                    address_2 = address_2,
                    state = state,
                )
                invoice.save()
                # TODO: add redirect to the selected payment option
                return redirect('checkout')
            messages.warning(self.request, 'Faild checkout')
            return redirect('checkout')
        except ObjectDoesNotExist:
            messages.warning(self.request, "you do not have an active order")
            return redirect('order_summary')


class PaymentView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'payments/payment.html')

# def sync_products_view(request):
#     print(products.data)
#     print(prices.data)
#     return HttpResponse('data')

class StripeCheckoutView(View):
    def post(self, request):
        YOUR_DOMAIN = 'http://localhost:4242'
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': '{{PRICE_ID}}',
                        'quantity': 1,
                    },
                ],
                payment_method_types=['card',],
                mode='payment',
                success_url=YOUR_DOMAIN + '/success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url=YOUR_DOMAIN + '?canceled=true',
            )
            return redirect(checkout_session.url)
        except Exception as e:
            return str(e)
    
    @csrf_exempt
    def create_checkout_session(request):
        if request.method == 'GET':
            domain_url = 'http://localhost:8000/'
            stripe.api_key = settings.STRIPE_SECRET_KEY
            try:
                # Create new Checkout Session for the order
                # Other optional params include:
                # [billing_address_collection] - to display billing address details on the page
                # [customer] - if you have an existing Stripe Customer ID
                # [payment_intent_data] - capture the payment later
                # [customer_email] - prefill the email input in the form
                # For full details see https://stripe.com/docs/api/checkout/sessions/create

                # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
                checkout_session = stripe.checkout.Session.create(
                    success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                    cancel_url=domain_url + 'cancelled/',
                    payment_method_types=['card'],
                    mode='payment',
                    line_items=[
                        {
                            'name': 'T-shirt',
                            'quantity': 1,
                            'currency': 'usd',
                            'amount': '2000',
                        }
                    ]
                )
                # return JsonResponse({'sessionId': checkout_session['id']})
                return redirect(checkout_session.url)
            except Exception as e:
                # return str(e)
                return JsonResponse({'error': str(e)})