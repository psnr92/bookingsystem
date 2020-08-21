from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView
from .models import Room, Booking
from .forms import AvailabilityForm
from bookingapp.booking_functions.availability import check_availability

# Create your views here.

# Erstellt eine Liste der Räume
class RoomList(ListView):
    model=Room


# Erstellt eine Liste aller Belegungen
class BelegungList(ListView):
    model=Booking


# Erstellt eine Liste der Buchungen und fragt User-Berechtigung ab. (Aktuelle Verwendung: Buchungsliste gefiltert nach Username)
# Admin: Sieht alle Buchungen
# Normaler User: Sieht nur seine Buchungen
class BookingList(ListView):
    model=Booking
    def get_queryset(self, *args, **kwargs):
#        if self.request.user.is_staff:
#            booking_list = Booking.objects.all()
#            return booking_list
#        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list


# Raumbuchungsfunktion & gleichzeitige Prüfung auf Raumverfügbarkeit
class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])
        available_rooms=[]
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        if len(available_rooms)>0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user = self.request.user,
                room = room,
                check_in = data['check_in'],
                check_out = data['check_out']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('Zeitslot für diese Art Raumkategorie bereits belegt. Bitte versuchen Sie einen anderen Zeitslot oder wählen Sie eine andere Raumkategorie.')