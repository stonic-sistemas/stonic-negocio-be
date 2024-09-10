from django.db import models

class CajaEstablecimiento(models.Model):
    idcaja = models.BigIntegerField()
    idestablecimiento = models.BigIntegerField()

    class Meta:
        db_table = 'neg_cajaestablecimiento'