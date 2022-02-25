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

class Estacionamiento(models.Model):
    ADDRESS_CHOICES=(
        ('A','Zona A'),
        ('B','Zona B'),
        ('C','Zona C'),
        ('D','Zona D'),
    )
    NIVEL_CHOICES=(
        ('1','Primer Nivel'),
        ('2','Segundo Nivel'),
        ('3','Tercer Nivel'),
    )
    zona=models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    numero=models.IntegerField()
    piso_nivel=models.CharField(max_length=1, choices=NIVEL_CHOICES)
    estado_disponibilidad=models.BooleanField(default=False)
    def __str__(self):
        return f"El id es : {self.id}, Nivel: {self.piso_nivel}"
    

class Reserva(models.Model):

    Id_sede=models.ForeignKey(Sede,on_delete=models.SET_NULL,null=True)
    placa=models.CharField(max_length=7)
    fecha=models.DateField()
    hora= models.TimeField()
    Id_estacionamiento=models.ForeignKey(Estacionamiento,on_delete=models.SET_NULL,null=True)
