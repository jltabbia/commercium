from django.db import models

# Create your models here.
class Rubro(models.Model):
    codigo = models.CharField('Rubros', max_length=4,nullable=False, unique=True)
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
    codigo = models.CharField('Rubros', max_length=4,nullable=False, unique=True)
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
    codigo = models.CharField('Rubros', max_length=10,nullable=False, unique=True)
    descripcion = models.TextField()
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.IntegerField()
    stock_minimo=models.IntegerField()
    id_subrubro = models.ForeignKey(Subrubro, on_delete=models.CASCADE)
    id_proveedor = models.ForeignKey('proveedores.Proveedor', on_delete=models.CASCADE)

    def __str__(self):
            return '%s,%s,%s,%s,%s,%s,%s' % (self.id, 
                                             self.codigo, 
                                             self.descripcion, 
                                             self.precio, 
                                             self.stock, 
                                             self.stock_minimo, 
                                             self.id_subrubro,
                                             self.id_proveedor)
    
    class Meta:
        db_table = 'productos'
        ordering = ["codigo"]
        verbose_name_plural = "Productos"
        verbose_name = 'Producto'
        managed=True

