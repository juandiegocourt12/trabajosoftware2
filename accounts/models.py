from django.db import models
from django.contrib import admin
# Create your models here.
class Usuario(models.Model):

    codigo = models.IntegerField(primary_key = True, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo  = models.EmailField()
    tipo_Usuario = (
        ('A', 'Alumno'),
        ('P', 'Profesor'),
        ('S', 'SECRETARIA ACADEMICA'),
    )
    tipo = models.CharField(max_length=1, choices=tipo_Usuario)


    def __unicode__(self):
        return self.title

class Profesor(models.Model):
    codProfesor = models.IntegerField(primary_key = True, unique= True)
    nombrepProfesor = models.CharField(max_length=50)
    correo  = models.EmailField()
    def __unicode__(self):
        return self.title

class Curso(models.Model):
    codigoCurso = models.IntegerField(primary_key = True, unique= True)
    nombreCurso = models.CharField(max_length=50)
    seccion = models.IntegerField()
    codProfesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)


    def __unicode__(self):
        return self.title



class Asesoria(models.Model):
    codAsesoria = models.IntegerField(primary_key = True, unique= True)
    codCurso= models.OneToOneField(
      Curso,
      on_delete=models.CASCADE,
       )
    fechaAsesoria= models.CharField(max_length=30)
    #los puse como charfield porque nose como colocar horas fijas
    #hora inicio = models.CharField()
#    hora fin = models.CharField()
      # asasdads
    lugar = models.CharField(max_length=128)

    def __unicode__(self):
        return self.title

class Cita(models.Model):
    asesoria = models.ForeignKey(Asesoria, on_delete=models.CASCADE)
    nombreAlumno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    #PUEDE MEJORARSE
    tema = models.CharField(max_length=300)

    def __unicode__(self):
        return self.title
