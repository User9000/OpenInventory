from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from status.models import Status
from .serializers import StatusSerializer
from django.shortcuts import get_object_or_404
#authentication rest package related
from rest_framework.authentication import SessionAuthentication
#error class
import json
#return boolean
def is_json(json_data):
    try:
        is_valid = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid

class StatusDetailAPIView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView):

    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'    

    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def perform_update(self, serializer):
    #     serializer.save(updated_by_user = self.request.user)


    # def perform_destroy(self, instance):
    #     if instance is not None:
    #         return instance.delete()
    #     return None

class StatusAPIView(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,                   
                    generics.ListAPIView):  #Create and List [using mixin]

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #authentication_classes = [SessionAuthentication]
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        #print(request.user)

        qs = Status.objects.all()
        query = request.GET.get('q')

        if query is not None:
            qs = qs.filter(content__icontains=query)

        return qs
    
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



    # def get_object(self):
    #     request = self.request
    #     passed_id = request.GET.get('id', None) or self.passed_id

    #     obj = None

    #     queryset = self.get_queryset()

    #     if passed_id is not None:
    #         obj = get_object_or_404(queryset, id=passed_id)
    #         self.check_object_permissions(request, obj)

    #     return obj

    # def perform_destroy(self, instance):
    #     if instance is not None:
    #         return instance.delete()
    #     return None

    # def get(self, request, *args, **kwargs):

    #     #data = json.loads(request.body)
    #     url_passed_id = request.GET.get('id', None)
    #     json_data = {}
    #     body_ = request.body
    #     if is_json(body_):
    #         json_data = json.loads(request.body)

    #     new_passed_id = json_data.get('id', None)
    #     passed_id = url_passed_id or new_passed_id or None
    #     self.passed_id = passed_id
    #     if passed_id is not None:
    #         return self.retrieve(
    #             request, *args,
    #             **kwargs)  # this will call the the get_object function

    #     return super().get(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):

    #     url_passed_id = request.GET.get('id', None)
    #     json_data = {}
    #     body_ = request.body
    #     if is_json(body_):
    #         json_data = json.loads(request.body)

    #     new_passed_id = json_data.get('id', None)
    #     passed_id = url_passed_id or new_passed_id or None
    #     self.passed_id = passed_id

    #     return self.create(request, *args, **kwargs)

#CreateModelMixin -- POST method
#UpdateModelMixin -- PUT method
#DestroyModelMixin --- Delete method
#Class that handles everything CRUDL
# class StatusAPIView(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin, mixins.DestroyModelMixin,
#                     generics.ListAPIView):  #Create and List [using mixin]

#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     passed_id = None

#     def get_queryset(self):
#         request = self.request
#         qs = Status.objects.all()
#         query = request.GET.get('q')

#         if query is not None:
#             qs = qs.filter(content__icontains=query)

#         return qs

#     def get_object(self):
#         request = self.request
#         passed_id = request.GET.get('id', None) or self.passed_id

#         obj = None

#         queryset = self.get_queryset()

#         if passed_id is not None:
#             obj = get_object_or_404(queryset, id=passed_id)
#             self.check_object_permissions(request, obj)

#         return obj

#     def perform_destroy(self, instance):
#         if instance is not None:
#             return instance.delete()
#         return None

#     def get(self, request, *args, **kwargs):

#         #data = json.loads(request.body)
#         url_passed_id = request.GET.get('id', None)
#         json_data = {}
#         body_ = request.body
#         if is_json(body_):
#             json_data = json.loads(request.body)

#         new_passed_id = json_data.get('id', None)
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         if passed_id is not None:
#             return self.retrieve(
#                 request, *args,
#                 **kwargs)  # this will call the the get_object function

#         return super().get(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         url_passed_id = request.GET.get('id', None)
#         json_data = {}
#         body_ = request.body
#         if is_json(body_):
#             json_data = json.loads(request.body)

#         new_passed_id = json_data.get('id', None)
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id

#         return self.create(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):  # create / update
#         url_passed_id = request.GET.get('id', None)
#         json_data = {}
#         body_ = request.body
#         if is_json(body_):
#             json_data = json.loads(request.body)

#         new_passed_id = json_data.get('id', None)
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id

#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         url_passed_id = request.GET.get('id', None)
#         json_data = {}
#         body_ = request.body
#         if is_json(body_):
#             json_data = json.loads(request.body)

#         new_passed_id = json_data.get('id', None)
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id

#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         url_passed_id = request.GET.get('id', None)
#         json_data = {}
#         body_ = request.body
#         if is_json(body_):
#             json_data = json.loads(request.body)

#         new_passed_id = json_data.get('id', None)
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id

#         return self.destroy(request, *args, **kwargs)


class StatusListSearchAPIView(APIView):

    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)

        return Response(serializer.data)


#CreateModelMixin --- post data
#UpdateModelMixin --- put data


class StatusAPIView2(mixins.CreateModelMixin,
                     generics.ListAPIView):  #Create and List [using mixin]

    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)

        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StatusAPIView2(generics.ListAPIView):

    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)

        return qs


class StatusCreateAPIView(generics.CreateAPIView):

    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class StatusDetailAPIView2(mixins.DestroyModelMixin, mixins.UpdateModelMixin,
                           generics.RetrieveAPIView):

    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    lookup_field = 'id'  # for update view, change from PK to ID

    def put(self, request, *args, **kwargs):
        #qs = Status.objects.all()
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        #qs = Status.objects.all()
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        #qs = Status.objects.all()
        return self.update(request, *args, **kwargs)

    #override lookup field function method
    # def get_object(self, *args, **kwargs):
    #     kwargs = self.kwargs
    #     kw_id = kwargs.get('id')

    #     return Status.objects.get(id=kw_id)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class StatusUpdateAPIView(generics.UpdateAPIView):

    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusDeleteAPIView(generics.DestroyAPIView):

    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer





#MAIN METHOD to do Everything
