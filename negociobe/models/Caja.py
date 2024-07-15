from django.db import models

class Caja(models.Model):
    idcaja = models.AutoField(primary_key=True)
    idsucursal = models.ForeignKey('negociobe.Sucursal', on_delete=models.DO_NOTHING, db_column='idsucursal')
    numero = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'gen_caja'