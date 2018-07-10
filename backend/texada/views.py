from texada import serializers
from texada.models import Product
from texada.filters import ProductFilter
from rest_framework import generics
from rest_framework.permissions import AllowAny

# Create your views here.

class ListCreateProduct(generics.ListCreateAPIView):

    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    filter_class = ProductFilter
    serializer_class = serializers.ProductSerializer


class UpdateProduct(generics.UpdateAPIView):

    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer

class DestroyProduct(generics.DestroyAPIView):

    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer

    