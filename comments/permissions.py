from rest_framework import permissions


class IsSupportOrAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.type == 'support')

    def has_object_permission(self, request, view, obj):
        return bool(obj.author == request.user or request.user.type == 'support')
