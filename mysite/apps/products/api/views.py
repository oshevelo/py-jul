from django.shortcuts import render,  get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from apps.products.models import Product
from rest_framework import generics
from .serializers import ProductSerializer


class ProductsList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_object(self):
        return get_object_or_404(Product, pk=self.kwargs.get('product_pk'))
