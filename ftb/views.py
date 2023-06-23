from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, FlightForm,BookingForm
from .models import Flight, Booking
from django.contrib.auth import get_user_model
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('ftb:flight_list')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
        return render(request, 'booking/login.html', {'form': form})
    

def user_logout(request):
    logout(request)
    return redirect('ftb:user_login')
    

def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ftb:user_login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'booking/user_register.html', {'form': form})

@login_required
def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'booking/flight_list.html', {'flights': flights})

@login_required
def flight_details(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, 'booking/flight_details.html', {'flight': flight})

@login_required
def book_flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    if flight.available_seats > 0:
        User=get_user_model()
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
    # Set any additional fields for the booking
            booking.userid =request.user.id

    # Save the booking
            booking.save()
    
    # Optionally, you can display a success message
            messages.success(request, 'Flight booked successfully!')
            return redirect('ftb:flight_list')
        else:
            form=BookingForm()
            return render(request, 'booking/book_flight.html', {'flight': flight,'form':form})
    else:
        error_message = 'No available seats on this flight.'
        return render(request, 'booking/flight_details.html', {'flight': flight, 'error_message': error_message})

@user_passes_test(lambda u: u.is_superuser, login_url='ftb:user_login')
def admin_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ftb:admin_login')
    else:
        form = UserCreationForm()
        return render(request, 'booking/admin_register.html',{'form': form})

@user_passes_test(lambda u: u.is_superuser, login_url='ftb:user_login')
def admin_logout(request):
    logout(request)
    return redirect('ftb:user_login')

@user_passes_test(lambda u: u.is_superuser, login_url='ftb:user_login')
def admin_add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ftb:flight_list')
    else:
        form = FlightForm()
    return render(request, 'booking/admin_add_flight.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser, login_url='ftb:user_login')
def admin_remove_flight(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    if request.method == 'POST':
        flight.delete()
        return redirect('ftb:flight_list')
    return render(request, 'booking/admin_remove_flight.html', {'flight': flight})

def my_booking(request):
    bookings = Booking.objects.filter(userid=request.user.id)
    return render(request, 'booking/my_booking.html', {'bookings': bookings})

    
@user_passes_test(lambda u: u.is_superuser, login_url='ftb:user_login')
def admin_view_bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'booking/admin_view_bookings.html', {'bookings': bookings})