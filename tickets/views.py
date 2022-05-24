import django_filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from tickets.models import Ticket
from tickets.permissions import IsClientOrReadOnly, IsSupportOrReadOnly
from tickets.serializers import (SupportTicketDetail, SupportTicketList,
                                 UserTicketDetail, UserTicketList)
from tickets.tasks import send_email as send_email_task


class TicketList(generics.ListCreateAPIView):
    # Depending on a user returns data from DB
    def get_queryset(self):
        if self.request.user.type == 'support':
            return Ticket.objects.all().select_related('author')
        else:
            return Ticket.objects.filter(author_id=self.request.user.id)

    # Different serializers for users in request
    def get_serializer_class(self):
        if self.request.user.type == 'support':
            return SupportTicketList

        return UserTicketList

    permission_classes = (IsAuthenticated, IsClientOrReadOnly)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['status']


class TicketDetail(generics.RetrieveUpdateAPIView):
    # Get the ticket with comments
    def get_queryset(self):
        return Ticket.objects.filter(
            pk=self.kwargs['pk']
        ).select_related(
            'author'
        ).prefetch_related(
            'comments__author'
        )

    # Different serializers for users in request
    def get_serializer_class(self):
        if self.request.user.type == 'support':
            return SupportTicketDetail

        return UserTicketDetail

    # In this method added task to send a mail with a new status
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        current_status = instance.status  # Get current status of ticket
        self.perform_update(serializer)

        # Send a mail for user's task which is changed
        send_email_task.apply_async(
            kwargs={
                'user': instance.author.username,
                'email': instance.author.email,
                'ticket': instance.title,
                'current_status': current_status,
                'new_status': request.data['status']
            }
        )

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    permission_classes = (IsAuthenticated, IsSupportOrReadOnly)
