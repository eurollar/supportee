from rest_framework import permissions

from tickets.models import Ticket


class IsSupportOrAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        """
        Get permission to add a new comment for the ticket if the user is an author or a support.
        This permission checks if support in request or ticket's author is the same as the user in request
        """
        queryset = Ticket.objects.select_related('author').get(pk=view.kwargs['pk'])
        return bool(request.user.type == 'support' or request.user.username == queryset.author.username)
