from django.urls import path
from .views import RoomList, BookingList, BookingView, BelegungList, CancelBookingView

app_name='bookingapp'

urlpatterns=[
    path('room_list/', RoomList.as_view(), name='RoomList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='BookingView'),
    path('belegung_list/', BelegungList.as_view(), name='BelegungList'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(), name='CancelBookingView'),
]