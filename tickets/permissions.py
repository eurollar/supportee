from rest_framework import permissions


class IsClientOrReadOnly(permissions.BasePermission):
    """
    Get permission to create a new ticket for the user.
    Support can only read
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.type == 'user'


class IsSupportOrReadOnly(permissions.BasePermission):
    """
    Get permission to change a status of the ticket for support.
    The user can only read
    """
    def has_object_permission(self, request, view, obj):
        support = request.user.type == 'support'

        if request.method in permissions.SAFE_METHODS:
            return obj.author == request.user or support

        return support
