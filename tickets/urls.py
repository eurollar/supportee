from django.urls import include, path

from tickets import views

urlpatterns = [
    # List of tickets
    path('api/', views.TicketList.as_view(), name='ticket_list'),
    # Ticket detail
    path('api/<int:pk>/', views.TicketDetail.as_view(), name='ticket_detail'),
    # Comments for tickets
    path('api/<int:pk>/comments/', include('comments.urls'))
]
