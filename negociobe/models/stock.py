from django.db import models

class Stock(models.Model):
    idsucursal = models.ForeignKey('negociobe.Sucursal', on_delete=models.DO_NOTHING, db_column='idsucursal')
    idproducto = models.ForeignKey('negociobe.Producto', on_delete=models.DO_NOTHING, db_column='idproducto')
    fechafabricacion = models.DateTimeField(blank=True, null=True)
    fechavencimiento = models.DateTimeField(blank=True, null=True)
    audfecharegistro = models.DateTimeField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    preciomayor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    preciomenor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'inv_stock'