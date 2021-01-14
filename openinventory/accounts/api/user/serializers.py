from django.contrib.auth import get_user_model
from rest_framework import serializers

from django.utils import timezone

import datetime

from status.api.serializers import StatusInlineSerializer

from rest_framework.reverse import reverse as api_reverse
User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    status_list = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields =[

            'id',
            'username',
            'url',
            'status_list'
        ]
    # def get_url(self,obj):
    #     return "/api/users/{id}".format(id=obj.id)

    def get_url(self,obj):
        request = self.context.get('request')
        return api_reverse("api-user:detail", kwargs={"username":obj.username}, request=request)

    def get_status_list(self,obj):
        qs =  obj.status_set.all() #Status.objects.filter(user=obj)
        return  StatusInlineSerializer(qs, many=True).data
