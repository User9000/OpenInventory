from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token #accounts app

from .views import AuthView, RegisterView
urlpatterns = [

    re_path(r'^$',AuthView.as_view()),
    re_path(r'^register/$',RegisterView.as_view()),
    re_path(r'^jwt/$',obtain_jwt_token),
    
    re_path(r'^jwt/refresh/$', refresh_jwt_token),
    


]

#
