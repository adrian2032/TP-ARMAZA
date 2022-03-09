from django.db import models
from django.db.models.base import Model

# Create your models here.

class Materia(models.Model):
    MNombre = models.CharField('Nombre', max_length=50)

    class Meta:
        verbose_name = ("Materia")
        verbose_name_plural = ("Materias")

    def __str__(self):
        return self.MNombre

class DocenteCla(models.Model):

    Nombre = models.CharField('Nombre', max_length=50)
    Apellido = models.CharField('Apellido', max_length=50)
    Edad = models.IntegerField('Edad')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, blank=True, null=True)


    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        ordering = ['Nombre']

    def __str__(self):
        return str (self.Nombre+", "+self.Apellido)

class Oficina(models.Model):
    ONombre = models.CharField('Nombre', max_length=50)

    class Meta:
        verbose_name = ("Oficina")
        verbose_name_plural = ("Oficinas")

    def __str__(self):
        return self.ONombre

class NoDocente(models.Model):
    NNombre = models.CharField('Nombre', max_length=50)
    NApellido = models.CharField('Apellido', max_length=50)
    NEdad = models.IntegerField('Edad')
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'No Docente'
        verbose_name_plural = 'No Docentes'

    def __str__(self):
        return str (self.NNombre+", "+self.NApellido)