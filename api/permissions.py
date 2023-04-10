from rest_framework.permissions import SAFE_METHODS, BasePermission


class ProductPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == "DELETE":
            return request.user.is_staff()
        else:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_staff:
            return True
        elif request.user == obj.user:
            return True
        else:
            return False
