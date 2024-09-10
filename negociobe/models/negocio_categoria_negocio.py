from django.db import models

class NegocioCategoriaNegocio(models.Model):
    idcategorianegocio = models.BigIntegerField()  # Correspondiente a bigint en SQL
    idnegocio = models.BigIntegerField()  # Correspondiente a bigint en SQL

    class Meta:
        db_table = 'neg_negociocategorianegocio'