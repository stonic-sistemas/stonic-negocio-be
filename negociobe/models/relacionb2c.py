from django.db import models

class RelacionB2C(models.Model):
    idusuario = models.IntegerField()
    idnegocio = models.ForeignKey('negociobe.Negocio', on_delete=models.DO_NOTHING, db_column='idnegocio')
    idtiporelacion = models.ForeignKey('negociobe.MaestraArgu', on_delete=models.DO_NOTHING, db_column='idtiporelacion')

    class Meta:
        db_table = 'gen_relacionb2c'