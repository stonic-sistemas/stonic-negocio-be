from django.db import models

class MaestraArgu(models.Model):
    idargu = models.IntegerField(primary_key=True)
    # Agrega otros campos de la tabla gen_maestraargu si los hay

    class Meta:
        db_table = 'gen_maestraargu'