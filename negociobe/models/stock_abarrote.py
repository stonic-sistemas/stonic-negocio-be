from django.db import models

class StockAbarrote(models.Model):
    idstockabarrote = models.BigAutoField(primary_key=True)
    idnegocio = models.BigIntegerField()
    idabarrote = models.BigIntegerField()
    fechafabricacion = models.DateTimeField(blank=True, null=True)
    fechavencimiento = models.DateTimeField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    flagagotado = models.BooleanField()
    audfecharegistro = models.DateTimeField()
    audfechamodifico = models.DateTimeField(blank=True, null=True)
    audfechaagotado = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'neg_stockabarrote'