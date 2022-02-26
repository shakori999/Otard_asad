from urllib import request
from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import CheckoutForm
# Create your views here.

class CheckoutPageView(View):
    
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form': form
        }
        return render(self.request, 'checkout/checkout-page.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(request.POST or None)
        if form.is_valid():
            print("The form is valid")
            return redirect('checkout')