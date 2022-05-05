from django.shortcuts import render
from rest_framework import status, permissions, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from tickets.models import Ticket
from tickets.permissions import IsClientOrReadOnly, IsSupportOrReadOnly
from tickets.serializers import TaskSerializer, SupportTaskSerializer, UserTaskSerializer


class TicketList(generics.ListCreateAPIView):
    def get_queryset(self):
        if self.request.user.type == 'support':
            return Ticket.objects.all()
        else:
            return Ticket.objects.filter(author_id=self.request.user.id)

    def get_serializer_class(self):
        if self.request.user.type == 'support':
            return SupportTaskSerializer
        return UserTaskSerializer

    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsClientOrReadOnly)


class TicketDetail(generics.RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()

    def get_serializer_class(self):
        if self.request.user.type == 'support':
            return SupportTaskSerializer
        return UserTaskSerializer

    permission_classes = (IsAuthenticated, IsSupportOrReadOnly)

# class TicketView(APIView):
#     serializer_class = TaskSerializer
#     model = Ticket
#     permission_classes = (IsClientOrReadOnly, permissions.AllowAny)
#
#     def get(self, request):
#         queryset = Ticket.objects.all()
#         if request.user.type == 'support':
#             queryset = Ticket.objects.all()
#         else:
#             queryset = Ticket.objects.filter(author_id=request.user.id)
#         serializer_for_queryset = TaskSerializer(
#             instance=queryset,
#             many=True
#         )
#         return Response({'tasks': serializer_for_queryset.data})
#
#     def post(self, request):
#         context = {'request': self.request}
#         serializer_for_writing = self.serializer_class(data=request.data, context=context)
#         serializer_for_writing.is_valid(raise_exception=True)
#         serializer_for_writing.save()
#         return Response(data=serializer_for_writing.data, status=status.HTTP_201_CREATED)
