from rest_framework import permissions

class BlocklistPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blocked = Blocklist.objects.filter(ip_addr=ip_addr).exists() # TRUE/FALSE
        return not blocked

        
class AnonPermissionOnly(permissions.BasePermission):
    """
    Non-authenticated users only
    """
    
    def has_permission(self, request, view):
        return not request.user.is_authenticated


from rest_framework import exceptions
CANDIDATE_ALREADY_ANSWERED = "NOT OWNER"
class cIsOwnerOrReadOnly(permissions.BasePermission):
    message = '2030329'

    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        #if not request.method in permissions.SAFE_METHODS:
        #    raise exceptions.PermissionDenied(detail=CANDIDATE_ALREADY_ANSWERED) 
        
        if  request.method in permissions.SAFE_METHODS:
            return True
        

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user
        #return True