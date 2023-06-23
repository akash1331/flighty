from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission,BaseUserManager,AbstractBaseUser
import datetime


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Create and save a regular user
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Create and save a superuser
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
    
class Flight(models.Model):
    flight_number = models.CharField(max_length=10,null=True)
    origin = models.CharField(max_length=100,null=True)
    destination = models.CharField(max_length=100,null=True)
    departure_date = models.DateField(default=datetime.date.today)
    departure_time = models.TimeField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    available_seats = models.IntegerField(default=60)

    def __str__(self):
        return self.flight_number

class Booking(models.Model):
    userid = models.IntegerField(null=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100,null=True)
    seat_number = models.CharField(max_length=10,null=True)
    username=models.CharField(max_length=200,null=True)

    # def __str__(self):
    #     return f"Booking #{self.pk} - {self.user.username}"


