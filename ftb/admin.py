from django.contrib import admin

from .models import User, Flight, Booking

from django.contrib.auth.models import Group

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin




#admin.site.register(User, UserAdmin)
admin.site.register(Flight)
admin.site.register(Booking)