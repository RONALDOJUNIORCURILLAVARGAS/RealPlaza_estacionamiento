from django.db import models

# Create your models here.
class Sede(models.Model):
    Nombre = models.CharField(max_length=150)   
    Direccion=models.CharField(max_length=500)
    Aforo_total=models.IntegerField()
    Aforo_actual=models.IntegerField()
    #Image_sede=models.ImageField(upload_to='sede_images')
    def __str__(self):
        return f'Sede {self.id}:{self.Nombre}'