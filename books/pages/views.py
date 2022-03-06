from django.shortcuts import render
from django.views.generic import ListView,TemplateView

from books.models import *

# Create your views here.

class HomePageView(
        ListView):
    model = Book
    context_object_name = 'items'
    template_name = 'home-page.html'
    login_url = 'account_login'
