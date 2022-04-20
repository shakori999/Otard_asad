from django.shortcuts import get_object_or_404

from drf.serializer import *
from order.models import *
from inventory.models import *

from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import viewsets, permissions, mixins, generics
from rest_framework import status

# Create your views here.


class CategoryList(viewsets.ModelViewSet):
    """
    Return list of all categories
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, pk=None):
        product_web = Product.objects.filter(category__slug=pk)
        serializer = ProductSerializer(product_web, many=True)
        return Response(serializer.data)


class ProductInventoryByWebId(viewsets.ModelViewSet):
    """
    Return Sub Product by WebId
    """

    queryset = ProductInventory.objects.all()

    def get_serializer_class(self):
        if self.request.method in ("GET",):
            return ProductInventoryReadSerializer
        return ProductInventorySerializer

    def retrieve(self, request, pk=None):
        queryset = ProductInventory.objects.all()
        product_web = get_object_or_404(queryset, product__web_id=pk)
        serializer = ProductInventorySerializer(product_web)
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

    def get_serializer_class(self):
        if self.request.method in ("GET",):
            return OrderSummaryReadSerializer
        return OrderSummarySerializer

    # def update(self, request, *args, **kwargs):
    #     user = self.request.user

    #     return super().update(request, *args, **kwargs)
