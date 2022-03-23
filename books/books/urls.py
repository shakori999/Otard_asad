from django.urls import path
from .views import *

urlpatterns = [
    path("", BookListView.as_view(), name="books_list"),
    # path("<uuid:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("search/", SeachResultsListView.as_view(), name="search_results"),
]
