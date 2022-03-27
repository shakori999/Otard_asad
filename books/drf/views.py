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
    """
    API endpoint that returns all products
    """

    queryset = Product.objects.all()
    serializer_class = AllProducts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        queryset = Product.objects.filter(category__slug=slug)[:10]
        serializer = AllProducts(queryset, many=True)
        return Response(serializer.data)


class ProductByCategory(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    """
    API endpoint that returns products by category
    """

    queryset = ProductInventory.objects.all()

    def list(self, request, slug=None):
        queryset = ProductInventory.objects.filter(
            product__category__slug=slug,
        ).filter(is_default=True)[:10]
        serializer = ProductInventorySerializer(
            queryset, context={"request": request}, many=True
        )
        return Response(serializer.data)
