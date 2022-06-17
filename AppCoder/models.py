from django.db import models

# Create your models here.

class Usuario(models.Model):  
    nombre = models.CharField('nombre_user', max_length=25)
    apellido = models.CharField('apellido', max_length=25)
    edad = models.IntegerField('edad')

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'



class Producto(models.Model):
    nombre = models.CharField('nombre_prod', max_length=50)
    precio = models.IntegerField('precio')
    stock = models.IntegerField('stock')
    categoria = models.CharField('categoria', max_length=50)

    def __str__(self) -> str:
        return f'{self.nombre}'



class Carrito(models.Model):
    producto = models.CharField('producto', max_length=50)
    cantidad = models.IntegerField('cantidad')

    def __str__(self) -> str:
        return f'{self.producto}'
