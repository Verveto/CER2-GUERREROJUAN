from django.db import models

# Create your models here.
tema_proyecto = [
    ("0" , "Software"),
    ("1" , "Hardware"),
    ("2" , "Tesis"),
    ("3" , "Pyme"),
]

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    estudiante = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    tema = models.CharField(max_length=50, choices=tema_proyecto)
    descripcion = models.CharField(max_length=200)
    profesor = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.nombre