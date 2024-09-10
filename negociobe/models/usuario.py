from django.db import models

class Usuario(models.Model):
    idusuario = models.BigAutoField(primary_key=True)  # Auto increment field, similar to nextval
    nombres = models.CharField(max_length=100, blank=True, null=True)
    apellidos = models.CharField(max_length=100, blank=True, null=True)
    clave = models.CharField(max_length=500, blank=True, null=True)
    dni = models.CharField(max_length=10, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(unique=True)  # Define correo como EmailField
    nickname = models.CharField(max_length=255, blank=True, null=True)  # Cambié el campo para que acepte hasta 255 caracteres
    audfecharegistro = models.DateTimeField(auto_now_add=True)  # Para registrar fecha automática de creación
    fechanacimiento = models.DateField(blank=True, null=True)
    flagactivo = models.BooleanField(default=True)
    flagverificado = models.BooleanField(default=False)

    class Meta:
        db_table = 'usu_usuario'  # Nombre de la tabla en la base de datos
        constraints = [
            models.UniqueConstraint(fields=['correo'], name='uk_correo_usuario'),  # Constraint de correo único
        ]

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"