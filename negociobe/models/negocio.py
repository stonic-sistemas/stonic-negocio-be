from django.db import models

class Negocio(models.Model):
    idnegocio = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    ruc = models.CharField(max_length=20, blank=True, null=True)
    flagverificado = models.BooleanField(default=False)
    idcategorianegocio = models.ForeignKey(
        'CategoriaNegocio',  # Nombre de la clase relacionada
        on_delete=models.SET_NULL,  # Si la categoría es eliminada, el campo será nulo
        null=True,  # Permitir valores nulos
        blank=True,
        db_column='idcategorianegocio'  # Nombre de la columna en la base de datos
    )

    class Meta:
        db_table = 'neg_negocio'
