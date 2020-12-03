from django.contrib import admin

# Register your models here.

from .models import Update as UpdateModel
#from .models import Status as StatusModel
admin.site.register(UpdateModel)

#admin.site.register(StatusModel)