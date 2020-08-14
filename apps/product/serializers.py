# apps/core/serializers.py
# Python imports

# Django imports
from django.contrib.auth.models import User
# Third party apps imports
from rest_framework import serializers

# Local imports
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
