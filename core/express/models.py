from django.db import models
from datetime import datetime


class RoomState(models.Model):
    room_state = models.CharField(
        max_length=300, verbose_name='Estado Habitación')

    class Meta:
        verbose_name = "Estado Habitación"
        verbose_name_plural = "Estado Habitaciones"


class Room(models.Model):
    number = models.CharField(
        max_length=4, primary_key=True, verbose_name='No Hab.')
    state = models.ForeignKey(RoomState, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Habitación"
        verbose_name_plural = "Habitaciones"


class Observ(models.Model):
    observ_name = models.CharField(max_length=300, verbose_name='Observación')

    class Meta:
        verbose_name = "Observación"
        verbose_name_plural = "Observaciones"


class Client(models.Model):
    id = models.CharField(max_length=11, primary_key=True,
                          verbose_name='CI/Pasaporte')
    rooms = models.ManyToManyField(
        Room, through="ClientRoom", through_fields=("client", "room"))
    first_name = models.CharField(max_length=30, verbose_name='Nombres')
    last_name = models.CharField(max_length=30, verbose_name='Apellidos')
    fly = models.CharField(max_length=50, verbose_name='Vuelo')
    agency = models.CharField(max_length=50, verbose_name='Agencia')
    arrive_date = models.DateField(
        default=datetime.now, verbose_name='Fecha LLegada')
    leave_date = models.DateField(verbose_name='Fecha Salida')
    observations = models.ManyToManyField(
        Observ, through="ClientOb", through_fields=("client", "observ"))
    
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class ClientOb(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    observ = models.ForeignKey(Observ, on_delete=models.CASCADE)
    observ_date = models.DateField(
        default=datetime.now, verbose_name='Fecha de Observación')

    class Meta:
        verbose_name = "Observ Cliente"
        verbose_name_plural = "Observ Clientes"


class ClientRoom(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Cliente")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="No. Hab")
    host_date = models.DateField(default=datetime.now,
                                 verbose_name='Fecha hospedaje')

    def __str__(self):
        return '%s %s' % (self.room, self.client)

    class Meta:
        verbose_name = "Habitación Cliente"
        verbose_name_plural = "Habitación Clientes"


class Departament(models.Model):
    id_dpt = models.CharField(
        primary_key=True, max_length=10, verbose_name='ID Dpt')
    name_dpt = models.CharField(max_length=50, verbose_name='Nombre Dpt')
    phone_number = models.CharField(max_length=10, verbose_name='Teléfono Dpt')

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"


class Attendants(models.Model):
    ci_attendant = models.CharField(
        max_length=11, primary_key=True, verbose_name='Ci Encargado')
    first_name = models.CharField(max_length=30, verbose_name='Nombres')
    last_name = models.CharField(max_length=30, verbose_name='Apellidos')
    dpt = models.ForeignKey(Departament, on_delete=models.CASCADE)
    
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = "Encargado"
        verbose_name_plural = "Encargados"


class KindRep(models.Model):
    id_kind = models.AutoField(primary_key=True, verbose_name='ID Tipo')
    name_kind = models.CharField(max_length=50, verbose_name='Nombre Tipo')
    
    def __str__(self):
        return self.name_kind

    class Meta:
        verbose_name = "Tipo Reporte"
        verbose_name_plural = "Tipo Reportes"


class Executive(models.Model):
    ci_executive = models.CharField(
        max_length=11, primary_key=True, verbose_name='CI ejecutivo')
    first_name = models.CharField(max_length=30, verbose_name='Nombres')
    last_name = models.CharField(max_length=30, verbose_name='Apellidos')
    user_name = models.CharField(max_length=11, verbose_name='Usuario')

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
    
    class Meta:
        verbose_name = "Ejecutivo"
        verbose_name_plural = "Ejecutivo"


class Responce(models.Model):
    id_response = models.BigAutoField(
        primary_key=True, verbose_name='ID Respuesta')
    description = models.CharField(max_length=500, verbose_name='Descripción')

    def __str__(self):
        return self.description
    

    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"


class Report(models.Model):
    report_number = models.AutoField(
        primary_key=True, verbose_name='No. Reporte')
    client_room = models.ForeignKey(ClientRoom, on_delete=models.CASCADE, verbose_name='No. Habitación')
    client_name = models.ForeignKey(ClientRoom, on_delete=models.CASCADE, verbose_name='Cliente')
    executive = models.ForeignKey(Executive, on_delete=models.CASCADE, verbose_name="Ejecutivo")
    attendant = models.ForeignKey(Attendants, on_delete=models.CASCADE, verbose_name="Encargado")
    kind = models.ForeignKey(KindRep, on_delete=models.CASCADE, verbose_name="Tipo")
    description = models.CharField(max_length=500, verbose_name='Descripción')
    get_date_time = models.DateTimeField(
        default=datetime.now, verbose_name='Fecha de recibo')
    com_date_time = models.DateTimeField(
        default=datetime.now, verbose_name='Fecha de comunicado')
    response_date_time = models.DateTimeField(
        blank=True, null=True, verbose_name='Fecha de respuesta')
    responsed = models.BooleanField(default=False, verbose_name='Resuelto')
    responce = models.ForeignKey(
        Responce, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Respuesta')

    
    class Meta:
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"
