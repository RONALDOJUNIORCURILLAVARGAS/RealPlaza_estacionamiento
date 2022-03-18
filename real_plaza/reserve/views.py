from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

from django.conf import settings
from django.shortcuts import redirect,render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from reserve.models import Sede,Reserva,Estacionamiento,Niveles
from reserve.forms import RegistroForm

class RegistrarUsuario(CreateView):
    model=User
    template_name="registration/registro.html"
    form_class=RegistroForm
    success_url=reverse_lazy('inicio')
def registro(request):
    form_class=RegistroForm
    return render(request,'registration/registro.html',{''})

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

@login_required
def Verhistorial(request):
    #Listar con JOIN
    lista=Reserva.objects.all().select_related('Id_sede')
    """ print(reser.query)
    for res in reser:
        print(res.fecha,' || ',res.Id_sede.Nombre) """
    return render(request,'reserve/historialdereserva.html',{'reservas':lista})

@login_required
def reg_reserve_sede(request,id):
    pref=Sede.objects.filter(id=id).order_by('Nombre')
    sedes=Sede.objects.all().order_by('Nombre').exclude(id=id)
    return render(request,'reserve/registro_reserva.html',{'sedes':sedes,'pref':pref})

@login_required
def estacionar(request):
    nivel=Niveles.objects.all()
    return render(request,'reserve/estacionar.html',{'nivel':nivel})

@login_required
def pagar(request):
    return render(request,'reserve/payment.html')



class Pagos(generic.TemplateView):
    template_name='reserve/payment.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PAYPAL_CLIENT_ID'] = settings.PAYPAL_CLIENT_ID
        context['CALLBACK_URL']=self.request.build_absolute_uri(reverse("inicio"))  
        return context
    