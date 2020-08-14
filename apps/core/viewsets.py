# apps/core/viewsets.py
# Python imports

# Django imports
from django.contrib.auth.models import User
# Third party apps imports
from rest_framework import viewsets

# Local imports
from .serializers import UserSerializer

# Create your viewsets here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["get", "post"]
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

  

