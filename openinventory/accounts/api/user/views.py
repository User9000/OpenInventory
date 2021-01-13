

from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import permissions, generics

from django.contrib.auth import authenticate, get_user_model




#Creating a new token manually
from rest_framework_jwt.settings import api_settings




from .serializers import UserDetailSerializer



User = get_user_model()



class UserDetailApiView(generics.RetrieveAPIView):
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

