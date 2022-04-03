from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from inventory.models import *


class BookListView(ListView):
    def get(self, *args, **kwargs):
        category = Category.objects.all
        # book = Book.objects.all()
        context = {
            "category": category,
            # 'items_list': book
        }
        return render(self.request, "books/Book_list.html", context)


class BookDetailView(DetailView):
    # model = Book
    context_object_name = "book"
    template_name = "books/product-page.html"
    login_url = "account_login"


class SeachResultsListView(ListView):
    # model = Book
    context_object_name = "items_list"
    template_name = "books/book_list_compy.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        # return Book.objects.filter(
        #     Q(title__icontains=query) | Q(author__icontains=query)
        # )
