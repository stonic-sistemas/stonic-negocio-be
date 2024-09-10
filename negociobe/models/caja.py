from django.db import models

class Caja(models.Model):
    idcaja = models.BigIntegerField(primary_key=True)
    idsucursal = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'neg_caja'