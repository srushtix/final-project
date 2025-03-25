from rest_framework import viewsets, permissions

from .models import Car, Booking

from .serializers import CarSerializer, BookingSerializer
from django.shortcuts import redirect
from django.contrib.auth import logout



class CarViewSet(viewsets.ModelViewSet):

    queryset = Car.objects.all()

    serializer_class = CarSerializer

    permission_classes = [permissions.AllowAny]



class BookingViewSet(viewsets.ModelViewSet):

    queryset = Booking.objects.all()

    serializer_class = BookingSerializer

    permission_classes = [permissions.IsAuthenticated]



def logout_view(request):
    logout(request)
    return redirect('/')
