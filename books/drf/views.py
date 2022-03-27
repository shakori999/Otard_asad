from rest_framework import viewsets, permissions, mixins
from inventory.models import *
from drf.serializer import *
from rest_framework.response import Response

# Create your views here.
class AllProductsViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):

    queryset = Product.objects.all()
    serializer_class = AllProducts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        queryset = Product.objects.filter(category__slug=slug)[:10]
        serializer = AllProducts(queryset, many=True)
        return Response(serializer.data)


class ProductInventoryViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer
