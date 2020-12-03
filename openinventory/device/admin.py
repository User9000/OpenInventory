from django.contrib import admin

# Register your models here.

from .forms import DeviceForm
from .models import Device as DeviceModel

admin.site.register(DeviceModel)


class DeviceAdmin(admin.ModelAdmin):
    list_display = ['hostname', '__str__', 'content']
    form = DeviceForm