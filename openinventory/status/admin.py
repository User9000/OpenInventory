from django.contrib import admin

# Register your models here.
from .models import Status as StatusModel
#admin.site.register(UpdateModel)

from .forms import StatusForm


class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', '__str__', 'image']
    form = StatusForm


admin.site.register(StatusModel)