from django.db import models

# Create your models here.
class Empresa(models.Model):
    codigo=models.CharField('Código', max_length=4,null=False,blank=False)
    nombre=models.CharField('Nombre de la Empresa',max_length=100,null=False,blank=False)
    domicilio=models.CharField('Domicilio', max_length=100,null=False,blank=False)
    provincia=models.ForeignKey('global.Provincias',on_delete=models.CASCADE)
    localidad=models.ForeignKey('global.Localidades',on_delete=models.CASCADE)
            
    def __str__(self):
        return '%s,%s,%s,%s,%s,%s' % (self.id, self.codigo, self.nombre, self.domicilio, self.provincia, self.localidad)

    class Meta:
        db_table = 'empresa'
        ordering = ["codigo"]
        verbose_name_plural = "Empresas"
        verbose_name = 'Empresa'
        managed=True