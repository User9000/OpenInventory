from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token #accounts app

from .views import AuthView, RegisterView, UserDetailApiView

app_name ='user-api'
urlpatterns = [

    re_path(r'^(?P<username>\w+)/$',UserDetailApiView.as_view(), name='detail'),



]

#
