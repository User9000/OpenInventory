from rest_framework import  pagination
#Custom class for pagination
class UserStatusPagination(pagination.PageNumberPagination):
    page_size= 5

    