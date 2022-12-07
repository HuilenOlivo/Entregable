from django.db import models

# Create your models here.
class Familiar(models.Model):
    parentesco = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.DateField()
    
    def __str__(self) -> str:
        return self.parentesco+ ''+str(self.nombre)+ ''+str(self.edad)+ ''+str(self.nacimiento)
