from django.db import models

class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    # Define los otros campos necesarios para gen_producto

    class Meta:
        db_table = 'gen_producto'