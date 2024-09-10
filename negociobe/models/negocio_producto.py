from django.db import models

class NegocioProducto(models.Model):
    idnegocio = models.BigIntegerField(primary_key=True)
    idproducto = models.BigIntegerField()
    audfecharegistro = models.DateTimeField()

    class Meta:
        db_table = 'neg_negocioproducto'