from rest_framework import permissions


class IsClientOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user.type == 'user')


class IsSupportOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        support = request.user.type == 'support'
        if request.method in permissions.SAFE_METHODS:
            return bool(obj.author == request.user or support)

        return bool(support)
