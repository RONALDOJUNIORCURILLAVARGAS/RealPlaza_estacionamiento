from django.shortcuts import render
from django.views import generic
from reserve.models import Sede

class HomeView(generic.TemplateView):
    template_name='index.html'
# Create your views here.
def bienvenido(request):

    no_sedes=Sede.objects.count()
    #personas=Persona.objects.all()

    #Prdenar de manera ascendente
    sedes=Sede.objects.order_by('id')
    #Ordenar de manera descendente
    #personas=Persona.objects.order_by('-id')

    #creanis un diccionario para mandar al html
    #mensajes={'msg1':'Valor mensaje 1','msg2':'Valor 2'}
    #return render(request,'bienvenido.html',mensajes)
    return render(request,'/sedes/sedes.html',{'no_sedes':no_sedes, 'sedes':sedes})
