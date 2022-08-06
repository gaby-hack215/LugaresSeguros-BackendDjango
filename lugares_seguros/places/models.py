from django.db import models

# Create your models here.
class Place(models.Model):
    "Place (singular): Instancia Lugar"
    name = models.CharField(max_length=56)
    description = models.CharField(max_length=256)
    address_state = models.CharField(max_length=32)
    address_city = models.CharField(max_length=32)
    address_colonia = models.CharField(max_length=32)
    address_street = models.CharField(max_length=32)
    address_zipcode = models.CharField(max_length=32)

    class Meta:
        "places (plurar): Nombre de la tabla, donde se almacenarán los lugares"
        db_table='places'
    
    def __str__(self):
        return self.name