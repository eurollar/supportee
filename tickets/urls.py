from django.urls import path, include

from tickets import views

urlpatterns = [
    path('api/', views.TicketList.as_view(), name='ticket_list'),
    path('api/<int:pk>/', views.TicketDetail.as_view(), name='ticket_detail'),
    path('api/<int:pk>/comments/', include('comments.urls'))
]
