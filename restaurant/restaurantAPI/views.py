from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from django.http import HttpResponse
import json
from datetime import datetime
from django.core import serializers as core_serializers
from django.views.decorators.csrf import csrf_exempt
from .forms import BookingForm
from .models import *
from .serializers import *

# Create your views here.

def home(request):
    return render(request, 'index.html')

def menu(request):
    queryset = MenuItems.objects.all()
    data = {'menu': queryset}
    return render(request, 'menu.html', {'data': data})

def single_menu(request, pk):
    queryset = MenuItems.objects.get(pk=pk)
    data = {'menu': queryset}
    return render(request, 'menu_item.html', {'data': data})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def about(request):
    return render(request, 'about.html')

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    queryset = Booking.objects.all()
    data = core_serializers.serialize('json', queryset)
    return render(request, 'bookings.html',{"bookings":data})

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
        if exist==False:
            booking = Booking(
                name=data['name'],
                no_of_guests=data['no_of_guests'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
    
    date = request.GET.get('date',datetime.today().date())

    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = core_serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')

class MenuItemView(generics.ListAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuSerializer

class BookingView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    