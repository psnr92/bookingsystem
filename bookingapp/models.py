from django.db import models

# Create your models here.

class Room(models.Model):
    raumID = models.CharField(max_length=10)
    anzahl_plaetze = models.IntegerField()
    anzahl_pc = models.IntegerField()

    def __str__(self):
        return f'{self.raumID}. Sitzplätze: {self.anzahl_plaetze}. Anzahl PCs: {self.anzahl_pc}'