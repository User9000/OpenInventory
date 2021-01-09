
import datetime
from django.conf import settings
from django.utils import timezone

expires_delta = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']

#RESPONSE BACK TO USER (PAYLOAD)
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.username,
        'expires':  timezone.now() + expires_delta - datetime.timedelta(seconds=1200), # approximate time

    }

