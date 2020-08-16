from django.db import models
from django.conf import settings

# Create your models here.

class Room(models.Model):
    raumID = models.CharField(max_length=10)
    anzahl_plaetze = models.IntegerField()
    anzahl_pc = models.IntegerField()

    def __str__(self):
        return f'{self.raumID}. Sitzplätze: {self.anzahl_plaetze}. Anzahl PCs: {self.anzahl_pc}'

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} hat {self.room} gebucht. Ckeck-In: {self.check_in} . Ckeck-Out: {self.check_out}'