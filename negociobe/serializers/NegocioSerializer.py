from rest_framework import serializers
from negociobe.models import Negocio

class NegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negocio
        fields = ('idnegocio', 'nombre', 'telefono', 'idtiponegocio', 'ruc', 'flagverificado', 'created_at')
        read_only_fields = ('created_at',)
