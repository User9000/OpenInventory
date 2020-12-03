from rest_framework import serializers
from device.models import Device
'''
Serializers - > JSON
Serializers - > validate data

'''


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['content', 'hostname', 'ipaddress', 'status']

    # def validate_content(self, value):
    #     if len(value) > 10000:
    #         raise serializers.ValidationError("This is way too long")
    #     return value

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None

        if content is None:
            raise serializers.ValidationError("Content is required ")

        return data