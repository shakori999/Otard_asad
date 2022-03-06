from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView,TemplateView

from books.models import *

# Create your views here.

class HomePageView(ListView):

    def get(self, *args, **kwargs):
        category = Category.objects.all
        book = Book.objects.all()
        context = {
            'category': category,
            'items': book
        }
        return render(self.request, 'home-page.html', context)
