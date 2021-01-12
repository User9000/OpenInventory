from rest_framework import serializers
from status.models import Status
'''
    Serializers - > JSON
    Serializers - > validate data
'''
from accounts.api.serializers import UserPublicSerializer



class StatusSerializer(serializers.ModelSerializer):

    user = UserPublicSerializer(read_only=True)
    class Meta:
        model = Status
        fields = ['id', 'user', 'content', 'image']
        read_only_fields = ['user'] # GET read

    # def validate_content(self, value):
    #     if len(value) > 10000:
    #         raise serializers.ValidationError("This is way too long")
    #     return value

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required ")
        return data

