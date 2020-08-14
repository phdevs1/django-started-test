# apps/core/viewsets.py
# Python imports

# Django imports
from django.shortcuts import render
# Third party apps imports
from rest_framework import viewsets

# Local imports
from .serializers import ProductSerializer
from .models import Product


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ["get", "post"]