import django_filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from tickets.models import Ticket
from tickets.permissions import IsClientOrReadOnly, IsSupportOrReadOnly
from tickets.serializers import UserTicketList, UserTicketDetail, SupportTicketDetail, SupportTicketList


class TicketList(generics.ListCreateAPIView):
    def get_queryset(self):
        if self.request.user.type == 'support':
            return Ticket.objects.all().select_related('author')
        else:
            return Ticket.objects.filter(author_id=self.request.user.id)

    def get_serializer_class(self):
        if self.request.user.type == 'support':
            return SupportTicketList
        return UserTicketList

    permission_classes = (IsAuthenticated, IsClientOrReadOnly)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['status']


class TicketDetail(generics.RetrieveUpdateAPIView):

    def get_queryset(self):
        return Ticket.objects.filter(pk=self.kwargs['pk']).select_related('author').prefetch_related('comments__author')

    def get_serializer_class(self):
        if self.request.user.type == 'support':
            return SupportTicketDetail
        return UserTicketDetail

    # queryset = Ticket.objects.all().select_related('author')
    permission_classes = (IsAuthenticated, IsSupportOrReadOnly)
