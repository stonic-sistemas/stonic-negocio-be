from django.db import models

class CategoriaNegocio(models.Model):
    idcategorianegocio = models.BigIntegerField(primary_key=True)  # Correspondiente al tipo bigint en SQL y clave primaria
    nombre = models.CharField(max_length=100)  # Correspondiente al tipo character varying(100) en SQL
    idpadre = models.BigIntegerField(blank=True, null=True)  # Correspondiente al tipo bigint en SQL, puede ser nulo

    class Meta:
        db_table = 'neg_categorianegocio'