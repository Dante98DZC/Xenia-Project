from django.db import models
from datetime import datetime


class RoomState(models.Model):
    room_state = models.CharField(
        max_length=300, verbose_name='Estado Habitación')

class Room(models.Model):
    number = models.CharField(max_length=4, primary_key=True, verbose_name='Número habitación')
    state = models.ForeignKey(RoomState, on_delete=models.CASCADE)

class Client(models.Model):
    id = models.CharField(max_length=11, primary_key=True, verbose_name='CI/Pasaporte')
    rooms = models.ManyToManyField(Room, through="ClientRoom", through_fields=("cliente", "habitacion"))
    first_name = models.CharField(max_length=30, verbose_name='Nombres')
    last_names = models.CharField(max_length=30, verbose_name='Apellidos')
    fly = models.CharField(max_length=50, verbose_name='Vuelo')
    agency = models.CharField(max_length=50, verbose_name='Agencia')
    arrive_date = models.DateField(default=datetime.now, verbose_name='Fecha LLegada')
    leave_date = models.DateField(verbose_name='Fecha Salida')
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

        
class ClientRoom(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now,
                            verbose_name='Fecha de asignación')

class Observ(models.Model):
    observ_id = models.CharField(
        max_length=10, primary_key=True, verbose_name='ID')
    observ_name = models.CharField(max_length=300, verbose_name='Observación')
    clients = models.ManyToManyField(Client, through='ClientOb')

    class Meta:
        verbose_name = "Observación"
        verbose_name_plural = "Observaciones"


class ClientOb(models.Model):
    person = models.ForeignKey(Client, on_delete=models.CASCADE)
    group = models.ForeignKey(Observ, on_delete=models.CASCADE)
    observ_date = models.DateField(
        default=datetime.now, verbose_name='Fecha de Observación')


class Departament(models.Model):
    id_dpt = models.CharField(primary_key=True, verbose_name='ID Dpt')
    name_dpt = models.CharField(max_length=50, verbose_name='Nombre Dpt')
    phone_number = models.CharField(max_length=10, verbose_name='Teléfono Dpt')


class Attendants(models.Model):
    ci_attendant = models.CharField()
    first_name = models.CharField(max_length=30, verbose_name='Nombres')
    last_names = models.CharField(max_length=30, verbose_name='Apellidos')
    dpt = models.ForeignKey(Departament, on_delete=models.CASCADE)


class KindRep(models.Model):
    id_kind = models.CharField(primary_key=True, verbose_name='ID Tipo')
    name_kind = models.CharField(max_length=50, verbose_name='Nombre Tipo')


class Executive(models.Model):
    ci_executive = models.CharField(max_length=11, primary_key=True)
    first_name = models.CharField(max_length=30, verbose_name='Nombres')
    last_names = models.CharField(max_length=30, verbose_name='Apellidos')
    user_name = models.CharField()


class Resolution(models.Model):
    description = models.CharField(max_length=500, verbose_name='Descripción')


class Report(models.Model):
    client_room = models.ForeignKey(ClientRoom, on_delete=models.CASCADE)
