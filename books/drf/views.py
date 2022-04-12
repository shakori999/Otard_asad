from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, mixins, generics
from inventory.models import *
from order.models import *
from drf.serializer import *
from rest_framework.response import Response

from .pagination import CustomPagination

# Create your views here.


class CategoryList(viewsets.ModelViewSet):
    """
    Return list of all categories
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPagination

    def list(self, request):
        """ """
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Return List of items in this category
        """
        queryset = Product.objects.filter(category__slug=pk)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductInventoryByWebId(viewsets.ModelViewSet):
    """
    Return Sub Product by WebId
    """

    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer

    def retrieve(self, request, pk=None):
        """
        Return List of items in this category
        """
        queryset = ProductInventory.objects.filter(product__web_id=pk)
        serializer = ProductInventorySerializer(queryset, many=True)
        return Response(serializer.data)


class OrderedViewList(viewsets.ModelViewSet):
    """
    Return a list of orders for this user
    """

    queryset = Order.objects.all()
    serializer_class = OrderedViewSerializer

    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderedViewSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderedDetailSerializer(order)
        return Response(serializer.data)


class OrderSummary(viewsets.ModelViewSet):
    """
    Return the order for this user
    """

    queryset = Order.objects.filter(ordered=False)
    serializer_class = OrderSummarySerializer
