import uuid
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('SH','Self-help'),
    ('N','Novel'),
    ('F','Fiction'),
)

LABEL_CHOICES = (
    ('P','primary'),
    ('S','secondary'),
    ('D','danger'),
)

class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, null=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['id'], name='id_index'),
        ]
        permissions = [ 
            ('special_status', 'Can read all books'),
        ]     

    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse('book_detail', args=[str(self.id)])
    
    def get_add_to_cart_url(self):
        return reverse('add-to-cart', args=[str(self.id)])
        

class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review