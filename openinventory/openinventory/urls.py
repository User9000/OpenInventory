"""openinventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from updates.views import update_model_detail_view, JsonCBV, JsonCBV2, SerializedView, SerializedListView, SerializedDetailView

from status.views import *

from device.views import *

#from rest_framework_jwt.views import obtain_jwt_token



urlpatterns = [
    path('admin/', admin.site.urls),
    # path(r'', update_model_detail_view),
    # path(r'json/cbv/', JsonCBV.as_view()),
    # path(r'json/cbv2/', JsonCBV2.as_view()),
    # path(r'json/ser/', SerializedView.as_view()),
    # path(r'json/ser2/', SerializedListView.as_view()),
    # path(r'json/detail/', SerializedDetailView.as_view()),
    path(r'api/updates/', include('updates.api.urls')),
    path(r'api/status/', include('status.api.urls')),
    path(r'api/device/', include('device.api.urls')),
    path(r'api/auth/', include('accounts.api.urls')),
    path(r'api/user/', include('accounts.api.user.urls', namespace='api-user')),
   # path(r'api/auth/jwt/',obtain_jwt_token),

    # path(r'api/updates/list/', include('updates.api.urls'))
]
