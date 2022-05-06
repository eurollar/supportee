from rest_framework import permissions


class IsSupportOrAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        return bool(1 == request.user)
        # return False
