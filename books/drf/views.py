from rest_framework import viewsets, permissions, mixins
from rest_framework.views import APIView
from inventory.models import *
from drf.serializer import *
from rest_framework.response import Response

# Create your views here.


class CategoryList(APIView):
    """
    Return list of all categories
    """

    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class ProductByCategory(APIView):
    """
    API endpoint that returns products by category
    """

    def get(self, request, query=None):
        queryset = Product.objects.filter(
            category__slug=query,
        )
        serializer = ProductSerializer(
            queryset,
            many=True,
        )
        return Response(serializer.data)


class ProductInventoryByWebId(APIView):
    """
    Return Sub Product by WebId
    """

    def get(self, request, query=None):
        queryset = ProductInventory.objects.filter(product__web_id=query)
        serializer = ProductInventorySerializer(queryset, many=True)
        return Response(serializer.data)