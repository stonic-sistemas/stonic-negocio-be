from rest_framework import serializers
from negociobe.models.negocio import Negocio

class NegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negocio
        fields = ('__all__')
        read_only_fields = ('created_at',)

class CreateNegocioSerializer(serializers.Serializer):
    idusuario = serializers.IntegerField()
    nombrenegocio = serializers.CharField(max_length=100)
    telefono = serializers.CharField(max_length=20)
    idtiponegocio = serializers.IntegerField()
    ruc = serializers.CharField(max_length=20)