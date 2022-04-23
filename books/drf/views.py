from django.shortcuts import get_object_or_404

from drf.serializer import *
from accounts.serializer import UserSerializer
from order.models import *
from inventory.models import *
from accounts.models import CustomUser

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.


class Category(viewsets.ModelViewSet):
    """
    Return list of all categories
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, pk=None):
        product_web = Product.objects.filter(category_id=pk)
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
        product_web = ProductInventory.objects.filter(product__id=pk)
        serializer = ProductInventorySerializer(product_web, many=True)
        return Response(serializer.data)


class OrderedView(viewsets.ModelViewSet):
    """
    Return a list of orders for this user
    """

    queryset = Order.objects.filter(ordered=True)
    serializer_class = OrderedViewSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderedDetailSerializer(order)
        return Response(serializer.data)


class User(viewsets.ModelViewSet):
    """
    Return list of all categories
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == "list":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, pk=None):
        product_web = CustomUser.objects.get(id=pk)
        serializer = UserSerializer(product_web, context={"request": request})
        return Response(serializer.data)
