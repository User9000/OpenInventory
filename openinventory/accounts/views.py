from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your tests here.


class AuthView(APIView):

    def post(self, request, *args, **kwargs):
        return Response({'token': 'abc'})