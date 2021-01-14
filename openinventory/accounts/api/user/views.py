

from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import permissions, generics, pagination

from django.contrib.auth import authenticate, get_user_model




#Creating a new token manually
from rest_framework_jwt.settings import api_settings




from .serializers import UserDetailSerializer

from status.api.serializers import StatusInlineSerializer
from status.models import Status
User = get_user_model()



class UserDetailApiView(generics.RetrieveAPIView):
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field = 'username'


class UserStatusPagination(pagination.PageNumberPagination):
    page_size= 4

    




class UserStatusApiView(generics.ListAPIView):
    #permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
   
    serializer_class = StatusInlineSerializer
    pagination_class= UserStatusPagination
    

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get("username", None)

        if username is None:
            return Status.objects.none()
        return  Status.objects.filter(user__username=username)

