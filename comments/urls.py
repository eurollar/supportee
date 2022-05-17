from django.urls import path

from comments import views

urlpatterns = [
    path('', views.CommentsList.as_view(), name='ticket_comment'),
]
