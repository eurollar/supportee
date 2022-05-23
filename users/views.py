from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.models import CustomUser
from users.serializers import (ChangePasswordSerializer, CreateUserSerializer,
                               UserSerializer)


class CreateUser(generics.CreateAPIView):
    """
    Create a new user
    """
    model = CustomUser
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny, )


class GetUpdateUserAndEmail(generics.RetrieveUpdateAPIView):
    """
    Get and update info of current user's name and mail
    """
    def get_object(self):
        return CustomUser.objects.get(pk=self.request.user.id)

    model = CustomUser
    serializer_class = UserSerializer


class UpdateUserPassword(generics.UpdateAPIView):
    """
    Change the password for current user
    """
    model = CustomUser
    serializer_class = ChangePasswordSerializer

    # Get user's object to know current password
    def get_object(self, queryset=None):
        return self.request.user

    # Change current password
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check an old password
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'old_password': ['Wrong password']}, status=status.HTTP_400_BAD_REQUEST)
            # Check passwords matching
            if serializer.data.get('new_password') != serializer.data.get('confirm_password'):
                return Response({'confirm_password': ["Passwords don't match"]}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully'
            }
            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
