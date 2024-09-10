from django.db import models

class NegocioClienteB2C(models.Model):
    idnegocio = models.BigIntegerField()  # Correspondiente a bigint en SQL
    idcliente = models.BigIntegerField()  # Correspondiente a bigint en SQL
    audfecharegistro = models.DateTimeField()  # Correspondiente a timestamp without time zone en SQL
    audfechamodifico = models.DateTimeField(blank=True, null=True)  # Correspondiente a timestamp without time zone, puede ser nulo
    flagactivo = models.BooleanField()  # Correspondiente a boolean en SQL

    class Meta:
        db_table = 'neg_negocioclienteb2c'