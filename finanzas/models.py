from django.db import models

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=100, unique=True)
    razon_social = models.CharField(max_length=100)
    cuenta_bancaria = models.CharField(max_length=100)

    class Meta:
        db_table = 'proveedor'
        managed = False 
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return f"{self.razon_social} ({self.rut})"