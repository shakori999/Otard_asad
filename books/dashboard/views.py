from itertools import product
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from inventory.models import *

# Create your views here.


class HomePageView(ListView):
    def get(self, *args, **kwargs):
        category = Category.objects.all
        item = ProductInventory.objects.all()
        context = {"category": category, "items": item}
        return render(self.request, "home-page.html", context)
