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

    # Relación 1 a muchos, 1 Productor a muchas fincas
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE, related_name='fincas', null=False)

    def __str__(self):
        return f"Finca {self.numero_catastro} - {self.municipio}"
    
# Modelo Vivero
class Vivero(models.Model):
    codigo = models.CharField(max_length=50, null=False)
    tipo_cultivo = models.CharField(max_length=100, null=False)

    # Relación 1 a muchos, 1 Finca a muchos viveros
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE, related_name='viveros', null=False)

    def __str__(self):
        return f"Vivero {self.codigo} - {self.tipo_cultivo}"
    
# Modelo Labor
class Labor(models.Model):
    fecha = models.DateField(null=False)
    descripcion = models.TextField(null=False)

    # Relación 1 a muchos, 1 Vivero a muchas labores
    vivero = models.ForeignKey(Vivero, on_delete=models.CASCADE, related_name='labores', null=False)

    def __str__(self):
        return f"Labor {self.descripcion} - {self.fecha}"
    
# Modelo Producto Control
# Clase abstracta
class ProductoControl(models.Model):
    registro_ica = models.CharField(max_length=50, null=False)
    nombre_producto = models.CharField(max_length=100, null=False)
    frecuencia_aplicacion = models.CharField(max_length=50, null=False)
    valor_producto = models.FloatField(null=False)

    # Ya que el modelo es abstracto no se instancia en BD
    # Se usa como modelo base para extender a otros modelos
    # Desde aquí se heredarán los atributos a otras clases hijas
    class Meta:
        abstract = True

# Modelo Producto Control Hongo
# Clase hereda de Producto Control
class ProductoControlHongo(ProductoControl):
    periodo_carencia = models.IntegerField(null=False)
    nombre_hongo = models.CharField(max_length=100, null=False)

# Modelo Producto Control Plaga
# Clase hereda de Producto Control
class ProductoControlPlaga(ProductoControl):
    periodo_carencia = models.IntegerField(null=False)

# Modelo Producto Control Fertilizante
# Clase hereda de Producto Control
class ProductoControlFertilizante(ProductoControl):
    fecha_ultima_aplicacion = models.DateField(null=False)