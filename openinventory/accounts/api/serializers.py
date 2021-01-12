from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.conf import settings
import datetime
from django.utils import timezone

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

expires_delta = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']

User = get_user_model()

class UserPublicSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields =[

            'id',
            'username',
            'url'
        ]
    def get_url(self,obj):
        return "/api/users/{id}".format(id=obj.id)


class UserRegisterSerializer(serializers.ModelSerializer):
    #password = serializers.CharField(style={'input_type': 'password'}, write_only=True )
    password2 = serializers.CharField(style={'input_type': 'password2'}, write_only=True )
    token = serializers.SerializerMethodField(read_only=True)
    expires = serializers.SerializerMethodField(read_only=True)
    #token_response = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model=User 
        fields= [

            'username', 
            'email',
            'password',
            'password2',
            'token',
            'expires',
            #'token_response',
        ]
        extra_kwargs = { 
            'password': {'write_only':True}
        }

    
    # def get_token_response (self,obj):
    #     user =obj
    #     payload = jwt_payload_handler(user)
    #     token = jwt_encode_handler(payload)
    #     response = jwt_response_payload_handler(token, user, request=None)
    #     return response 



    def get_expires (self,obj):
        return   timezone.now() + expires_delta - datetime.timedelta(seconds=1200)

    def validate_email(self,value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("User with this email already exists")
        
        return value

    def validate_username(self,value):
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("User with this username already exists")
        
        return value

    def get_token(self,obj): # instance of model
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def validate(self, data):
        pw = data.get('password')
        pw2 = data.pop('password2')
        if pw != pw2:
            raise serializers.ValidationError("Passwords must match")
        return data
    
    def create(self, validated_data):
        print(validated_data)
        user_obj = User.objects.create(username=validated_data['username'], email=validated_data['email'])
        user_obj.set_password(validated_data.get('password'))

        user_obj.is_active = False
        user_obj.save()

        return user_obj
