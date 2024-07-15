from django.db import models

class RelacionB2B(models.Model):
    idnegocioa = models.ForeignKey('negociobe.Negocio', on_delete=models.DO_NOTHING, db_column='idnegocioa', related_name='relaciones_b2b_a')
    idnegociob = models.ForeignKey('negociobe.Negocio', on_delete=models.DO_NOTHING, db_column='idnegociob', related_name='relaciones_b2b_b')
    idtiporelacion = models.ForeignKey('negociobe.MaestraArgu', on_delete=models.DO_NOTHING, db_column='idtiporelacion')

    class Meta:
        db_table = 'gen_relacionb2b'