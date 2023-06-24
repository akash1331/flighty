from django.contrib import admin
from .models import User, Flight, Booking
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class FlightAdminSite(admin.ModelAdmin):
    list_display = ('flight_number','flight_name','origin','destination','departure_date','departure_time','available_seats','available_seats')


class BookingAdminSite(admin.ModelAdmin):
    list_display = ('userid','flight','passenger_name','seat_number','username')

admin.site.register(Flight,FlightAdminSite)
admin.site.register(Booking,BookingAdminSite)

admin.site.site_header = 'Flighty Administrator'