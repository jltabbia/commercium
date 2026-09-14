from django.db import models

# Create your models here.
class Proveedores(models.Model):
    codigo=models.CharField('Código', max_length=4,null=False,blank=False)
    nombre=models.CharField('Nombre de la Empresa',max_length=100,null=False,blank=False)
    domicilio=models.CharField('Domicilio', max_length=100,null=False,blank=False)
    provincia=models.ForeignKey('global.Provincias',on_delete=models.CASCADE)
    localidad=models.ForeignKey('global.Localidades',on_delete=models.CASCADE)
    email=models.EmailField('Email',max_length=100,null=True,blank=True)
            
    def __str__(self):
        return '%s,%s,%s,%s,%s,%s,%s' % (self.id, self.codigo, self.nombre, self.domicilio, self.provincia, self.localidad, self.email)

    class Meta:
        db_table = 'proveedores'
        ordering = ["codigo"]
        verbose_name_plural = "Proveedores"
        verbose_name = 'Proveedor'
        managed=True
