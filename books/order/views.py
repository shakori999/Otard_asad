from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render, get_object_or_404
from books.models import Book
from django.utils import timezone
from .models import *

# Create your views here.
def add_to_cart(request, pk):
    item = get_object_or_404(Book, id=pk)
    order_item, created= OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
        )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect("book_detail", pk=pk)
