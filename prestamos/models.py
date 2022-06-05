from django.db import models


class Libro(models.Model):
    id_libro= models.IntegerField(primary_key=True)
    cod=models.IntegerField()
    titulo=models.CharField(max_length=101)
    isbn=models.CharField(max_length=30)
    editorial=models.CharField(max_length=60)

    numpags=models.IntegerField()

    def titulo_completo(self):
        return"{}".format(self.titulo)

    def __str__(self) -> str:
        return self.titulo_completo()

class Autor(models.Model):
    id_autor=models.IntegerField(primary_key=True)
    nombre_autor=models.CharField(max_length=100)
    nacionalidad=models.CharField(max_length=50)

class Usuario(models.Model):
    id_usuario=models.IntegerField(primary_key=True)
    num_usuario=models.IntegerField()
    nif=models.CharField(max_length=20)
    nombre_usuario=models.CharField(max_length=100)
    direccion=models.CharField(max_length=255)
    telefono=models.CharField(max_length=20)
    def nombre_completo(self):
        return"{}".format(self.nombre_usuario)

    def __str__(self) -> str:
        return self.nombre_completo()
    
class Prestamo(models.Model):

    id_prestamo = models.IntegerField(primary_key=True)
    titulo = models.ForeignKey(Libro, on_delete=models.CASCADE)
    nombre_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    fec_prestamo= models.DateField()
    fec_devolucion= models.DateField()
    
#Psmo = Prestamo.objects.select_related('Libro','Autor')


