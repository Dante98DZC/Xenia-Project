from datetime import datetime

from django.db import models
from django.db.models import Max


class RoomState(models.Model):
    room_state = models.CharField(
        unique=True, max_length=120, verbose_name="Estado Habitación"
    )

    class Meta:
        verbose_name = "Estado Habitación"
        verbose_name_plural = "Estado Habitaciones"

    def __str__(self):
        return self.room_state


class Room(models.Model):
    def room_number():
        no = Room.objects.aggregate(last_room=Max("number"))["last_room"]
        if no == None:
            return 1
        else:
            return no + 1

    number = models.IntegerField(verbose_name="No Hab.", default=room_number)
    state = models.ForeignKey(
        RoomState,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Estado",
    )

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = "Habitación"
        verbose_name_plural = "Habitaciones"


class Observ(models.Model):
    observ_name = models.CharField(
        unique=True, max_length=120, verbose_name="Nombre de Estancia"
    )

    def __str__(self):
        return str(self.observ_name)

    class Meta:
        verbose_name = "Estancia"
        verbose_name_plural = "Estancias"


class Client(models.Model):
    id = models.CharField(max_length=11, primary_key=True, verbose_name="CI/Pasaporte")
    rooms = models.ManyToManyField(
        Room, through="ClientRoom", through_fields=("client", "room")
    )
    first_name = models.CharField(max_length=30, verbose_name="Nombres")
    last_name = models.CharField(max_length=30, verbose_name="Apellidos")
    fly = models.CharField(max_length=50, verbose_name="Vuelo")
    agency = models.CharField(max_length=50, verbose_name="Agencia")
    arrive_date = models.DateField(default=datetime.now, verbose_name="Fecha LLegada")
    leave_date = models.DateField(verbose_name="Fecha Salida")
    observations = models.ManyToManyField(
        Observ,
        through="ClientOb",
        through_fields=("client", "observ"),
        verbose_name="Estancia",
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class ClientOb(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Cliente")
    observ = models.ForeignKey(
        Observ, on_delete=models.CASCADE, verbose_name="Estancia"
    )
    observ_date = models.DateField(default=datetime.now, verbose_name="Fecha estancia")

    class Meta:
        verbose_name = "Estancia Cliente"
        verbose_name_plural = "Estancias Clientes"


class ClientRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="No. Hab")
    client = models.ForeignKey(
        Client, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Cliente"
    )
    host_date = models.DateField(
        default=datetime.now, blank=True, null=True, verbose_name="Fecha hospedaje"
    )

    def __str__(self):
        return f"{self.room} : {self.client}"

    class Meta:
        verbose_name = "Habitación Cliente"
        verbose_name_plural = "Habitación Clientes"


class Departament(models.Model):
    name_dpt = models.CharField(max_length=50, verbose_name="Nombre Dpt")
    phone_number = models.CharField(max_length=10, verbose_name="Teléfono Dpt")

    def __str__(self):
        return self.name_dpt

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"


class Attendant(models.Model):
    ci_attendant = models.CharField(max_length=11, primary_key=True, verbose_name="CI")
    first_name = models.CharField(max_length=30, verbose_name="Nombres")
    last_name = models.CharField(max_length=30, verbose_name="Apellidos")
    dpt = models.ForeignKey(
        Departament, on_delete=models.CASCADE, verbose_name="Departamento"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Encargado"
        verbose_name_plural = "Encargados"


class KindRep(models.Model):
    name_kind = models.CharField(max_length=50, unique=True, verbose_name="Nombre")

    def __str__(self):
        return self.name_kind

    class Meta:
        verbose_name = "Tipo de Reporte"
        verbose_name_plural = "Tipo de Reportes"


class Executive(models.Model):
    ci_executive = models.CharField(
        max_length=11, primary_key=True, verbose_name="CI ejecutivo"
    )
    first_name = models.CharField(max_length=30, verbose_name="Nombres")
    last_name = models.CharField(max_length=30, verbose_name="Apellidos")
    user_name = models.CharField(max_length=11, verbose_name="Usuario")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Ejecutivo"
        verbose_name_plural = "Ejecutivos"


class Responce(models.Model):
    description = models.TextField(unique=True, verbose_name="Descripción")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"


class Report(models.Model):
<<<<<<< Updated upstream
    report_number = models.AutoField(
        primary_key=True, verbose_name='No.')
    client_room = models.ForeignKey(
        ClientRoom, on_delete=models.CASCADE, verbose_name='Habitación | Cliente')
=======
    report_number = models.AutoField(primary_key=True, verbose_name="No.")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Habitación")
>>>>>>> Stashed changes
    # client_name = models.ForeignKey(ClientRoom, on_delete=models.CASCADE, verbose_name='Cliente')
    executive = models.ForeignKey(
        Executive, on_delete=models.CASCADE, verbose_name="Ejecutivo"
    )
    attendant = models.ForeignKey(
        Attendant, on_delete=models.CASCADE, verbose_name="Encargado"
    )
    kind = models.ForeignKey(
        KindRep, on_delete=models.CASCADE, verbose_name="Tipo de reporte"
    )
    description = models.TextField(verbose_name="Descripción")
    get_date_time = models.DateTimeField(
        default=datetime.now, verbose_name="Fecha de recibo"
    )
    top_date_time = models.DateTimeField(
        default=datetime.now, verbose_name="Fecha tope"
    )
    response_date_time = models.DateTimeField(
        blank=True, null=True, verbose_name="Fecha de respuesta"
    )
    responsed = models.BooleanField(default=False, verbose_name="Resuelto")
    agree = models.BooleanField(default=False, verbose_name="Conforme")
    responce = models.ForeignKey(
        Responce,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Respuesta",
    )

    class Meta:
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"
