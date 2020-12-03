from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response

from device.models import Device
from .serializers import DeviceSerializer

from django.shortcuts import get_object_or_404

import json


#return boolean
def is_json(json_data):
    try:

        is_valid = json.loads(json_data)
        is_valid = True

    except ValueError:
        is_valid = False

    return is_valid


class DeviceAPIView(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                    generics.ListAPIView):  #Create and List [using mixin]

    permission_classes = []
    authentication_classes = []
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = Device.objects.all()
        query = request.GET.get('q')

        if query is not None:
            qs = qs.filter(content__icontains=query)

        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None) or self.passed_id

        obj = None

        queryset = self.get_queryset()

        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)

        return obj

    def perform_destroy(self, instance):
        if instance is not None:
            return instance.delete()
        return None

    def get(self, request, *args, **kwargs):

        #data = json.loads(request.body)
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)

        new_passed_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        if passed_id is not None:
            return self.retrieve(
                request, *args,
                **kwargs)  # this will call the the get_object function

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)

        new_passed_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id

        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):  # create / update
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)

        new_passed_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id

        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)

        new_passed_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id

        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)

        new_passed_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id

        return self.destroy(request, *args, **kwargs)
