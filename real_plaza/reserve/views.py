from winreg import QueryValue
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
import time
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
    userid = request.user.id
    lista=Reserva.objects.all().select_related('Id_sede').filter(Id_user=userid)
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
    id_sede=request.POST["id_sede"]
    placa=request.POST["placa"]
    fecha=request.POST["fecha"]
    hora=request.POST["hora"]
    userid = request.user.id
    if len(placa)!=0 and len(id_sede)!=0 and len(fecha)!=0 and len(hora)!=0:
        print(id_sede)
        estacionamiento=Estacionamiento.objects.all()
        reservado=Reserva.objects.all().filter(Id_sede=id_sede)

        #print("la fecha original es :"+fecha)
        reserva=[]
        #print(type(reserva))
        for res in reservado:
            if (str(res.fecha)==fecha):
                h_ini_reservada=str(res.hora)
                hour_res=int(str(res.hora)[0:2])
                minu_res=int(str(res.hora)[3:5])
                hour_sel=int(str(hora)[0:2])
                min_sele=int(str(hora)[3:5])
                if(hour_res==hour_sel):
                    #Horas y minutos reservados
                    """ if(<min_sele):
                        hour=hour+1
                        hour=str(hour) """
                   # print(hour_res)
                    """ h_fin_reservada=str(res.hora + 1)
                    if(h_ini_reservada<= hora and hora<=h_fin_reservada):
                        print("hora seleccionada : "+hora) """
                    reserva.append(str(res.Id_estacionamiento_id))  
                    #print("La fecha reservada es: "+str(res.fecha)+"y la hora es:"+str(res.hora))
        #print(reserva)
        #for s in reserva:

            #print(type(s))
        #for r in estacionamiento:
            #print(type(r))
        context={
            "id_sede":request.POST["id_sede"],
            "placa":request.POST["placa"],
            "fecha":request.POST["fecha"],
            "hora":request.POST["hora"],
            "nivel":Niveles.objects.all(),
            "estacionamiento":estacionamiento,
            "reservado":reserva,
        }
        return render(request,'reserve/estacionar.html',context)
    else:
        return redirect('reg-reserve')

@login_required
def pagar(request):
    sede=request.POST["sede"]
    nombre=""
    nombrar_sede=Sede.objects.filter(id=sede)
    tiempo=request.POST["hora"]
    hora=tiempo[0:2]
    minuto=tiempo[3:5]
    estacionamiento=request.POST["estacionamiento"]

    print(estacionamiento)
    print(hora)
    print(minuto)
    if len(estacionamiento)!=0 and estacionamiento!='0':
        for n in nombrar_sede:
            nombre=n.Nombre
        context={
            "PAYPAL_CLIENT_ID":settings.PAYPAL_CLIENT_ID,
            "CALLBACK_URL":request.build_absolute_uri(reverse("inicio")),
            "sede":request.POST["sede"],
            "placa":request.POST["placa"],
            "fecha":request.POST["fecha"],
            "tiempo":request.POST["hora"],
            "nivel_estacionamiento":request.POST["nivel_estacionamiento"],
            "estacionamiento":request.POST["estacionamiento"],
            "nombre_sede":nombre,
            "hora":hora,
            "minutos":minuto,
        }
        return render(request,'reserve/payment.html',context)
    else:
        context={
            "id_sede":request.POST["sede"],
            "placa":request.POST["placa"],
            "fecha":request.POST["fecha"],
            "hora":request.POST["hora"],
            "nivel":Niveles.objects.all()
        }
        return render(request,'reserve/estacionar.html',context)

@login_required
def pago_validado(request,sede,estacionamiento,placa,fecha,hora,minuto):
    
    
    reserva=Reserva()
    
    tiempo=hora+':'+minuto
    print("Placa: " + placa)
    print("la sede es : "+str(sede) )
    print("El estacionamiento es :" + str(estacionamiento))
    print("Fecha: " + fecha)
    print("Hora: " + tiempo)

    userid = request.user.id
	
    print('Id del usuario :' + str(userid))
    reserva.Id_user_id=userid
    reserva.Id_sede_id=sede
    reserva.placa=placa 
    reserva.fecha=fecha
    reserva.hora=tiempo
    reserva.Pago=1
    reserva.Id_estacionamiento_id=estacionamiento
    
    reserva.save()
    #return render(request,'index.html')
    return redirect('inicio')

class Pagos(generic.TemplateView):
    template_name='reserve/payment.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PAYPAL_CLIENT_ID'] = settings.PAYPAL_CLIENT_ID
        context['CALLBACK_URL']=self.request.build_absolute_uri(reverse("inicio"))  
        return context
    