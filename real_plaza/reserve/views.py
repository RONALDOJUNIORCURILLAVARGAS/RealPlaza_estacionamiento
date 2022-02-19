import re
import django
from django.shortcuts import redirect,render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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
    return render(request,'reserve/registro_reserva.html')
@login_required
def sedes(request):
    #AQUI DEBO cargar el contenido


    return render(request, 'sedes/sedes.html')
