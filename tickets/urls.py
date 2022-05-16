from django.urls import path, include

from tickets import views

urlpatterns = [
    path('api/', views.TicketList.as_view()),
    path('api/<int:pk>/', views.TicketDetail.as_view()),
    path('api/<int:pk>/comments/', include('comments.urls'))
]
