from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .models import *
from .serializers import *

# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuSerializer

class BookingView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    