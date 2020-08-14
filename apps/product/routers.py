# apps/geolocation/routers.py
# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import ProductViewSet


# Create your routers here.
product = (
    (r'products', ProductViewSet),
)
