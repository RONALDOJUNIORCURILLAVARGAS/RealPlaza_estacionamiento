from django.contrib import admin

# Register your models here.
from reserve.models import Sede,Reserva,Estacionamiento,Niveles,Zona

admin.site.register(Sede)
admin.site.register(Reserva)
admin.site.register(Estacionamiento)
admin.site.register(Niveles)
admin.site.register(Zona)