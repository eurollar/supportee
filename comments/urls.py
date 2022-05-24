from django.urls import path

from comments import views

urlpatterns = [
    # Show comments
    path('', views.CommentsList.as_view(), name='ticket_comment'),
]
