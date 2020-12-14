from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def index(request):
    return render(request,"app1/base.html", {})

def bestellung(request):
    #Daten gelesen
    kundenliste = Kunde.objects.all()
    #Daten an den Render übertragen
    return render(request, "app1/bestellung.html", {'kunden':kundenliste})