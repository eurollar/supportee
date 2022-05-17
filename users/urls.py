from django.urls import path

from users import views

urlpatterns = [
    path('', views.GetUpdateUserAndEmail.as_view(), name='user_info'),
    path('create/', views.CreateUser.as_view(), name='create_user'),
    path('new-pass/', views.UpdateUserPassword.as_view(), name='change-password'),
]
