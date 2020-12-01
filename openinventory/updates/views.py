
import json

from .models import Update

from django.core.serializers import serialize
from django.shortcuts import render


from django.http import JsonResponse , HttpResponse
# Create your views here.

from django.views.generic import View


#Mixins
from openinventory.mixins import JsonResponseMixin


def update_model_detail_view(request):

    data = {

        "count": 1000,
        "content":  "Some content"
    }
    return JsonResponse(data) #return JSON data  

class JsonCBV(View):
    def get(self,request, *args, **kwargs):
        data = {

            "count": 1000,
            "content":  "Some content"
        }        
       
        return JsonResponse(data) #return JSON data  
         


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):

        data = {

            "count": 1000,
            "content":  "Some content"
        }
        return self.render_to_json_response(data)

class SerializedView(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id = 2)
        data = {

            "user": obj.user.username,
            "content":  obj.content
        }

        json_data = json.dumps(data)
        return self.render_to_json_response(data)

class SerializedDetailView(View):
      def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id = 2)
        #data = serialize("json", [obj,], fields=('user', 'content'))       
        json_data = obj.serialize()
        return HttpResponse(json_data,content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        #qs = Update.objects.all()
        #data = serialize("json", qs, fields=('user', 'content'))
        json_data = Update.objects.all().serialize()
        #print(data) 
       
        return HttpResponse(json_data,content_type='application/json')