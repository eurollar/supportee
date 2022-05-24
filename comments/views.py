from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from comments.models import Comment
from comments.permissions import IsSupportOrAuthor
from comments.serializers import CommentSerializer


class CommentsList(generics.ListCreateAPIView):
    """
    Get list with comments for current ticket
    """
    def get_queryset(self):
        return Comment.objects.filter(
            ticket_id=self.kwargs['pk']
        ).select_related(
            'author', 'ticket__author'
        )

    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsSupportOrAuthor)
