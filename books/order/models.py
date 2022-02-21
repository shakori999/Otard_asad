from django.db import models
from django.contrib.auth import get_user_model
from books.models import *
# Create your models here.

class OrderItem(models.Model):
    item = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField() 
    ordered = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username