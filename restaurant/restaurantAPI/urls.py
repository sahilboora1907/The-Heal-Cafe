from django.urls import path
from .views import *
urlpatterns = [
    path('menu/', MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='single_menu'),
    path('booking/', BookingView.as_view({'get': 'list', 'post': 'create'}), name='booking'),
]