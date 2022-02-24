from django.contrib import messages
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render, get_object_or_404
from books.models import Book
from django.utils import timezone
from .models import *

# Create your views here.

class OrderSummaryView(
        View,
        LoginRequiredMixin,
        PermissionRequiredMixin,
        ):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'order': order
            }
            return render(self.request, 'order/order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "you do not have an active order")
            return redirect('/')


def add_to_cart(request, pk):
    item = get_object_or_404(Book, id=pk)
    order_item, created= OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
        )
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
        )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "this item was updated to your cart")
        else:
            order.items.add(order_item)
            messages.info(request, "this item was added to your cart")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user,
            ordered_date=ordered_date
            )
        order.items.add(order_item)
        messages.info(request, "this item was added to your cart")
    return redirect("book_detail", pk=pk)

def remove_from_cart(request, pk):
    item = get_object_or_404(Book, id=pk)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
        )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, "this item quantity was updated to your cart")
                return redirect("book_detail", pk=pk)
            else:
                messages.info(request, "this item was removed to your cart")
                order.items.remove(order_item)
                order_item.delete()
                return redirect("book_detail", pk=pk)
        else:
            messages.info(request, "this item was not in your cart")
            return redirect("book_detail", pk=pk)

    else:
        messages.info(request, "you don't have an active order")
        return redirect("book_detail", pk=pk)