from django.db import models
from django.contrib.auth import get_user_model


#Optenemos el usuario para enlazarlo a otras tablas
User=get_user_model()
class Sede(models.Model):
    Nombre = models.CharField(max_length=150)   
    Direccion=models.CharField(max_length=500)
    Aforo_total=models.IntegerField()
    Aforo_actual=models.IntegerField()
    Image_sede=models.ImageField(upload_to='sede_images')
    def __str__(self):
        return f'Sede {self.id}:{self.Nombre}'
class Niveles(models.Model):
    nombre=models.CharField(max_length=150)
    def __str__(self):
        return f'Nivel: {self.nombre}'
class Zona(models.Model):
    nombre=models.CharField(max_length=300)
    def __str__(self):
        return f' ZONA: {self.nombre}'
    
class Estacionamiento(models.Model):
    id_zona=models.ForeignKey(Zona,on_delete=models.SET_NULL,null=True)
    numero=models.IntegerField()
    id_nivel=models.ForeignKey(Niveles,on_delete=models.SET_NULL,null=True)
    estado_disponibilidad=models.BooleanField(default=False)
    def __str__(self):
        return f"La zona es : {self.id_zona}, Nivel: {self.id_nivel} y Número:{self.numero}"
    

class Reserva(models.Model):
    Id_user=models.ForeignKey(User,on_delete=models.CASCADE)
    Id_sede=models.ForeignKey(Sede,on_delete=models.SET_NULL,null=True)
    placa=models.CharField(max_length=7)
    fecha=models.DateField()
    hora= models.TimeField()
    Pago=models.IntegerField()
    Id_estacionamiento=models.ForeignKey(Estacionamiento,on_delete=models.SET_NULL,null=True)
