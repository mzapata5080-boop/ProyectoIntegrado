from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Trabajador(AbstractUser):
    rut = models.CharField(max_length=15, unique=True, verbose_name="RUT")
    telefono = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono")

    class Meta:
        db_table = 'proyecto_usuario'
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"