import uuid
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


LABEL_CHOICES = (
    ('P','primary'),
    ('S','secondary'),
    ('D','danger'),
)


class Category(MPTTModel):
    title = models.CharField(max_length=255)
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    parent = TreeForeignKey(
        'self', blank=True,
        null=True,
        related_name='childern',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural ='Categories'

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title



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
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, null=True)
    image = models.ImageField(upload_to='items')
    discription = models.TextField(blank=True, null=True)


    class Meta:
        indexes = [
            models.Index(fields=['id'], name='id_index'),
        ]
        permissions = [ 
            ('special_status', 'Can read all books'),
        ]     
        verbose_name_plural = 'items'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse('book_detail', args=[str(self.id)])
    
    def get_add_to_cart_url(self):
        return reverse('add-to-cart', args=[str(self.id)])

    def get_remove_from_cart_url(self):
        return reverse('remove-from-cart', args=[str(self.id)])
        


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
