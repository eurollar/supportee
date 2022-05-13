from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from comments.models import Comment
from comments.permissions import IsSupportOrAuthor
from comments.serializers import CommentSerializer
from tickets.models import Ticket


class CommentsList(generics.ListCreateAPIView):
    def get_queryset(self):
        return Comment.objects.filter(ticket_id=self.kwargs['pk']).select_related('author', 'ticket__author')

    # def get_queryset(self):
    #     obj = Ticket.objects.select_related('author').get(pk=self.kwargs['pk'])
    #     self.check_object_permissions(self.request, obj)
    #     return Comment.objects.filter(ticket_id=self.kwargs['pk']).select_related('author', 'ticket__author')

    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsSupportOrAuthor)
