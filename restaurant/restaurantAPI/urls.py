from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='single_menu'),
    path('book/', book, name='book'),
    path('about/', about, name='about'),
    path('booking/', BookingView.as_view({'get': 'list', 'post': 'create'}), name='booking'),
]