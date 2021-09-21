from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def myView(request):
    return HttpResponse("Hola esta es mi primera URL")