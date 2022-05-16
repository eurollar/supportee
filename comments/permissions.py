from rest_framework import permissions

from tickets.models import Ticket


class IsSupportOrAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        queryset = Ticket.objects.select_related('author').get(pk=view.kwargs['pk'])
        return bool(request.user.type == 'support' or request.user.username == queryset.author.username)

    # def has_object_permission(self, request, view, obj):
    #     return bool(request.user.type == 'support' or request.user.username == obj.author.username)
