from comments import views
from django.urls import path

urlpatterns = [
    # Show comments
    path('', views.CommentsList.as_view(), name='ticket_comment'),
]
