from django.db import models

class Negocio(models.Model):
    idnegocio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    idtiponegocio = models.ForeignKey('negociobe.MaestraArgu', on_delete=models.DO_NOTHING, db_column='idtiponegocio')
    ruc = models.CharField(max_length=20, blank=True, null=True)
    flagverificado = models.BooleanField(default=False)

    class Meta:
        db_table = 'gen_negocio'
