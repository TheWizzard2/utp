from django.db import models

# Modelo Productor
class Productor(models.Model):
    documento_identidad = models.CharField(max_length=50, unique=True, null=False)
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    telefono = models.CharField(max_length=15, null=False)
    correo = models.EmailField(null=False)

    # Método toString cuando se necesite ver el objeto instanciado
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
# Modelo Finca
class Finca(models.Model):
    numero_catastro = models.CharField(max_length=50, unique=True, null=False)
    municipio = models.CharField(max_length=100, null=False)
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE, related_name='fincas', null=False)

    def __str__(self):
        return f"Finca {self.numero_catastro} - {self.municipio}"