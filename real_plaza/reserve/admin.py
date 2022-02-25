from django.contrib import admin

# Register your models here.
from reserve.models import Sede,Reserva,Estacionamiento

admin.site.register(Sede)
admin.site.register(Reserva)
admin.site.register(Estacionamiento)