from rest_framework import serializers

from negociobe.models import CategoriaNegocio
from negociobe.models.negocio import Negocio
from negociobe.models.usuario import Usuario


class NegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negocio
        fields = ('__all__')
        read_only_fields = ('created_at',)

class CreateNegocioSerializer(serializers.Serializer):
    idusuario = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all())
    nombrenegocio = serializers.CharField(max_length=100)
    telefono = serializers.CharField(max_length=20)
    ruc = serializers.CharField(max_length=20)
    idcategorianegocio = serializers.PrimaryKeyRelatedField(
        queryset=CategoriaNegocio.objects.all())