from django.db import models
from proveedores.models import Proveedores

# Create your models here.

class Rubro(models.Model):
    codigo = models.CharField('Rubros', max_length=4,null=True, blank=True)
    descripcion = models.TextField()

    def __str__(self):
            return '%s,%s,%s' % (self.id, self.codigo, self.descripcion)
    
    class Meta:
        db_table = 'rubro'
        ordering = ["codigo"]
        verbose_name_plural = "Rubros"
        verbose_name = 'Rubro'
        managed=True

class Subrubro(models.Model):
    codigo = models.CharField('Rubros', max_length=4,null=True, blank=True)
    descripcion = models.TextField()
    id_rubro = models.ForeignKey(Rubro, on_delete=models.CASCADE)

    def __str__(self):
            return '%s,%s,%s,%s' % (self.id, self.codigo, self.descripcion, self.id_rubro)
    
    class Meta:
        db_table = 'subrubro'
        ordering = ["codigo"]
        verbose_name_plural = "Subrubros"
        verbose_name = 'Subrubro'
        managed=True

class Producto(models.Model):
    codigo = models.CharField('Rubros', max_length=10,null=True, blank=True)
    descripcion = models.TextField()
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.IntegerField()
    stock_minimo=models.IntegerField()
    rubro = models.ForeignKey(Rubro, on_delete=models.CASCADE)
    subrubro = models.ForeignKey(Subrubro, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

    def __str__(self):            
         return '%s,%s,%s,%s,%s,%s,%s,%s' % (self.id, 
                                             self.codigo, 
                                             self.descripcion, 
                                             self.precio, 
                                             self.stock, 
                                             self.stock_minimo, 
                                             self.rubro,
                                             self.subrubro,
                                             self.proveedor)
    
    class Meta:
        db_table = 'productos'
        ordering = ["codigo"]
        verbose_name_plural = "Productos"
        verbose_name = 'Producto'
        managed=True

