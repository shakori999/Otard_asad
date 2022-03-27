from rest_framework import viewsets, permissions
from inventory.models import Product
from drf.serializer import AllProducts

# Create your views here.
class AllProductsViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()[:10]
    serializer_class = AllProducts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
