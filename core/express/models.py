from django.db import models
from datetime import datetime
    
class Client(models.Model):
    id = models.CharField(max_length=11, primary_key=True, verbose_name='CI/Pasaporte')
    first_name = models.CharField(max_length=30, verbose_name='Nombres')
    last_names = models.CharField(max_length=30, verbose_name='Apellidos')
    fly = models.CharField(max_length=50, verbose_name='Vuelo')
    agency = models.CharField(max_length=50, verbose_name='Agencia')
    arrive_date =models.DateField(default=datetime.now , verbose_name='Fecha LLegada')
    leave_date =models.DateField(verbose_name='Fecha Salida')
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        