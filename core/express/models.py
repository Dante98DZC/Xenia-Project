from functools import _Descriptor
from django.db import models
from datetime import datetime


class Client(models.Model):
    id = models.CharField(max_length=11, primary_key=True,
                          verbose_name='CI/Pasaporte')
    first_name = models.CharField(max_length=30, verbose_name='Nombres')
    last_names = models.CharField(max_length=30, verbose_name='Apellidos')
    fly = models.CharField(max_length=50, verbose_name='Vuelo')
    agency = models.CharField(max_length=50, verbose_name='Agencia')
    arrive_date = models.DateField(
        default=datetime.now, verbose_name='Fecha LLegada')
    leave_date = models.DateField(verbose_name='Fecha Salida')

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Observ(models.Model):
    observ_id = models.CharField(
        max_length=10, primary_key=True, verbose_name='ID')
    observ_name = models.CharField(max_length=300, verbose_name='Observación')
    clients = models.ManyToManyField(Client, through='ClientObs')

    class Meta:
        verbose_name = "Observación"
        verbose_name_plural = "Observaciones"


class ClientOb(models.Model):
    person = models.ForeignKey(Client, on_delete=models.CASCADE)
    group = models.ForeignKey(Observ, on_delete=models.CASCADE)
    observ_date = models.DateField(
        default=datetime.now, verbose_name='Fecha de Observación')


class RoomState(models.Model):
    room_state = models.CharField(
        max_length=300, verbose_name='Estado Habitación')


class Room(models.Model):
    number = models.CharField(
        max_length=4, primary_key=True, verbose_name='Número habitación')
    state = models.ForeignKey(RoomState, on_delete=models.CASCADE)
    client = models.ManyToManyField(Client, through='ClientRoom')


class ClientRoom(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now,
                            verbose_name='Fecha de asignación')

class Departament(models.Model):
    id_dpt = models.CharField(primary_key=True, verbose_name='ID Dpt')
    name_dpt = models.CharField(max_length=50, verbose_name='Nombre Dpt')
    phone_number = models.CharField(max_length=10,verbose_name='Teléfono Dpt')
    
class Attendants(models.Model):
    ci_attendant = models.CharField(id = models.CharField(max_length=11, primary_key=True,
                          verbose_name='CI Encargado'))
    first_name = models.CharField(max_length=30, verbose_name='Nombres')
    last_names = models.CharField(max_length=30, verbose_name='Apellidos')
    dpt = models.ForeignKey(Departament, on_delete=models.CASCADE)

class KindRep(models.Model):
    id_kind = models.CharField(primary_key=True, verbose_name='ID Tipo')
    name_kind= models.CharField(max_length=50, verbose_name='Nombre Tipo')
    
class Executives(models.Model):
    ci_executive = models.CharField(id = models.CharField(max_length=11, primary_key=True,
                          verbose_name='CI Ejecutivo'))
    first_name = models.CharField(max_length=30, verbose_name='Nombres')
    last_names = models.CharField(max_length=30, verbose_name='Apellidos')
    user_name = models.CharField()

class Resolutions(models.Model):
    description = models.CharField(max_length=500, verbose_name='Descripción')
    
class Reports(models.Model):
    id_report = models.CharField(primary_key=True, verbose_name='ID Reporte')
    client = models.ForeignKey(ClientRoom, on_delete=models.CASCADE)
    room = models.ForeignKey()