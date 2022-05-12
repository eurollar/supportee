from rest_framework import permissions

from tickets.models import Ticket


class IsSupportOrAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        queryset = Ticket.objects.get(pk=view.kwargs['pk'])
        ticket_author = queryset.author.username
        return bool(request.user.type == 'support' or request.user.username == ticket_author)
