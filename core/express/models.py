from django.db import models
from datetime import datetime


class Clients(models.Model):
    id = models.CharField(max_length=11, primary_key=True, verbose_name='CI/Pasaporte')
    first_name = models.CharField(max_length=30, verbose_name='Nombres')
    last_names = models.CharField(max_length=30, verbose_name='Apellidos')
    fly = models.CharField(max_length=50, verbose_name='Vuelo')
    agency = models.CharField(max_length=50, verbose_name='Agencia')
    arrive_date = models.DateField(default=datetime.now, verbose_name='Fecha LLegada')
    leave_date = models.DateField(verbose_name='Fecha Salida')
    
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        
class Observs(models.Model):
    observ_id = models.CharField(max_length=10, primary_key=True, verbose_name='ID')
    observ_name = models.CharField(max_length=300, verbose_name='Observación')
    clients = models.ManyToManyField(Clients, through='ClientObs')
    
    class Meta:
        verbose_name = "Observación"
        verbose_name_plural = "Observaciones"

class ClientObs(models.Model):
    person = models.ForeignKey(Clients, on_delete=models.CASCADE)
    group = models.ForeignKey(Observs, on_delete=models.CASCADE)
    observ_date = models.DateField(default=datetime.now, verbose_name='Fecha de Observación')
    

class RoomStates(models.Model):
    room_state = models.CharField(max_length=300, verbose_name='Estado Habitación')
    
class Rooms(models.Model):
    number = models.CharField(max_length=4, primary_key=True, verbose_name='Número habitación')
    state = models.ForeignKey(RoomStates, on_delete=models.CASCADE)
    client = models.ManyToManyField(Clients, through='ClientRoom')
    
class ClientRoom(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now, verbose_name='Fecha de asignación')
    
