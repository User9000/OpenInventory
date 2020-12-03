from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel
from .mixins import CSRFExamptMixin
from openinventory.mixins import HttpResponseMixin
import json
from updates.forms import UpdateModelForm
from .utils import is_json


class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExamptMixin, View):
    is_json = True

    def get_object(self, id=None):
        # try:
        #     obj = UpdateModel.objects.get(id=id)
        # except UpdateModel.DoesNotExists:
        #     obj = None
        # retun obj
        """
                Below handles a does not exist exception Too.
        
        """
        qs = UpdateModel.objects.filter(id=id)
        if qs.count() == 1:
            return qs.first()

        return None

    def get(self, request, id, *args, **kwargs):
        #obj = UpdateModel.objects.get(id=id)
        obj = self.get_object(id=id)

        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)

        json_data = obj.serialize()
        #json_data = obj.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        json_data = json.dumps(
            {"message": "Not allowed, please use the /api/updates endpoint"})
        return self.render_to_response(json_data, status=403)

    def put(self, request, id, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message": "Not JSON data"})
            return self.render_to_response(error_data, status=404)
        #new_data = json.loads(request.body)
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)

        #new_data = {}
        data = json.loads(obj.serialize())
        #retrieves data
        #saved_data = json.loads(obj.serialize())
        passed_data = json.loads(request.body)
        for key, value in passed_data.items():
            #This will only update the data passed
            data[key] = value

        #print(passed_data)

        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            #Saving post data
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)

        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)

        json_data = json.dumps({"message": "something"})

        return self.render_to_response(json_data)

    def delete(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "object not found"})
            return self.render_to_response(error_data, status=404)
        deleted_, item_deleted = obj.delete()
        if deleted_ == 1:
            print(deleted_)
            json_data = json.dumps({"message": "sunccessfully deleted"})
            return self.render_to_response(json_data, status=200)
        error_data = json.dumps(
            {"message": "Could not delete item. Please try again"})
        return self.render_to_response(error_data, status=403)


#AUTH/ Permissions - DJANGO REST FRAMEWORK


# OBJECTS
class UpdateModelListAPIView(HttpResponseMixin, CSRFExamptMixin, View):

    is_json = True
    queryset = None

    def get_queryset(self):
        qs = UpdateModel.objects.all()
        self.queryset = qs
        return qs

    def get_object(self, id=None):
        # try:
        #     obj = UpdateModel.objects.get(id=id)
        # except UpdateModel.DoesNotExists:
        #     obj = None
        # retun obj
        """
                Below handles a does not exist exception Too.
        
        """
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()

        return None

    def get(self, request, *args, **kwargs):
        data = json.loads(request.body)
        passed_id = data.get("id", None)
        if passed_id is not None:
            obj = self.get_object(id=passed_id)
            if obj is None:
                error_data = json.dumps({"obj": "object not found"})
                return self.render_to_response(error_data, status=403)
            json_data = obj.serialize()
            return self.render_to_response(json_data)
        else:
            qs = UpdateModel.objects.all()
            json_data = qs.serialize()
            return self.render_to_response(json_data)
        #return HttpResponse(json_data, content_type='application/json')

    #POST use of form to save data
    def post(self, request, *args, **kwargs):
        #print(request.POST) # SHOWS THE POST data passed

        valid_json = is_json(request.body)

        if not valid_json:

            error_data = json.dumps({"message": "Not JSON data"})
            return self.render_to_response(error_data, status=404)

        data = json.loads(request.body)

        form = UpdateModelForm(data)
        if form.is_valid():
            #Saving post data
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)

        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)

        data = {"message not allowed"}

        return self.render_to_response(data, status=400)

        data = json.dumps({"message": "unknown data"})
        #return HttpResponse({data}, content_type='application/json')  #json
        return self.render_to_response(data, status=400)

    def delete(self, request, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message": "Not JSON data"})
            return self.render_to_response(error_data, status=404)
        #new_data = json.loads(request.body)
        #new_data = {}
        #retrieves data
        #saved_data = json.loads(obj.serialize())
        passed_data = json.loads(request.body)
        passed_id = passed_data.get('id', None)
        if not passed_id:
            error_data = json.dumps(
                {"id": "This is a required field to update an item"})
            return self.render_to_response(error_data, status=404)
        obj = self.get_object(id=passed_id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)

        deleted_, item_deleted = obj.delete()
        if deleted_ == 1:
            print(deleted_)
            json_data = json.dumps({"message": "sunccessfully deleted"})
            return self.render_to_response(json_data, status=200)
        error_data = json.dumps(
            {"message": "Could not delete item. Please try again"})
        data = json.dumps({"message": "you cannot delete an entire list."})
        #return HttpResponse({data}, content_type='application/json')  #json

        return self.render_to_response(data, status=403)

    def put(self, request, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message": "Not JSON data"})
            return self.render_to_response(error_data, status=404)
        #new_data = json.loads(request.body)
        #new_data = {}
        #retrieves data
        #saved_data = json.loads(obj.serialize())
        passed_data = json.loads(request.body)
        passed_id = passed_data.get('id', None)
        if not passed_id:
            error_data = json.dumps(
                {"id": "This is a required field to update an item"})
            return self.render_to_response(error_data, status=404)

        obj = self.get_object(id=passed_id)
        if obj is None:
            error_data = json.dumps({"obj": "obj not found"})
            return self.render_to_response(error_data, status=404)

        data = json.loads(obj.serialize())

        for key, value in passed_data.items():
            #This will only update the data passed
            data[key] = value

        #print(passed_data)

        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            #Saving post data
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)

        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)

        json_data = json.dumps({"message": "something"})

        return self.render_to_response(json_data)