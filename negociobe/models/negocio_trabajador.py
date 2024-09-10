from django.db import models

class NegocioTrabajador(models.Model):
    idnegocio = models.BigIntegerField(primary_key=True)
    idtrabajador = models.BigIntegerField()  # Correspondiente a bigint en SQL
    idroltrabajador = models.BigIntegerField()  # Correspondiente a bigint en SQL
    audfecharegistro = models.DateTimeField()  # Correspondiente a timestamp without time zone en SQL
    audfechamodifico = models.DateTimeField(blank=True, null=True)  # Correspondiente a timestamp without time zone, puede ser nulo
    flagactivo = models.BooleanField()  # Correspondiente a boolean en SQL

    class Meta:
        db_table = 'neg_negociotrabajador'