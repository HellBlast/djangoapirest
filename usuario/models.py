from django.db import models

class Usuario(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    correo=models.CharField(max_length=50)
    contraseña=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    telefono=models.IntegerField()
    fecha_nacimiento=models.DateField()