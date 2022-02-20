import re
import django
from django.shortcuts import redirect,render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from reserve.models import Sede

@login_required
def index(request):
    return render(request,'index.html')
    
@login_required
def salir(request):
    logout(request)
    return redirect('/')
@login_required
def reservas(request):
    return render(request,'reserve/reserva.html')
@login_required
def reg_reserve(request):
    sedes=Sede.objects.order_by('Nombre')
    return render(request,'reserve/registro_reserva.html',{'sedes':sedes})
@login_required
def sedes(request):
    #AQUI DEBO cargar el contenido


    #return render(request, 'sedes/sedes.html')

    no_sedes=Sede.objects.count()
    #personas=Persona.objects.all()

    #Prdenar de manera ascendente
    sedes=Sede.objects.order_by('id')
    #Ordenar de manera descendente
    #personas=Persona.objects.order_by('-id')

    #creanis un diccionario para mandar al html
    #mensajes={'msg1':'Valor mensaje 1','msg2':'Valor 2'}
    #return render(request,'bienvenido.html',mensajes)
    return render(request,'sedes/sedes.html',{'no_sedes':no_sedes, 'sedes':sedes})
