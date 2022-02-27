from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from .forms import CheckoutForm
from django.contrib import messages
from .models import *
from order.models import * 
# Create your views here.
class CheckoutPageView(View):
    
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form': form
        }
        return render(self.request, 'checkout/checkout-page.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('apartment_address')
                country = form.cleaned_data.get('country')
                zip = form.cleaned_data.get('zip')
                # TODO: add functinoality for these fields
                # same_shipping_address = form.cleaned_data.get(
                #     'same_shipping_address')
                # save_info =  form.cleaned_data.get('save_info')
                payment_option = form.cleaned_data.get('payment_option')
                billing_address = BillingAddress(
                    user=self.request.user,
                    street_address = street_address,
                    apartment_address = apartment_address,
                    country = country,
                    zip = zip,
                )
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                # TODO: add redirect to the selected payment option
                return redirect('checkout')
            messages.warning(self.request, 'Faild checkout')
            return redirect('checkout')
        except ObjectDoesNotExist:
            messages.warning(self.request, "you do not have an active order")
            return redirect('order_summary')


class PaymentView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'Payment.html')