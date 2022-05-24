from django.urls import path

from users import views

urlpatterns = [
    # Show and change user's name and mail
    path('', views.GetUpdateUserAndEmail.as_view(), name='user_info'),
    # Create new user
    path('create/', views.CreateUser.as_view(), name='create_user'),
    # Change user's password
    path('new-pass/', views.UpdateUserPassword.as_view(), name='change-password'),
]
