from rest_framework.permissions import SAFE_METHODS, BasePermission
# SAFE_METHODS are request methods that do not change the database eg. POST and GET methods

class IsAdminOrReadOnly(BasePermission):
    # only allow users with admin privileges to perform certain requests
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff