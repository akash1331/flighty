from django.urls import path
from ftb.views import *
app_name = 'ftb'

urlpatterns = [
    path('', user_login, name='user_login'),
    path('user/login/', user_login, name='user_login'),
    path('user/logout/', user_logout, name='user_logout'),
    path('user/register/', user_register, name='user_register'),
    path('user/flights/', flight_list, name='flight_list'),
    path('user/flight/<int:flight_id>/', flight_details, name='flight_details'),
    path('user/flight/book/<int:flight_id>/', book_flight, name='book_flight'),
    #path('user/bookings/', user_bookings, name='user_bookings'),
    path('admin_register/', admin_register, name='admin_register'),
    path('admin_logout/', admin_logout, name='admin_logout'),
    path('admin_add-flight/', admin_add_flight, name='admin_add_flight'),
    path('admin_remove-flight/<int:flight_id>/', admin_remove_flight, name='admin_remove_flight'),
    path('my-booking/',my_booking, name='my_booking'),
     path('view-bookings/', admin_view_bookings, name='admin_view_bookings'),
]
